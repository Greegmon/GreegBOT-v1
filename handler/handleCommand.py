from data import botInfo
from handler.load_module import commands
import json

botAdmins = botInfo.admins
prefix = botInfo.prefix

bannedUsers = json.load(open('database/bannedUsers.json', 'r'))
bannedThreads = json.load(open('database/bannedThreads.json', 'r'))

def handleCommand(api, mid,author_id,message,message_object,thread_id,thread_type,ts,metadata,msg):
	event = {
		"mid": mid,
		"author_id": author_id,
		"message": message,
		"message_object": message_object,
		"thread_id": thread_id,
		"thread_type": thread_type,
		"ts": ts,
		"metadata": metadata,
		"msg": msg
	}
	cmd,*args = message.split(maxsplit=1)
	thread = api.fetchThreadInfo(thread_id)[thread_id]

	# Execute the commands function
	def function_execute(name):
		commands[name]['function'](api, event, args[0] if args else '')

	# check if user/thread is ban
	def is_ban(user: str, thread: str):
		if user in bannedUsers:
			text = f"❌ You are banned using {botInfo.name}\n\nReason » {bannedUsers[user]}"
			return text
		elif thread in bannedThreads:
			text = f"❌ This thread is banned\n\nReason » {bannedThreads[thread]}"
			return text
		else:
			return False
	chopchop = is_ban(author_id, thread_id)

	# check the permission and call the function_execute
	def permiso(I):
		perm = commands[I]['permission']
		if perm == 0:
			function_execute(I)
		elif perm == 1:
			if author_id in thread.admins or author_id in botAdmins:
				function_execute(I)
			else:
				api.sendReply(
					"Only group admins can use this command",
					mid,
					thread_id=thread_id,
					thread_type=thread_type
				)
		elif perm == 2:
			if author_id in botAdmins:
				function_execute(I)
			else:
				api.sendReply(
					"Only bot admins can use this command",
					mid,
					thread_id=thread_id,
					thread_type=thread_type
				)
		else:
			api.sendReply(
				"❌ error while fetching the command",
				mid,
				thread_id=thread_id,
				thread_type=thread_type
			)
	
	if message.startswith(prefix) and cmd[1:].lower() in commands and commands[cmd[1:].lower()]['use_prefix']:
		if chopchop:
			api.sendReply(chopchop, mid, thread_id=thread_id, thread_type=thread_type)
		else:
			permiso(cmd[1:].lower())
	else:
		if cmd.lower() in commands:#  and not commands[cmd.lower()]['use_prefix']:
			if chopchop:
				api.sendReply(chopchop, mid, thread_id=thread_id, thread_type=thread_type)
			else:
				permiso(cmd.lower())
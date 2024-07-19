from utils import font
from handler.load_module import commands as Lopi

line = "━━━━━━━━━━━━━━━━━━━"

# /help all
def fetch_all_commands(cmd, lenCmd):
	xyz = f"{font('All Commands', 'bold')}\n"
	xyz += line + '\n'
	for A in cmd:
		xyz += f"➥ {A['name']} {A['usage']}\n"
	xyz += f"{line}\n{font('Total Commands', 'sans')}: {lenCmd}"
	return font(xyz, 'sans')

# /help <cmd name>
# e.g /help uid
def usage_command(cmd, commandName):
	def role(r):
		if int(r) == 0:
			return 'User'
		if int(r) == 1:
			return 'Admin'
		if int(r) == 2:
			return 'Bot Admin'
		if int(r) not in [1,2,3]:
			return 'User'
	for greeg in cmd:
		if commandName.lower() == greeg['name']:
			xyz = ""
			xyz += f"{font('name', 'bold')}: {greeg['name']}\n"
			xyz += f"{font('version', 'bold')}: {greeg['version']}\n"
			xyz += f"{font('credits', 'bold')}: {greeg['credits']}\n"
			xyz += f"{font('usage', 'bold')}: {greeg['usage']}\n"
			xyz += f"{font('description', 'bold')}: {greeg['description']}\n"
			xyz += f"{font('usePrefix', 'bold')}: {greeg['use_prefix']}\n"
			xyz += f"{font('role', 'bold')}: {role(greeg['role'])}\n"
			return font(xyz, 'sans')
	return f"""{font("No command name found, use '/help' to see all commands", 'sans')}"""

# /help <page | none>
# e.g /help
# or /help 2
def fetch_command(cmd, lenCmd, page=None):
	vorat = [cmd[i:i+10] for i in range(0, len(cmd), 10)]
	if not page:
		xyz = f"{font('Command List', 'bold')}\n{line}\n"
		for i in vorat[0]:
			xyz += f"➥ {i['name']}\n"
		xyz += line + '\n'
		xyz += f"{font('Page', 'bold')} : (1/{len(vorat)})\n"
		xyz += f"{font('Total Commands', 'bold')}: {lenCmd}"
		return font(xyz, 'sans')
	elif int(page) <= len(vorat):
		xyz = "Command List\n\n"
		xyz += f"{font('Total Commands', 'bold')} : {lenCmd}\n" + line + "\n\n"
		for i in vorat[int(page)-1]:
			xyz += f"➥ {i['name']}\n"
		xyz += line + '\n'
		xyz += f"{font('Page', 'bold')} : (1/{len(vorat)})\n"
		xyz += f"{font('Total Commands', 'bold')}: {lenCmd}"
		return font(xyz, 'sans')
	else:
		return "Command page not found"


def help_command(api, event, text):
	commands = []
	for cmd in Lopi:
		commands.append({
			"name": cmd,
			"version": Lopi[cmd]['version'],
			"credits": Lopi[cmd]['credits'],
			"usage": Lopi[cmd]['usage'],
			"description": Lopi[cmd]['description'],
			"use_prefix": Lopi[cmd]['use_prefix'],
			"role": Lopi[cmd]['permission']
		})
	lenCmd = len(commands)
	tid = event['thread_id']
	type = event['thread_type']
	mid = event['mid']
	try:
		if not text:
			api.sendReply(fetch_command(commands, len(commands)), mid, thread_id=tid, thread_type=type)
		elif text not in [str(i) for i in range(1,999)] and text not in ['all', 'All', 'ALL', 'aLl', 'alL', 'ALl']:
			api.sendReply(usage_command(commands, text), mid, thread_id=tid, thread_type=type)
		elif text in [str(i) for i in range(1,999)]:
			api.sendReply(fetch_command(commands,len(commands), page=text), mid, thread_id=tid, thread_type=type)
		elif text in ['all', 'All', 'ALL', 'aLl', 'alL', 'ALl']:
			api.sendReply(fetch_all_commands(commands, len(commands)), mid, thread_id=tid, thread_type=type)
		else:
			api.sendReply("❌ error while fetching commands", mid, thread_id=tid, thread_type=type)
	except Exception as e:
		api.sendReply(f"❌ error: {e}", mid, thread_id=tid, thread_type=type)

config = {
	"name": 'help',
	"version": '1.0.0',
	"permission": 0,
	"credits": 'Greegmon',
	"usage": '[all/page/None]',
	"use_prefix": True,
	"description": "See all commands",
	"function": help_command
}
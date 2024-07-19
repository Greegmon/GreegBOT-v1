from handler.handleCommand import handleCommand
import json
print("\033[1;93m[ GREEG ] » \033[0;97mMessage handler loaded")
def handleMessage(api, mid=None,author_id=None,message=None,message_object=None,thread_id=None,thread_type=None,ts=None,metadata=None,msg=None):
	#print(message_object.original_dimensions.id)
	banned_users = json.load(open("database/bannedUsers.json", 'r'))
	if api.uid != author_id:
		if author_id in banned_users:
			return api.sendReply(
				"❌ Your are not allowed using this bot\n\nREASON [BAN USER] - Test Reason",
				mid,
				thread_id=thread_id,
				thread_type=thread_type
			)
		handleCommand(api,mid,author_id,message,message_object,thread_id,thread_type,ts,metadata,msg)
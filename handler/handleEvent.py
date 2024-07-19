from utils import font
from data import botInfo

def joinNoti(api, mid=None, added_ids=None, author_id=None, thread_id=None, thread_type=None, **kwargs):
	users=[]
	thread = api.fetchThreadInfo(thread_id)[thread_id]
	for i in added_ids:
		user = api.fetchUserInfo(i)[i]
		users.append(user.name)
	j = ', '.join(users) if len(users) > 1 else users[0]
	text = font(f"Welcome {font(j, 'bold')} to {thread.name}", 'sans')
	if api.uid not in added_ids:
		api.sendMessage(text, thread_id=thread_id, thread_type=thread_type)
	else:
		api.sendMessage(
			font(f"Thank you for using {botInfo.name}, type '{botInfo.prefix}help' to see my commands\n\nowner » {botInfo.owner_name}\nlink » {botInfo.owner_fb}", 'sans'),
			thread_id=thread_id,
			thread_type=thread_type
		)
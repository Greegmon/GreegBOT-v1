def uid(api, event, args):
	msg = event['message_object']
	tid = event['thread_id']
	type = event['thread_type']
	mid = event['mid']
	try:
		if msg.replied_to is not None:
			rep = msg.replied_to
			user = api.fetchUserInfo(rep.author)[rep.author]
			text = f"name: {user.name}\nuid: {user.uid}"
			return api.sendReply(text, mid, thread_id=tid, thread_type=type)
		elif msg.mentions:
			text = ""
			for mention in msg.mentions:
				user = api.fetchUserInfo(mention.thread_id)[mention.thread_id]
				text += f"name: {user.name}\nuid: {user.uid}\n\n"
			api.sendReply(
				text,
				mid,
				thread_id=tid,
				thread_type=type
			)
		else:
			user = api.fetchUserInfo(event['author_id'])[event['author_id']]
			text = f"name: {user.name}\nuid: {user.uid}"
			return api.sendReply(
				text,
				mid,
				thread_id=tid,
				thread_type=type
			)
	except Exception as e:
		api.sendReply(f"❌ error: {e}", mid, thread_id=tid, thread_type=type)

config = {
	"name": 'uid',
	"version": '1.0.0',
	"credits": 'Greegmon',
	"usage": '[reply/mention/None]',
	"use_prefix": False,
	"permission": 0,
	"function": uid
}
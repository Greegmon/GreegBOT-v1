from data import botInfo

def prefix(api, event, args):
	try:
		api.sendReply(
			f"my prefx: {botInfo.prefix}",
			event['mid'],
			thread_id=event['thread_id'],
			thread_type=event['thread_type']
		)
	except Exception as d:
		print(d)

config = {
	"name": 'prefix',
	"version": '1.0.0',
	"credits": 'Greegmon',
	"use_prefix": False,
	"function": prefix
}
from utils import font
import requests

def gemini(api, event, args):
	tid = event['thread_id']
	type = event['thread_type']
	mid = event['mid']
	
	if not args:
		return api.sendReply(font('Please provide a question first!', 'sans'), mid, thread_id=tid, thread_type=type)
	try:
		api.sendReply(font('Answering please wait...', 'sans'), mid, thread_id=tid, thread_type=type)
		respo = requests.get(f'https://joshweb.click/new/gemini?prompt={args}').json()
		result = respo['result']['data']
		api.sendReply(font(result, 'sans'), mid, thread_id=tid, thread_type=type)
	except Exception as e:
		api.sendMessage(
			font(f"❌ error: {e}",'sans'),
			thread_id=tid,
			thread_type=type
		)

config = {
	"name": 'gemini',
	"version": '1.0.0',
	"credits": 'Greeg (api by Joshua Sy)',
	"usage": '[prompt]',
	"use_prefix": True,
	"permission": 0,
	"function": gemini
}
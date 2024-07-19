from fbchat import Client, ThreadType
from fbchat.models import *
import json
from handler import *
from data import botInfo

class Greeg(Client):
	
	def onMessage(self, mid=None, author_id=None, message=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, ts=None, metadata=None, msg=None, **kwargs):
		self.markAsRead(thread_id)
		handleMessage(self, mid=mid, author_id=author_id, message=message, message_object=message_object, thread_id=thread_id, thread_type=thread_type, ts=ts, metadata=metadata, msg=msg)

	"""
	EVENT
	"""
	# joinNoti
	def onPeopleAdded(self, mid=None, added_ids=None, author_id=None, thread_id=None, ts=None, msg=None):
		joinNoti(self, mid=mid, added_ids=added_ids, author_id=author_id, thread_id=thread_id, thread_type=ThreadType.GROUP)

if __name__ == '__main__':
	print("\033[1;96m[ LOADING ] » \033[0;97mLogging in....")
	cookies = {i['key']: i['value'] for i in json.load(open('appstate.json', 'r'))}
	try:
		greeg = Greeg('', '', session_cookies=cookies)
		if greeg.isLoggedIn():
			print(f"\033[1;92m[ GREEG ] » \033[96m{botInfo.name} \033[0;97mSuccessfully logged in.")
		greeg.listen()
	except:
		print("\033[1;91m[ ERROR ] » \033[0;91mError while logging in, please try again or change your appstate")
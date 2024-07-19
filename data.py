import json
from dataclasses import dataclass

@dataclass
class botInfo:
	name: str
	prefix: str
	owner_name: str
	owner_age: str
	owner_fb: str
	admins: list

def load_data():
	with open('config.json', 'r') as f:
		info = json.load(f)
		botInfo.name = info['bot']['name']
		botInfo.prefix = info['bot']['prefix']
		botInfo.owner_name = info['owner']['name']
		botInfo.owner_age = info['owner']['age']
		botInfo.owner_fb = info['owner']['fb']
		botInfo.admins = info['admins']

load_data()
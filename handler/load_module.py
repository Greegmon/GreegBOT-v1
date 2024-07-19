import os
from importlib import import_module as Import
import time
print("\033[1;96m[ LOADING ] » \033[0;97mFetching Commands please wait......")
commands = {}
error = lambda f, r: print(f"\033[1;91m[ ERROR ] (\033[93m{f}\033[91m) » \033[0;91m{r}")
done = lambda name: print(f"\033[1;92m[ GREEG ] » \033[0;97mCommand loaded \033[95m{name}")
for file in os.listdir('commands'):
	if file.endswith('.py') and file != '__init__.py':
		fileName = file[:-3]
		module = Import(f'commands.{fileName}')
		info = getattr(module, 'config', None)
		if info:
			def geti(y,n):
				re = n if not info.get(y) or not info[y] else info[y]
				return re
			name = info['name']
			use_prefix = info['use_prefix']
			permission = info['permission']
			function = info['function']
			version = geti('version', '1.0.0')
			credits = geti('credits', 'Developer')
			usage = geti('usage', '')
			description = geti('description', 'No Descriptiond')
			if type(use_prefix) != bool:
				error(fileName, f"Prefix must be 'bool' not {use_prefix}")
			if int(permission) not in [0, 1, 2]:
				permission = 0
			if type(use_prefix) == bool and int(permission) in [0, 1, 2]:
				commands[name.lower()] = {
					"use_prefix": use_prefix,
					"permission": permission,
					"function": function,
					"version": version,
					"credits": credits,
					"usage": usage,
					"description": description
				}

for i in commands:
	done(i)
	time.sleep(0.1)
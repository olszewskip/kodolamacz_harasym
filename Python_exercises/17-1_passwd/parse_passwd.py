SPLITBY = ':'
COMMENTSIGN = '#'

passwd_path = './passwd_file.txt'
shadow_path = './shadow_file.txt'
group_path = './group_file.txt'

user_data_base = {} # dict of dicts, {login: {'login': login, ...}, ...}


# handle passwd
with open(passwd_path) as file:
	for line in file:
		line = line.strip()
		if line and line[0] != COMMENTSIGN:
			raw = line.split(SPLITBY)
			login, _, uid, gid, _, home, shell, *_ =  raw
			
			if login in user_data_base:
				user_data_base[login]['uid'] = int(uid)
				user_data_base[login]['guid'] = int(guid)
				user_data_base[login]['home'] = home
				user_data_base[login]['shell'] = shell
				
			else:
				user_data_base[login] = {
					'login': login,
					'uid': int(uid),
					'gid': int(gid),
					'home': home,
					'shell': shell,
					}

				
# handle shadow		
DECODE_ALGOS= {
	'1': 'MD5',
	'2a': 'Blowfish',
	'2y': 'Blowfish',
	'5': 'SHA-256',
	'6': 'SHA-512'
	}

with open(shadow_path) as file:
	for line in file:
		line = line.strip()		
		if line and line[0] != COMMENTSIGN:
			raw = line.split(SPLITBY)
			login, password_field, days_since_change, *_ = raw
			
			locked = None
			password = None
			algorithm = None
			date_changed = None
			
			if '!' in password_field:
				locked = True
				#password = 'locked'
				
			elif "*" in password_field:
				locked = False
				#password = 'never_given'
				
			elif password_field[0] == '$':
				locked = False
				if password_field[2] == '$':
					algo_code = password_field[1]
					password = password_field[2:]
				elif password_field[3] == '$':
					algo_code = password_field[1:3]
					password = password_field[3:]					
				algorithm = DECODE_ALGOS[algo_code]

			from datetime import datetime, timedelta
			date_changed = datetime(1970,1,1) + timedelta(days=int(days_since_change))
			
			if login in user_data_base:
				user_data_base[login]['locked'] = locked
				user_data_base[login]['password'] = password
				user_data_base[login]['algorithm'] = algorithm			
				user_data_base[login]['lastchanged'] = date_changed
				
			else:
				user_data_base[login] = {
					'login': login,
					'locked': locked,
					'password': password,
					'algorithm': algorithm,
					'lastchanged': date_changed
					}

				
with open(group_path) as file:
	for line in file:
		line = line.strip()		
		if line and line[0] != COMMENTSIGN:
			raw = line.split(SPLITBY)
			group, _, _, members = raw
			members = members.split(',')
			
			for login in members:
				if login in user_data_base:
					if 'groups' in user_data_base[login]:
						if group not in user_data_base[login]['groups']:
							user_data_base[login]['groups'].append(group)
					else:
						user_data_base[login]['groups'] = [group]
				
				else:
					user_data_base[login] = {
						'login': login,
						'groups': [group]
						}
							

for login, user in user_data_base.items():
	assert(user['login'] == login)

users = [dict_ for dict_ in user_data_base.values()]
KEYS = ['login', 'uid', 'gid', 'home', 'shell', 'algorithm', 'password', 'groups', 'lastchanged', 'locked']
for user in users:
	for key in KEYS:
		if key in user:
			print(key + ":", user[key])
	print('-' * 67)
	

def CONDITION(login):
	return 'uid' in user_data_base[login] and user_data_base[login]['uid'] >= 1000
	
print([login for login in user_data_base if CONDITION(login)])
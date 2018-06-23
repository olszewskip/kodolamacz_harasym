SPLITBYSIGN = ':'
COMMENTSIGN = '#'

passwd_path = './passwd_file.txt'
shadow_path = './shadow_file.txt'
group_path = './group_file.txt'

user_data_base = {}  # dict of dicts, {login: {'login': login, ...}, ...}

# handle passwd
with open(passwd_path) as file:
    for line in file:
        line = line.strip()

        if not line or line[0] == COMMENTSIGN:
            continue

        raw = line.split(SPLITBYSIGN)
        login, _, uid, gid, _, home, shell, *_ = raw
        uid = int(uid)
        gid = int(gid)

        if uid < 1000:
            continue

        user_data_base[login] = {
            'login': login,
            'uid': uid,
            'gid': gid,
            'home': home,
            'shell': shell
        }


# handle shadow
with open(shadow_path) as file:
    for line in file:
        line = line.strip()

        if not line or line[0] == COMMENTSIGN:
            continue

        raw = line.split(SPLITBYSIGN)
        login, password_field, days_since_change, *_ = raw

        locked = None
        password = None
        algorithm = None
        date_changed = None

        if '!' in password_field:
            locked = True

        elif "*" in password_field:
            locked = False

        elif password_field[0] == '$':
            locked = False
            algo_code = None
            DECODE_ALGOS = {
                '1': 'MD5',
                '2a': 'Blowfish',
                '2y': 'Blowfish',
                '5': 'SHA-256',
                '6': 'SHA-512'
            }

            if password_field[2] == '$':
                algo_code = password_field[1]
                password = password_field[2:]

            elif password_field[3] == '$':
                algo_code = password_field[1:3]
                password = password_field[3:]

            algorithm = DECODE_ALGOS[algo_code]

        from datetime import date, timedelta

        date_changed = date(1970, 1, 1) + timedelta(days=int(days_since_change))

        if login in user_data_base:
            user_data_base[login]['locked'] = locked
            user_data_base[login]['password'] = password
            user_data_base[login]['algorithm'] = algorithm
            user_data_base[login]['lastchanged'] = date_changed

# handle group
with open(group_path) as file:
    for line in file:
        line = line.strip()

        if not line or line[0] == COMMENTSIGN:
            continue

        raw = line.split(SPLITBYSIGN)
        group, _, _, members = raw
        members = members.split(',')

        for login in members:

            if login in user_data_base:

                if 'groups' in user_data_base[login] \
                        and group not in user_data_base[login]['groups']:
                    user_data_base[login]['groups'].append(group)
                else:
                    user_data_base[login]['groups'] = [group]


for login, user in user_data_base.items():
    assert (user['login'] == login)

users = [dict_ for dict_ in user_data_base.values()]

from pprint import pprint
pprint(users)

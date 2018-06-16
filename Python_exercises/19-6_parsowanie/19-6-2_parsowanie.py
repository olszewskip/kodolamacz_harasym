from pprint import pprint

FILENAME = './hosts'

with open(FILENAME) as file:

    hosts = {}

    for line in file:
        line = line.strip()

        if not line or line[0] == '#':
            continue

        ip, *host_names = line.split()

        prot = '.' in ip
        decode_prot = {False: 'ipv6', True: 'ipv4'}
        protocol = decode_prot[prot]

        if ip not in hosts:
            hosts[ip] = {
                'ip': ip,
                'hostnames': host_names,
                'protocol': protocol
            }
        else:
            hosts[ip]['hostnames'].extend(host_names)

    pprint(list(hosts.values()))






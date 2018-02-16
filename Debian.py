import os
import random
import getpass
import sys

args = sys.argv

def n():
    gera = random.choice('abcdef0123456789')
    return gera;
def MacAddress():
    gera = """eth0      Link encap:Ethernet  Endereço de HW {}{}:{}{}:{}{}:{}{}:{}{}:{}{}
          inet end.: 10.0.2.15  Bcast:10.0.2.15  Masc:255.255.255.0
          endereço inet6: fdf4:22ef:e281:1:a00:27ff:fe66:93f5/64 Escopo:Global
          endereço inet6: 2804:431:f701:f3f2:a00:27ff:fe66:93f5/64 Escopo:Global
          endereço inet6: fe80::a00:27ff:fe66:93f5/64 Escopo:Link
          UP BROADCASTRUNNING MULTICAST  MTU:1500  Métrica:1
          RX packets:18572 errors:0 dropped:0 overruns:0 frame:0
          TX packets:2726 errors:0 dropped:0 overruns:0 carrier:0
          colisões:0 txqueuelen:1000
          RX bytes:21366716 (20.3 MiB)  TX bytes:194697 (190.1 KiB)
 lo        Link encap:Loopback Local
          inet end.: 127.0.0.1  Masc:255.0.0.0
          endereço inet6: ::1/128 Escopo:Máquina
          UP LOOPBACKRUNNING  MTU:65536  Métrica:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          colisões:0 txqueuelen:0
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
          """.format(n(), n(), n(), n(), n(), n(), n(), n(), n(), n(), n(), n())
    return gera;

code = 'false'
hostname = 'debian'
comm = 'start'
passco = '123'
os.system('cls||clear')

print('Debian GNU/Linux 8 debian tty1\n')
user = str(input('{} login: '.format(hostname)))
#passw = getpass.getpass("Password: ")
passw = str(input('Password: '))

if user == 'guest' and passw == 'guest':
    print("""
The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.""")

    while comm != 'exit' and comm != 'shutdown -h' and comm != 'shutdown':
        if comm == '--help':
            print('\nAvailable Commands:\n\nexit\nshutdown\nshutdown -h\nclear\nhostname\nwhoami')

        if comm == 'clear':
            os.system('cls||clear')

        if comm == 'whoami':
            print(user)

        if comm == 'hostname':
            if len(comm) == 8:
                print(hostname)

        if comm == 'su':
            senha = str(input('Senha: '))

            if senha == passco:
                user = 'root'
                code = 'true'
                comm = 'exit'
            else:
                print('su: Falha na autenticação')

        comm = str(input('{}@{}:~# '.format(user, hostname)))

        if comm != 'exit' and comm != '' and comm != 'shutdown' and comm != 'shutdown -h' and comm != 'clear' and comm != 'su' and comm != 'hostname' and comm != 'whoami' and comm != '--help':
            print('bash: {}: comando não encontrado'.format(comm))

if user == 'root' and passw == passco or code == 'true' and args[1] != '--help':
    if code != 'true':
        print("""
The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.""")

    while comm != 'exit' and comm != 'shutdown -h' and comm != 'shutdown' or code == 'true':
        if comm == 'clear':
            os.system('cls||clear')

        if comm == 'hostname':
            if len(comm) == 8:
                print(hostname)

        if comm == 'ifconfig':
            print(MacAddress())

        if comm == 'ip route':
            print("""default via 10.0.2.2 dev eth0\n10.0.2.0/24 dev eth0  proto kernel  scope link  src 10.0.2.15""")

        if comm[0:8] == 'hostname':
            if len(comm) > 9:
                hostname = comm[9:20]

        if comm == 'whoami':
            print(user)

        if comm == '--help':
            print('\nAvailable Commands:\n\nexit\nshutdown\nshutdown -h\nclear\nhostname\nhostname <new_hostname>\nifconfig\nip route\nwhoami')

        if comm[0:4] == 'ping':
            os.system("ping " + comm[5:20])

        comm = str(input('{}@{}:~# '.format(user, hostname)))

        if comm != 'exit' and comm[0:4] != 'ping' and comm != '' and comm != 'shutdown' and comm != 'shutdown -h' and comm != 'clear' and comm != 'hostname' and comm != 'ifconfig' and comm != 'ip route' and comm[0:8] != 'hostname' and comm != 'whoami' and comm != '--help':
            print('bash: {}: comando não encontrado'.format(comm))
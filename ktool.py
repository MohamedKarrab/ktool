import os
import sys
import paramiko
import time
import argparse
import logging
import threading
import itertools
import subprocess
from ssh_bruteforce import ssh_bruteforce
from w_gen_mod import w_gen_mod

def sys_arg_cleaner():
    prog_name = sys.argv[0]
    sys.argv.clear()
    sys.argv.append(prog_name)


def main():
    choice = 1000
    while (choice != 3):
        subprocess.run(['clear'])
        welcome = r"""
        ██╗░░██╗████████╗░█████╗░░█████╗░██╗░░░░░
        ██║░██╔╝╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
        █████═╝░░░░██║░░░██║░░██║██║░░██║██║░░░░░
        ██╔═██╗░░░░██║░░░██║░░██║██║░░██║██║░░░░░
        ██║░╚██╗░░░██║░░░╚█████╔╝╚█████╔╝███████╗
        ╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝"""

        welcome+= "\n\nktool 1.12 Copyright (c) 2023 by Mohamed Karrab\n\n"

        welcome+= """Select from the menu:
            1) ssh bruteforce
            2) wordlist generation/modification
            3) exit
"""
        welcome += "\033[4mktool\033[0m" + "> "
        print(welcome,end="")
        choice = input()
        if (choice == "1"):
            ssh_bruteforce()
            sys_arg_cleaner()
            main()
        elif (choice == "2"):
            w_gen_mod()
            sys_arg_cleaner()
            main()
        elif (choice == "3"):
            sys.exit()
        print("")


if __name__ == '__main__':
    main()
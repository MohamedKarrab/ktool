import subprocess
from ssh_bruteforce import ssh_bruteforce
from w_gen_mod import w_gen_mod
from file_downloader import file_downloader
from information_gatherer import information_gatherer
from utilities import *

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

        welcome+= "\n\nktool 1.2.1 Copyright (c) 2023 by Mohamed Karrab\n\n"

        welcome+= """Select from the menu:
            1) ssh bruteforce
            2) wordlist generation/modification
            3) file downloader
            4) information gathering
            5) exit
"""
        welcome += "\033[4mktool\033[0m" + "> "
        print(welcome,end="")
        choice = input()
        if (choice == "1"):
            while(ssh_bruteforce()==True):
                sys_arg_cleaner()

        elif (choice == "2"):
            while(w_gen_mod()==True):
                sys_arg_cleaner()
        elif (choice == "3"):
            while(file_downloader()==True):
                sys_arg_cleaner()
        elif (choice == "4"):
            while(information_gatherer()==True):
                sys_arg_cleaner()
        elif (choice == "5"):
            sys.exit()
        print("")
        main()


if __name__ == '__main__':
    main()
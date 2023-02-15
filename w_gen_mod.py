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


def w_gen_mod():
    choice = 1000
    sys_arg_cleaner()
    while (choice != "1" and choice != "2" and choice != "3"):
        print("""Select from the menu:
            1) generate a wordlist from scratch
            2) generate a wordlist from an existing one
            3) go back""")
        print("\033[4mktool\033[0m" + "> ", end="")
        choice = input()
        if (choice == "1"):

            def w_gen():
                sys_arg_cleaner()
                gen_choice = 1000
                while (gen_choice != "exit"):
                    print("type 'exit' to go back.")
                    print("""-h or --help for help""")
                    print("\033[4mktool\033[0m" + "> ", end="")
                    arguments = input()
                    if (arguments == "exit"):
                        return
                    sys.argv += arguments.split()

                    def generate_wordlist(min_length, max_length, charset):
                        for length in range(min_length, max_length + 1):
                            for word in itertools.product(charset, repeat=length):
                                yield "".join(word)

                    try:
                        parser = argparse.ArgumentParser(description='Wordlist Generator', usage="-min MIN_LENGTH -max MAX_LENGTH [-c CHAR_SET] -o OUTPUT", exit_on_error=False)
                        parser.add_argument("-min", "--min_length", type=int, help="Minimum length of words to generate",required=True)
                        parser.add_argument("-max", "--max_length", type=int, help="Maximum length of words to generate",required=True)
                        parser.add_argument("-c", "--charset",help="Charset to use for generating words (default: abcdefghijklmnopqrstuvwxyz)",
                                            default="abcdefghijklmnopqrstuvwxyz")
                        parser.add_argument("-o", "--output", help="Output file name", required=True)
                        args = parser.parse_args()
                    except argparse.ArgumentTypeError as e:
                        print(e)
                        w_gen()
                        return
                    except argparse.ArgumentError as e:
                        print(e)
                        w_gen()
                        return
                    except:
                        time.sleep(0.1)
                        print("Le 3ad")
                        w_gen()
                        return
                    logging.basicConfig(filename='w_gen.log', level=logging.INFO)

                    if (args.min_length > args.max_length):
                        print("min_length can't exceed max_length")
                        w_gen()
                        return

                    if (args.max_length > 4):
                        print("MAX LENGTH CAN'T EXCEED 4, YOU DON'T WANNA RUN OUT OF STORAGE, THIS WILL BE FIXED SOON!")
                        w_gen()
                        return

                    with open(args.output, 'w') as f:
                        for word in generate_wordlist(args.min_length, args.max_length, args.charset):
                            f.write(word + '\n')
                    print("wordlist generated in " + args.output)

            w_gen()
        elif (choice == "2"):

            def w_mod():
                sys_arg_cleaner()
                while (True):
                    print("type 'exit' to go back.")
                    print("""-h or --help for help""")
                    print("\033[4mktool\033[0m" + "> ", end="")
                    arguments = input()
                    if (arguments == "exit"):
                        return

                    sys.argv += arguments.split()
                    try:
                        parser = argparse.ArgumentParser(description="Wordlist Modifier",
                                                         usage="-min MIN_LENGTH -max MAX_LENGTH [-c CHAR_SET] -w WORDLIST -o OUTPUT",exit_on_error=False)
                        parser.add_argument("-min", "--min_length", type=int,
                                            help="Minimum length of words that will be taken", required=True)
                        parser.add_argument("-max", "--max_length", type=int,
                                            help="Maximum length of words that will be taken", required=True)
                        parser.add_argument("-c", "--char_set",
                                            help="Charset for the words that will be taken (default: abcdefghijklmnopqrstuvwxyz)",
                                            default="abcdefghijklmnopqrstuvwxyz")
                        parser.add_argument("-w", "--wordlist", help="Input file name", required=True)
                        parser.add_argument("-o", "--output", help="Output file name", required=True)
                        args = parser.parse_args()
                    except argparse.ArgumentTypeError as e:
                        print(e)
                        w_mod()
                        return
                    except argparse.ArgumentError as e:
                        print(e)
                        w_mod()
                        return
                    except:
                        time.sleep(0.1)
                        w_mod()
                        return
                    logging.basicConfig(filename='w_gen.log', level=logging.INFO)

                    try:
                        with open(args.wordlist) as input_file:
                            words = input_file.read().splitlines()
                    except:
                        print("The specified wordlist file doesn't exist")
                        w_mod()
                        return

                    with open(args.output, 'w') as output_file:
                        for word in words:
                            w_len = len(word)
                            if (w_len >= args.min_length and w_len <= args.max_length):
                                output_file.write(word + "\n")
                    print("wordlist generated in " + args.output)

            w_mod()


        elif (choice == "3"):
            sys_arg_cleaner()
            return

    w_gen_mod()

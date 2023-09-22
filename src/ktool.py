from ssh_bruteforce import ssh_bruteforce
from w_gen_mod import w_gen, w_mod
from file_downloader import file_downloader
from information_gatherer import information_gatherer
from port_scanner import port_scanner
from utilities import *
import argparse


def main():

    welcome = "\n\nktool 1.3.5 Copyright (c) 2023 by Mohamed Karrab\n\n"
    # print(welcome, end="")

    parser = argparse.ArgumentParser(exit_on_error=False)
    subparsers = parser.add_subparsers(help='sub-command help')

    parser_down = subparsers.add_parser('down', help='file download help', usage="-u url [-o] outputFile")
    parser_down.add_argument("-u", "--url", help="Download URL", required=True)
    parser_down.add_argument("-o", "--output", help="Output file")
    parser_down.set_defaults(func=file_downloader)

    parser_wgen = subparsers.add_parser('wgen', description='Wordlist Generator',
                                        usage="-min MIN_LENGTH -max MAX_LENGTH [-c CHAR_SET] -o OUTPUT")
    parser_wgen.add_argument("-min", "--min_length", type=int, help="Minimum length of words to generate",
                             required=True)
    parser_wgen.add_argument("-max", "--max_length", type=int, help="Maximum length of words to generate",
                             required=True)
    parser_wgen.add_argument("-c", "--charset",
                             help="Charset to use for generating words (default: abcdefghijklmnopqrstuvwxyz)",
                             default="abcdefghijklmnopqrstuvwxyz")
    parser_wgen.add_argument("-o", "--output", help="Output file name", required=True)
    parser_wgen.set_defaults(func=w_gen)

    parser_wmod = subparsers.add_parser('word', description="Wordlist Modifier",
                                        usage="-min MIN_LENGTH -max MAX_LENGTH [-c CHAR_SET] -w WORDLIST -o OUTPUT")
    parser_wmod.add_argument("-min", "--min_length", type=int,
                             help="Minimum length of words that will be taken", required=True)
    parser_wmod.add_argument("-max", "--max_length", type=int,
                             help="Maximum length of words that will be taken", required=True)
    parser_wmod.add_argument("-c", "--char_set",
                             help="Charset for the words that will be taken (default: abcdefghijklmnopqrstuvwxyz)",
                             default="abcdefghijklmnopqrstuvwxyz")
    parser_wmod.add_argument("-w", "--wordlist", help="Input file name", required=True)
    parser_wmod.add_argument("-o", "--output", help="Output file name", required=True)
    parser_wmod.set_defaults(func=w_mod)

    parser_pscan = subparsers.add_parser('pscan', usage="-sp STARTING PORT -ep ENDING PORT -t Target IP")
    parser_pscan.add_argument("-sp", "--starting_port", help="Starting Port", type=int, required=True)
    parser_pscan.add_argument("-ep", "--ending_port", help="Ending Port", type=int, required=True)
    parser_pscan.add_argument("-t", "--target", help="Target IPv4 address", required=True)
    parser_pscan.set_defaults(func=port_scanner)

    parser_ssh = subparsers.add_parser('ssh', usage="-t TARGET -p PORT -u USERNAMES -w PASSWORDS [-T] THREADS")
    parser_ssh.add_argument("-t", "--target", help="Target IP address", required=True)
    parser_ssh.add_argument("-p", "--port", help="Target port", required=True)
    parser_ssh.add_argument("-u", "--usernames", help="Usernames file", required=True)
    parser_ssh.add_argument("-w", "--passwords", help="Passwords file", required=True)
    parser_ssh.add_argument("-T", "--threads", type=int, help="Number of threads", required=False)
    parser_ssh.set_defaults(func=ssh_bruteforce)

    parser_info = subparsers.add_parser('info', usage="-d domain")
    parser_info.add_argument("-d", "--domain", help="Domain name", required=True)
    parser_info.set_defaults(func=information_gatherer)

    args = parser.parse_args()
    try:
        args.func(args)
    except AttributeError:
        parser.error("too few arguments")

    main()


if __name__ == '__main__':
    main()

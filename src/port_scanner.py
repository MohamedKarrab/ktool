from utilities import *
import sys
import socket
import argparse
import time
import readline


def port_scanner():
    choice = 1000
    sys_arg_cleaner()
    while (choice != "0"):
        print("type '0' to go back.")
        print("""-h or --help for help""")
        print("\033[4mktool\033[0m" + "> ", end="")
        arguments = input()
        if (arguments == "0"):
            return False

        sys.argv += arguments.split()

        try:
            parser = argparse.ArgumentParser(exit_on_error=False, usage="-sp STARTING PORT -ep ENDING PORT -t Target IP")
            parser.add_argument("-sp","--starting_port", help="Starting Port",type=int, required=True)
            parser.add_argument("-ep","--ending_port", help="Ending Port",type=int, required=True)
            parser.add_argument("-t", "--target", help="Target IPv4 address", required=True)

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
            open_ports=[]
            socket.setdefaulttimeout(1)
            target = socket.gethostbyname(args.target)
            for port in range(args.starting_port, args.ending_port + 1):
                print(f"checking port {port}")
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((target,port))
                if(result == 0):
                    open_ports.append(port)
        except socket.gaierror as e:
            print(e)
            return True
        except socket.error as e:
            print(e)
            return True

        if(len(open_ports) == 0):
            print("No open ports found!")
        else:
            print("The open ports are:",)
            for port in open_ports:
                print(port)

    return True


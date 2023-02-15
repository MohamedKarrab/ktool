import os
import time
import argparse
from utilities import *
import urllib.request
import urllib.parse
def file_downloader():
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
            parser = argparse.ArgumentParser(exit_on_error=False, usage="-u url")
            parser.add_argument("-u", "--url", help="Download URL", required=True)
            args= parser.parse_args()
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
            url = args.url
            #file_name = url.split('/')[-1]
            file_name = os.path.basename(urllib.parse.urlsplit(url).path)
            urllib.request.urlretrieve(url, file_name)

        except Exception as e:
            print("An Error has occurred: ", e)

        print("File downloaded as", file_name)
        return True



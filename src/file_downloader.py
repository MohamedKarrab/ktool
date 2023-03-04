import os
import time
import argparse
from utilities import *
import urllib.request
import urllib.parse
import os
import readline
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
            parser = argparse.ArgumentParser(exit_on_error=False, usage="-u url [-o] outputFile")
            parser.add_argument("-u", "--url", help="Download URL", required=True)
            parser.add_argument("-o","--output",help="Output file")
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
            print("Downloading..")
            url = args.url
            file_name = os.path.abspath(os.path.basename(urllib.parse.urlsplit(url).path))
            if (args.output != None):
                args.output = os.path.abspath(args.output)
                file_name = args.output
            urllib.request.urlretrieve(url, file_name)

        except Exception as e:
            print("An Error has occurred: ", e)
            return True
        download_directory ="/".join(file_name.split('/')[:-1])
        actual_file_name = file_name.split('/')[-1]
        print("File downloaded in ",download_directory," as ", actual_file_name)
        return True



import requests
import re
from utilities import *
import argparse
import time
from googlesearch import search
# pip install googlesearch-python
import random
import readline


USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 OPR/45.0.2552.635",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
]

def information_gatherer():
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
            parser = argparse.ArgumentParser(exit_on_error=False, usage="-d domain")
            parser.add_argument("-d", "--domain", help="Domain name", required=True)
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

        domain = args.domain

        found_emails = set()
        try:
            urls = list(search(f"site:{domain}", num_results=5))
        except Exception as e:
            print(e)
            return True

        for url in urls:
            print(url)
            user_agent = random.choice(USER_AGENTS)
            try:
                response = requests.get(url, headers={'User-Agent': user_agent}, timeout=5)
                if response.status_code == 200:
                    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
                    emails = email_pattern.findall(response.text)
                    for email in emails:
                        found_emails.add(email)
            except (requests.exceptions.RequestException, requests.exceptions.Timeout, requests.exceptions.ConnectionError):
                pass
            time.sleep(0.2)

        if len(found_emails) > 0:
            found_emails = sorted(list(set(found_emails)))
            print(f"Found {len(found_emails)} email addresses:")
            for email in found_emails:
                print(email)
        else:
            print("No email addresses found.")

    return True

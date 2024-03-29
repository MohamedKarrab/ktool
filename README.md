# ktool
ktool 1.5.6 Copyright (c) 2023 by Mohamed Karrab

## Disclaimer: 
```
This tool is intended for ethical and legal usage only.
The authors and contributors of this tool do not condone or promote illegal or unauthorized access to any systems or networks.
They are not liable for any damages or losses that may result from its use either.
It is the user's responsibility to ensure that their use of this tool is in compliance with all relevant laws and regulations.
```

                  ██╗░░██╗████████╗░█████╗░░█████╗░██╗░░░░░
                  ██║░██╔╝╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
                  █████═╝░░░░██║░░░██║░░██║██║░░██║██║░░░░░
                  ██╔═██╗░░░░██║░░░██║░░██║██║░░██║██║░░░░░
                  ██║░╚██╗░░░██║░░░╚█████╔╝╚█████╔╝███████╗
                  ╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝

## available options
```
1) ssh bruteforce using username/password lists
2) wordlist generation/modification
3) file downloader
4) information gathering
5) port scanning
```
## usage
```
ktool [command] [options] 
            
commands:
            ktool down  - Downloads a file from a specified url
            ktool wgen  - Generates a wordlist
            ktool wmod  - Modifies a wordlist
            ktool pscan - Port scanning
            ktool info  - Gather information about a specified domain
            ktool ssh   - ssh bruteforce

Use "ktool [command] -h" for more information about a specific command.  
```
## Installation
### Linux
```
git clone https://github.com/MohamedKarrab/ktool
cd ktool
pip3 install -r requirements.txt 
sudo python3 ./setup.py
```

### to do:
```
Add more features

Add a better information gathering script

Add more search engines for the information gatherer

Expand the USER_AGENTS list

Add setup.py (done)

Work with TDD, BDD

Add colors

Seperate the files by function, better the banners (done)

Add arrows movement when taking input (done)

Fix the exception handling (done)

```

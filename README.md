# ktool
ktool 1.13 Copyright (c) 2023 by Mohamed Karrab

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
```

### to do:
```
Work with TDD, BDD

Add colors

Seperate the files by function, better the banners

Add arrows movement when taking input

Fix the exception handling

Add a command line option to specify the number of threads to use. This will allow you to control the number of parallel connections being made to the target, which can help avoid overloading the server or getting your IP address blocked.

Add a command line option to specify the time interval between connection attempts. This can be useful to avoid overwhelming the server with too many requests at once.

Add support for different types of authentication methods, such as key-based authentication or multi-factor authentication.

Add a command line option to specify a proxy server to use for the connections. This can be useful for anonymizing the connection and avoiding detection.

Add a function that will check if the server is still up and running before starting the brute force attack, this way you won't waste time and resources on a server that is down.

Add a function that will check if the server has a rate limit for login attempts. If it does and you exceed that limit the script will stop.

Add a verbose option, that will allow you to see more details about the login attempts, such as the time it took to check the login credentials.

Add a function that will save the successful login credentials in a file.

Add a function that will check if the server has a honeypot, and if it does, it will stop the attack.
```

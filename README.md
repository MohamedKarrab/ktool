# ktool
ktool 1.1 Copyright (c) 2023 by Mohamed Karrab
this is a tool for penetration testing, some options can be intrusive! Only use it when you have explicit permission from the targeted party! and use it for legal purposes only!



## available options:
ssh bruteforce using username/password lists.

## usage:
python3 ./ktool.py [-h] -t TARGET -p PORT -u USERNAMES -w PASSWORDS

### to do:
Add a command line option to specify the number of threads to use. This will allow you to control the number of parallel connections being made to the target, which can help avoid overloading the server or getting your IP address blocked.

Add a command line option to specify the time interval between connection attempts. This can be useful to avoid overwhelming the server with too many requests at once.

Add support for different types of authentication methods, such as key-based authentication or multi-factor authentication.

Add a command line option to specify a proxy server to use for the connections. This can be useful for anonymizing the connection and avoiding detection.

Add a function that will check if the server is still up and running before starting the brute force attack, this way you won't waste time and resources on a server that is down.

Add a function that will check if the server has a rate limit for login attempts. If it does and you exceed that limit the script will stop.

Add a verbose option, that will allow you to see more details about the login attempts, such as the time it took to check the login credentials.

Add a function that will save the successful login credentials in a file.

Add a function that will check if the server has a honeypot, and if it does, it will stop the attack.

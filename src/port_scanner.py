import socket

def port_scanner(args):
    try:
        open_ports = []
        socket.setdefaulttimeout(1)
        target = socket.gethostbyname(args.target)
        for port in range(args.starting_port, args.ending_port + 1):
            print(f"checking port {port}")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
    except socket.gaierror as e:
        print(e)
        return True
    except socket.error as e:
        print(e)
        return True

    if len(open_ports) == 0:
        print("No open ports found!")
    else:
        print("The open ports are:", )
        for port in open_ports:
            print(port)

    return True

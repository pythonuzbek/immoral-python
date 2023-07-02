import socket

from termcolor import colored, cprint  #noqa

internet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.68.145"


# port = 5432


def scanning_port(port):  # noqa
    if internet.connect_ex((host, port)):
        print(colored(f"{port} porti yopiq ekan", 'red'))
    else:
        print(f"{port} porti ochiq ekan")


ports = [5432, 80, 8000, 443, 32, 21, 22]
for i in ports:
    scanning_port(i)

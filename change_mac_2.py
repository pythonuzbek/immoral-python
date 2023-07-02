import subprocess


def change_mac(interface: str, new_mac: str):
    print(f"{interface} ----- {new_mac}ga o'zgaryapti")
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])


interface = input("Interface Nomini Kiriting : " )
new_mac = input("New Macni Kiriting : ")

change_mac(interface,new_mac)
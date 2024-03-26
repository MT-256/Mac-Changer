# Credits to s4vitar from hack4u.io
#!/usr/bin/env python3

import argparse
import re
import subprocess
from termcolor import colored

valid_interfaces = ["ens33", "enp0s17", "eth0", "enp0s3"] # If you have another interface, add it to this list

def get_arguments(): # Help panel

    parser = argparse.ArgumentParser(description="Tool to change MAC address")
    parser.add_argument("-i", "--interface", required=True, dest="interface", help="Network interface name")
    parser.add_argument("-m", "--mac", required=True, dest="mac_address", help="New MAC address for the network interface")
    return parser.parse_args()

def is_valid_input(interface, mac_address):

    is_valid_list = interface in valid_interfaces
    is_valid_mac = bool(re.match(r'^([A-Fa-f0-9]{2}[:]){5}[A-Fa-f0-9]{2}$', mac_address))
    return is_valid_mac and is_valid_list

def change_address(interface, mac_address):

    if is_valid_input(interface, mac_address):

        subprocess.run(["ifconfig", interface, "down"])     # Disable the interface
        subprocess.run(["ifconfig", interface, "hw", "ether", mac_address])     # Change MAC address
        subprocess.run(["ifconfig", interface, "up"])   # Activate the interface with the new MAC address
        print(colored(f"\n[+] MAC address has been changed successfully {interface}\n", 'green'))

    else:
        print(colored(f"\n[!] The data entered is incorrect\n", 'red'))

def main():

    args = get_arguments()
    change_address(args.interface, args.mac_address)

if __name__ == '__main__':
    main()

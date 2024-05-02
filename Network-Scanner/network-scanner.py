#!/usr/bin/env python

import scapy.all as scapy
import optparse
from colorama import init, Fore

# Initialize colorama
init()

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="ip", help="[-] Enter the Subnet range of the IP or IP Address\n"
                                                        "            [-] Usage: python3 network-scanner.py -t 192.168.0.0/24")
    (options, arguments) = parser.parse_args()
    if not options.ip:
        parser.error("[-] Please specify a target. Use --help for more info.")
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(results_list):
    print(Fore.GREEN + "[+] IP\t\t\tMAC Address\n-----------------------------------------")
    for client in results_list:
        print("[+]" +  client["ip"] + '\t\t' + client["mac"])

options = get_arguments()
scan_result = scan(options.ip)
print_result(scan_result)


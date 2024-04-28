#!/usr/bin/env python
import re
import subprocess
import optparse
def get_arguments():
    parser= optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",help="Interface to change its MAC address")

    parser.add_option("-m", "--mac", dest="new_mac",help="New  MAC address")

    (options,arguments) =  parser.parse_args()
    if not  options.interface:

        parser.error("[-] Please specify an interface, use --help for more info.")  
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return options




def change_mac(interface,new_mac):
    print(f"[+] changing MAC address for { interface}  to { new_mac}")
    subprocess.call(["ifconfig",interface, "down"])
    subprocess.call(["ifconfig",interface,"hw","ether", new_mac])
    subprocess.call(["ifconfig",interface,"up"])
    
    #print(f'[+] Succesfully changed mac address to { new_mac}' )
def get_current_mac(interface):    
    
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface]).decode()
    #print(ifconfig_result)

    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read Mac address. ")


options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current Mac = " + str(current_mac))

change_mac(options.interface,options.new_mac)

current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac:
    print("[+] Mac address was successfully changed to " + current_mac)
else:
    print("[-] Mac address did not get changed. " )









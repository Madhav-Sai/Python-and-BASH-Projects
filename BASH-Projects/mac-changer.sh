#!/bin/bash

echo "[+]MAC-CHANGER using BASH"

CURRENT_MAC=$(ifconfig)  # geting the network information

curr_mac=$(echo "$CURRENT_MAC" | grep -oE '([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}') # using regular expression to extrat the value of MAC ' -oE flag "o" is used to  only get the value and E is used to state that use regular expressions"


echo "[+]Current MAC Address: $curr_mac"  # printing the current mac

# using the while loop to get cmd arguments

while getopts "i:m:" opt; do
    case "${opt}" in
        i )
            interface=$OPTARG  # OPTARGS to get the options value from arguments
            ;;
        m )
            new_mac=$OPTARG
            ;;
        \? )
            echo "[-] Invalid Option: $OPTARG" 1>&2  # if invalid options are provid then redirecting the erros to standerror
            ;;
        : )
            echo "[-] Usage: ./mac-changer.sh -i <interface> -m <new_mac>"
            echo "[-] Example: ./mac-changer.sh -i eth0 -m xx:xx:xx:xx:xx:xx"
            exit 1
            ;;
    esac
done

# Check if both -i and -m options are provided
if [ -z "$interface" ] || [ -z "$new_mac" ]; then
    echo "[-] Both -i and -m options are required."
    echo "[-] Usage: ./mac-changer.sh -i <interface> -m <new_mac>"
    echo "[-] Example: ./mac-changer.sh -i eth0 -m xx:xx:xx:xx:xx:xx"
    exit 1
fi
# working principle 
sudo ifconfig $interface down
sudo ifconfig $interface hw ether $new_mac
sudo ifconfig $interface up

# Retrieve the new MAC address after changing it
new_mac=$(ifconfig $interface | grep -oE '([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}')
echo "[+] New MAC address: $new_mac"


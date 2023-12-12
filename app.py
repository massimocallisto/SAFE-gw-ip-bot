import socket
import requests
import json
from netifaces import interfaces, ifaddresses, AF_INET
import telepot
import time
import subprocess
import re

# Function to get local IP addresses
def get_local_ip_addresses():
    ip_list = []
    # Get a list of all interfaces
    interfaces = socket.if_nameindex()
    
    for interface in interfaces:
        # Fetch IP addresses associated with each interface
        ifname = interface[1]
        try:
            ips = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_IP, socket.AI_CANONNAME)
            for ip in ips:
                ip_addr = ip[4][0]
                if ip_addr not in ip_list:
                    ip_list.append(ip_addr)
        except:
            pass

    return ip_list

def get_interface_ip(interface):
    """Get IP address for a given network interface"""
    command = f"ip addr show {interface}"
    output = subprocess.check_output(command, shell=True).decode()
    ip_pattern = r'inet\s+(\d+\.\d+\.\d+\.\d+)'
    match = re.search(ip_pattern, output)
    
    if match:
        ip_address = match.group(1)
        return ip_address
    else:
        return None

def list_ip_addresses():
    ip_list = []
    interfaces = socket.if_nameindex()
    for interface in interfaces:
        ip_addr = get_interface_ip(interface[1])
        if ip_addr is not None:
            ip_list.append(interface[1] + ":" + ip_addr)
        else:
            print(interface[1]  + " has no ip address...")
    return ip_list

def build_message(ip_list):
    if ip_list:
        message = "Local IP Addresses:\n" + "\n".join(ip_list)
    else:
        message = "No IP addresses found"
    return message

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('chat id: ' + str(chat_id))
    print('command: ' +  command)

    # Send IP addresses to Telegram bot
    if command == '/getIP':
        ip_list = list_ip_addresses() #get_local_ip_addresses()
        bot.sendMessage(chat_id, build_message(ip_list))
        
if __name__ == "__main__":
    bot = telepot.Bot('TOKEN')

    bot.message_loop(handle)
    print('I am listening...')

    while 1:
	    time.sleep(10)



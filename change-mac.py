#!usr/bin/env python3
import subprocess
import re
from colorama import init, Fore, Back
#we will use subprocess to run system commands.so if not install install it.
#we use colorama for colour if not installed u can do it by running pip3 install colorama.

init(autoreset=True)
def change_mac(interface,new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def check_interface(interface , final_interface):


    if interface not in final_interface:
        print(Fore.RED + Back.WHITE + "[-] Hey! you do not have",Fore.RED + Back.WHITE + interface,Fore.RED + Back.WHITE + "in your machine.Choose the correct interface \n")
        return 0
    if not interface:
        #print(interface)
        print(Fore.YELLOW + "[!]", Fore.RED + "NO interface provided. Please provide correct interface")
        return 0
    return interface

def get_mac():
    new_mac = input(f"enter the new mac address to change for {interface} interface eg(00:11:22:33:44:55)>> ")
    if not new_mac:
        print(Fore.YELLOW + "[!]", "you did not provide a mac address so setting to default",  Fore.RED + "(00:11:22:33:44:55)", "\n")
        new_mac = "00:11:22:33:44:55"
        #print(new_mac)
    return new_mac

def verify(interface,new_mac):
    ifconf_inter=subprocess.check_output(["ifconfig", interface])
    mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconf_inter))
    if mac.group(0)==new_mac:
        print(Fore.GREEN + "[+] GREAT YOUR MAC ADDRESS HAS BEEN CHANGED TO ", Fore.RED + Back.WHITE + new_mac)
        print("YOUR NEW MAC ADDRESS IS ", Fore.RED + Back.WHITE + new_mac)
    else:
        print(Fore.RED + "[-] COULD NOT CHANGE THE MAC ADDRESS ")

def decorate():
    final_interface = []
    print(Fore.GREEN + "The available Interfaces for this device are:\n")
    search_interface = subprocess.check_output(["ifconfig"])
    available_interface = re.search(r"\w{3,7}:\s", str(search_interface))
    available_interface2 = re.findall(r"[n]\w{3,7}:\s", str(search_interface))
    for elements in available_interface2:
        final_interface.append(elements[1:-2])
    final_interface.append(available_interface.group(0)[:-2])
    for ele in final_interface:
        print(Fore.BLACK + Back.CYAN + ele, end="\t\t\t")
    print("\n")
    return final_interface

def requirements():
    li = ""
    li2 = ""
    subprocess.call("touch touch.txt", shell=True)
    subprocess.call("cat /etc/NetworkManager/NetworkManager.conf >> touch.txt", shell=True)

    with open("touch.txt", "r") as touch1:
        for items in touch1:
            li = li + items
    with open("touch5.txt", "r") as touch2:
        for items in touch2:
            li2 = li2 + items

    if li.find(li2) == -1:
        print(Fore.GREEN + Back.WHITE + "Writing to NetworkManager config file.")
        subprocess.call("cat touch5.txt >> /etc/NetworkManager/NetworkManager.conf", shell=True)

    else:
        print(Fore.GREEN + Back.WHITE + "[+] REQUIREMENTS ALREADY SATISFIED")
    subprocess.call("rm touch.txt", shell=True)

requirements()
print("Enter the interface for which you want to change the mac","\n eg", Fore.YELLOW + "(eth0 , wlan0 , wlan1)", Fore.RED + ">>  ")
final_interface=decorate()
interface = str(input())
interface1=check_interface(interface , final_interface)
while (interface1==0):
    print("Enter the interface for which you want to change the mac", "\n eg", Fore.YELLOW + "(eth0 , wlan0 , wlan1)",Fore.RED + ">>  ")
    final_interface = decorate()
    interface = str(input())
    interface1 = check_interface(interface,final_interface)
new_mac=get_mac()
change_mac(interface1,new_mac)
verify(interface1,new_mac)
















'''
#Created by MvT - 30-10-2023
# MacSpoofing with Python..
#
# - Randomize a mac adress and uppercase it
# - bring interface down, randomize Mac adress and bring adapter back up
'''

#Import libs
import subprocess
import random
import string
import re


def randomize_MACAdress():
    #Generate and return a mac adress
    #get hex digits uppercase
    uppercase_HexDigits = ''.join(set(string.hexdigits.upper()))
    #2nd digit must be a 0,2,4,6,7,A,C or E
    GenMac = ""
    for i in range(6):
        for j in range(2):
            if i == 0:
                GenMac += random.choice("02468ACE")
            else:
                GenMac += random.choice(uppercase_HexDigits)
        GenMac += ":"
    return GenMac.strip(":")



if __name__ == "__main__":
    new_MAC = randomize_MACAdress()


    interface = "eth0"
    
    
    print(f"BringS DOWN the interface: {interface}")
    subprocess.run(["sudo", "ifconfig", "eth0", "down"])
    
    print(f"Changing the interface MAC adress of {interface}, to {new_MAC}")
    subprocess.run(["sudo", "ifconfig", "eth0", "hw", "ether", new_MAC])
    
    print(f"MAC Adress has been changed to:{new_MAC}, bring Networking back up . . .")
    subprocess.run(["sudo", "ifconfig", "eth0", "up"])
    
    print(f"network interface back UP")
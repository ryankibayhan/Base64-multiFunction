import pybase64
import time
import os
import sys
import codecs
from base64 import b64decode
import pyfiglet

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

ascii_banner = pyfiglet.figlet_format("Welcome to \n Base64 ")
ascii_banner2 = pyfiglet.figlet_format("Encode/Decode")
ascii_banner3 = pyfiglet.figlet_format("By  RYB")
print(bcolors.GREEN + ascii_banner)
print(bcolors.GREEN + ascii_banner2)
print(bcolors.GREEN + ascii_banner3)



option = input("Are you want to encode or decode your wished string? 1/Encode,2/Decode : ")

print(option)

if (option == "1"):

    s = input("Enter your string characters : \n")
    print("Encoding magick started!!!...")
    time.sleep(2)
    encode = pybase64.b64encode(s.encode())
    print("Your encoded string is.... : ",encode)
    sys.exit()

elif (option == "2"):

    encoded_s = input("Enter your base64 code : \n  ")
    print("Decoding magick started!!!...")
    time.sleep(2)
    decodedBytes = b64decode(encoded_s)
    decodedStr = str(decodedBytes,"utf-8")

    print("Your decoded base64 code is.... : ",decodedStr)

    
    sys.exit()

else:
    print("You have entered wrong operation,program will be aborted,try again!" )
    sys.exit()




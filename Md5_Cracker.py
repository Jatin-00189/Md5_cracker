import os
import hashlib
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Crack The hash \n Written By Sanjay Jangra \n :)")
print(ascii_banner)


wordlist = input("Enter you file location : ")

if not os.path.isfile(wordlist):
    print("File Not Found")

hash = input("Enter hash to crack : ")

with open(wordlist,'rb') as file:

    for password in file.readlines():

        try:
            password = password.decode('utf-8')

        except UnicodeDecodeError:
            continue

        password = password.strip()

        hash_object = hashlib.md5(password.encode())

        hash_to_compare = hash_object.hexdigest()

        if hash == hash_to_compare:
            print("Valid password found : {} \n \n Enjoy :)".format(password))
            exit(0)

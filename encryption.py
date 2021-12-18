#Simple Caesar cipher program capable of encrypting/decrypting text (there is a ~250 word limit), as well as outputting a .txt file containing letter frequency.
#This was used to analyse the frequency of letters in any given text for a project.
import sys
import os
import time
import collections
import string
import re
key_size = 26

# Allows the user the decide whether to encrypt or decrypt their message
def getMode():
    while True:
        print("Would you like to Encrypt or decrypt?")
        mode = input().lower()
        if mode in "encrypt e decrypt d".split():
            return mode
        else: #The user will be asked to input the correct command
            print("Invalid input. Enter either 'Encrypt', 'e' or 'Decrypt', 'd'.")
            os.system('cls')

def getMessage():
    print("Enter your message: ")
    return input()

def getKey():
    key = 0
    while True: 
        print('Enter the key number (1-%s)' % (key_size))
        key = int(input())
        if (key >= 1 and key <= 26):
            return key
        
def translatedMessage(mode,message,key):
    if mode[0] == 'decrypt' or 'd':
        key = -key
    translated = ''
    
    for symbol in message:
         if symbol.isalpha():
             num = ord(symbol)
             num += key

#Checks whether characters are upper case or lower case
             if symbol.isupper():
                 if num > ord('Z'):
                     num -= 26
                 elif num < ord('A'):
                     num += 26
             elif symbol.islower():
                 if num > ord('z'):
                     num -= 26
                 elif num < ord('a'):
                     num += 26

             translated += chr(num)
         else:
            translated += symbol
    return translated

mode = getMode()
message = getMessage()
key = getKey()

print('Here is your translated text: ')
print(translatedMessage(mode, message, key))# Displays the user's text in translated form

dencrypt = str(translatedMessage(mode,message,key)) #Converting the text into string format
translateText = re.sub(r"\s+","",dencrypt, flags=re.UNICODE)
for p in string.punctuation:
    translateText = translateText.replace(p,"")
#Counter is used to count the frequency of letters in the translated text
from collections import Counter
freq = str(Counter(translateText.lower()).most_common())

letterFreq = freq
# Write file for output, 'w' is write 'a' is append 'r' is read
t,s = str(time.time()).split('.') #writes a new file based on time of access
tl = t+".txt"
with open(tl, 'w') as new_file:
    new_file.write("Here is your translated text: \n")
    new_file.write(dencrypt)
    new_file.write("\nLetter frequency: \n")
    new_file.write(letterFreq)

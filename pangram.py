# Importing Libraries
import string

def pan(str):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in alpha:
        if i not in str.lower():
            return False
    return True
    
x = str(input("Enter your sentence."))

if pan(x) == True:
    print("This sentence is a pangram.")
if pan(x) == False:
    print("This sentence isn't a pangram.")

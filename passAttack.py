import os 
from random import randint 

pas = input("set the password: ")

keys = ["a","@",
        "b","c","d","e","f","g","h","i","j","k","l",
        "m","n","o","p","q","r","s","t","u","v","w",
        "x","y","z"]

pwg = ""
while(pwg != pas):
    pwg = ""
    for i in range(len(pas)):
        guesspass = keys[randint(0,4)]
        pwg = str(guesspass)+str(pwg)
        print(pwg)
        print("attacking...please wait!!!")
        os.system("cls")

print(f"The pass is: {pwg}")
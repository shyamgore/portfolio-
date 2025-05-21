
import colorama
import time
import msvcrt
import os
colorama.init(autoreset=True)
        
def check(j):
    
    while True:    
        
        if j:
            break
        else:
           continue



data = "the quick brown fox jumps over thirteen lazy dogs while Jack quietly writes numbers from one to nine and then zero as he practices his daily keyboard lessons."
print("Type highlited part:")
for i in range(len(data)):
    for j in range(len(data)):
        if i == j:
            print(colorama.Back.CYAN + data[j] + colorama.Back.RESET, end="")
        else:
            print(data[j], end="")
    print(end="\r")  
    time.sleep(0.2) 
    print("")
    key=msvcrt.getch().decode()
    os.system("cls")
    if data[i]==key:
        continue
    else:
        while True:
            red=colorama.Back.RED+data[i]+colorama.Back.RESET
            print("Eorror! type",red)
            updated_key=msvcrt.getch().decode()
            if data[i]==updated_key:
                break
            else:
                os.system("cls")
                continue
os.system("cls")
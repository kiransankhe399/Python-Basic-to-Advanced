#Check number is divisible by 5 using comand line 
import sys

def Divisible(No):
    if No % 5 == 0:
        print("True")
    else:
        print("False")   

No = int(sys.argv[1])
Divisible(No)
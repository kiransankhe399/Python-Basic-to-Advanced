#Check positive negative using comand line 
import sys

def Display(No):
    if No > 0:
        print("Number is Positive")
    elif No < 0:
        print("Number is Negative")
    else:
        print("Number is Zero")
     

No = int(sys.argv[1])
Display(No)
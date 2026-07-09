#Display Marvelleous using comand line 
import sys

def Display(No):
    for i in range(No):
        print("Marvellous")

No = int(sys.argv[1])
Display(No)
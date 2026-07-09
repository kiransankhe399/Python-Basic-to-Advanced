#Display Numbers reverse using comand line 
import sys

def Number(No):
    for i in range(No,0,-1):
       print(i)

No = int(sys.argv[1])
Number(No)
#Check Addition using comand line 
import sys

def Add(No1, No2):
    Ans = No1 + No2
    print(Ans)

No1 = int(sys.argv[1])
No2 = int(sys.argv[2])
Add(No1, No2)

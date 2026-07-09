#Check num even or odd using comand line 
import sys
def CheckNum(No):
    if No%2 == 0:
     print("Even")    
    else:
     print("Odd")
    

No1 = int(sys.argv[1])
CheckNum(No1)

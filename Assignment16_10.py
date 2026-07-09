#Print pattern * using comand line 
import sys

def Pattern(No):
    print("*  "*No)

No = int(sys.argv[1])
Pattern(No)
#Program to distplay first 10 even num using comand line 
import sys

def Number(No):
      for i in range(2,No+1,2):
       print(i)

No = int(sys.argv[1])
Number(No)
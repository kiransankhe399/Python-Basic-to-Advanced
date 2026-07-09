#Program to distplay length of string using comand line 
import sys

def Length(xn):
      Res =  len(xn)
      print(Res)

Value = sys.argv[1]
Length(Value)
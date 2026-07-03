#Multiplication table

def Multiplication(No):
    Table = list()
    for i in range(1,11):
      Ret = No * i
      Table.append(Ret)
    return Table
    
def main():
   Value = int(input("Enter a number:"))
   multi = Multiplication(Value)
   print("Multiplication is :", multi)
    

if __name__ == "__main__":
    main()
#Factorial of number

def Factorial(No):
    if No == 0 or No == 1:
       return 1
    else:
       return No * Factorial(No - 1)

    
def main():
   Value = int(input("Enter a number:"))
   Res = Factorial(Value)
   print("Factorial is :", Res)
    

if __name__ == "__main__":
    main()


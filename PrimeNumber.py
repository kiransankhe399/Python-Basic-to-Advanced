#Prime Number

def PrimeNum(No):
    if No<= 1:
        return False   
    for i in range(2, No):
       if No%i == 0:
          return False 
    return True   
    
def main():
    Value = int(input("Enter a Number : "))
    Res = PrimeNum(Value)
    if Res:
       print("Number is prime")
    else:
       print("Number is Not prime") 
    
if __name__ == "__main__":
    main()
#Divisible of one input number

def Divisible(No):
  if No%5 == 0 and No%3 == 0:
    return True
  else:
    return False

def main():
    Value = int(input("Enter a number :"))
    Res = Divisible(Value)
    if Res:
        print("Number is divisible")
    else:
        print("Number is Not divisible")

if __name__ == "__main__":
    main()
#Natural number

def Natural(No):
    Sum = 0
    for i in range(1,No+1):
      Sum = Sum + i
    return Sum
    
def main():
   Value = int(input("Enter a number:"))
   Res = Natural(Value)
   print("Natural number is :", Res)
    

if __name__ == "__main__":
    main()
#Cube of one input number

def Cube(No):
  return No*No*No

def main():
    Value = int(input("Enter a number :"))
    Res = Cube(Value)
    print("Cube of a number is:", Res)

if __name__ == "__main__":
    main()
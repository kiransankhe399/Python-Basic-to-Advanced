#Square of one input number

def Square(No):
  return No*No

def main():
    Value = int(input("Enter a number :"))
    Res = Square(Value)
    print("Square of a number is:", Res)

if __name__ == "__main__":
    main()
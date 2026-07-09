#program to print pattern 

def Pattern(No):
    for i in range(No):
      print("* "*5)

def main():
    Value = int(input("Enter a Number: "))
    Pattern(Value)

if __name__ == "__main__":
    main()
#program to print patter
def Pattern(No):
    for i in range(No,0,-1):
       print("*" * i)

def main():
    Value = int(input("Enter a number : "))
    Pattern(Value)

if __name__ == "__main__":
    main()
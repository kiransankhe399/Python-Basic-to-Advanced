#reverse num

def RevNum(No):
    rev = 0
    while No > 0:
        digit = No % 10
        rev = rev * 10 + digit
        No //= 10

    return rev
    
def main():
    Value = int(input("Enter a Number : "))
    Res = RevNum(Value)
    print(Res) 
    
if __name__ == "__main__":
    main()
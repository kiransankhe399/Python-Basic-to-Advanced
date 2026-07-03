#Sum of digits

def SumDigit(No):
    total = sum(int(digit) for digit in str((No)))
    return total

def main():
    Value = int(input("Enter a Number : "))
    Res = SumDigit(Value)
    print(Res) 
    
if __name__ == "__main__":
    main()
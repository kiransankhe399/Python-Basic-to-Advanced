#Palindrom Number

def Palindrom(No):
    Num = No
    rev = 0
    while No > 0:
        digit = No % 10
        rev = rev * 10 + digit
        No //= 10
    if rev == Num:
        return True
    
def main():
    Value = int(input("Enter a Number : "))
    Res = Palindrom(Value)
    if Res:
       print("Number is Palindrom")
    else:
       print("Number is Not Palindrom") 
    
if __name__ == "__main__":
    main()
#Count Number

def CountNum(No):
    return len(str(No))   
    
def main():
    Value = int(input("Enter a Number : "))
    Res = CountNum(Value)
    print(Res) 
    
if __name__ == "__main__":
    main()
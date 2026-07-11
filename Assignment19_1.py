#Function accepts one number and return power of two numbers using lambda

Power = lambda No : No**2
# def Power(No):
#     Sum = 1
#     for i in range(No):
#         Sum = Sum*2
#     return Sum

def main():
    Value = int(input("Enter a number :"))
    Ret = Power(Value)
    print(f"{Value} Power of 2 is :", Ret)

if __name__ == "__main__":
    main()

#Odd Thread Lib

def Odd(No):
    print("\nExecuting:", "Odd Thread")

    count = 0
    num = No

    while count < 10:
        if num % 2 != 0:
            print("Odd:", num)
            count += 1
        num += 1
#Even Thread Lib

def Even(No):
    print("\nExecuting:", "Even Thread")

    count = 0
    num = No

    while count < 10:
        if num % 2 == 0:
            print("Even:", num)
            count += 1
        num += 1
#Calculate Count Odd number in list using pool map()
import multiprocessing
import os
import time
import math

def Multiple(No):
    return math.factorial(No)


def main():
    IList = []
    Length = int(input("Enter length of a list : "))

    for i in range(Length):
        No = int(input("Enter a Element : "))
        IList.append(No)
        
    pObj = multiprocessing.Pool()
    Res = pObj.map(CountOdd,IList)
    pObj.close()
    pObj.join()

    print("List of input is :", IList)
    print("PID is :", os.getpid())
    print("Factorial is :", Res)


if __name__ == "__main__":
    main()

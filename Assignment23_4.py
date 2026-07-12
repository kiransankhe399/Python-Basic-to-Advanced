#Calculate Count Odd number in list using pool map()
import multiprocessing
import os

def CountOdd(IList):
    Count = 0
    Sum = 0

    for i in range(1, IList + 1):
        for j in range(1,i+1):
          if i%2 != 0:
            Sum = True
            break

        if Sum:
            Count += 1

    return Count

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
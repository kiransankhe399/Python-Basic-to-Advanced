#Calculate Count Even number in list using pool map()
import multiprocessing
import os

def CountEven(IList):
    return (IList + 1) // 2

def main():
    IList = []
    Length = int(input("Enter length of a list : "))

    for i in range(Length):
        No = int(input("Enter a Element : "))
        IList.append(No)
        
    pObj = multiprocessing.Pool()
    Res = pObj.map(CountEven,IList)
    pObj.close()
    pObj.join()

    print("List of input is :", IList)
    print("PID is :", os.getpid())
    print("CountEven is :", Res)


if __name__ == "__main__":
    main()

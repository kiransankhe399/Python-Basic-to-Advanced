#Calculatesum of Sum of Even of list using pool map()
import multiprocessing
import os

def SumEven(Num):
    n = Num // 2  
    return n * (n + 1)

def main():
    IList = []
    Length = int(input("Enter length of a list : "))

    for i in range(Length):
        No = int(input("Enter a Element : "))
        IList.append(No)
        
    pObj = multiprocessing.Pool()
    Res = pObj.map(SumEven,IList)

    pObj.close()
    pObj.join()

    print("ProcessId is :", os.getpid())
    print("Sum of EvenNumber of a List is :", Res)

if __name__ == "__main__":
    main()

#Calculatesum of Sum of square of list using pool map()
import multiprocessing

def Sum(Num):
    total = 0
    for i in range(1, Num + 1):
        total += i * i
    return total

def main():
    IList = []
    Length = int(input("Enter length of a list : "))

    for i in range(Length):
        No = int(input("Enter a Element : "))
        IList.append(No)
        
    pObj = multiprocessing.Pool()
    Res = pObj.map(Sum,IList)

    pObj.close()
    pObj.join()

    print("Sum of Square of a List is :", Res)

if __name__ == "__main__":
    main()
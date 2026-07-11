#Function accepts List using FMR
def CheckFilter(No):
    if No%2 == 0:
        return True
    return False


def IncreaseNum(No):
    return No*2


def Product(x, y):
    return x + y


def Filter(Task, Elements):
    Result = []
    for no in Elements:
        if Task(no):
            Result.append(no)
    return Result


def Map(Task, Elements):
    Result = []
    for no in Elements:
        Result.append(Task(no))
    return Result


def Reduce(Task, Elements):
    Result = 1
    for no in Elements:
        Result = Task(Result, no)
    return Result


def main():
    List = []
    VList = int(input("Enter number of length of list: "))
    for i in range(VList):
        no = int(input("Enter numbers: "))
        List.append(no)
    FData = Filter(CheckFilter, List)
    MData = Map(IncreaseNum, FData)
    RData = Reduce(Product, MData)

    print("Input list is:", List)
    print("List after Filter is:", FData)
    print("List after Map is:", MData)
    print("List after Reduce is:", RData)


if __name__ == "__main__":
    main()
    
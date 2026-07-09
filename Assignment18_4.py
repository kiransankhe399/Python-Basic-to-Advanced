def Frequency(Data, Value):
    Count = 0

    for no in Data:
        if no == Value:
            Count = Count + 1

    return Count


def main():
    List = []

    N = int(input("Enter number of elements: "))

    for i in range(N):
        no = int(input("Enter number: "))
        List.append(no)

    Search = int(input("Enter element to search: "))

    Ret = Frequency(List, Search)

    print("Frequency is:", Ret)


if __name__ == "__main__":
    main()
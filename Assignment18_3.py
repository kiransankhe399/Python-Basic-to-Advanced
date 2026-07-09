def Minimum(Data):
    Min = Data[0]

    for no in Data:
        if no < Min:
            Min = no

    return Min


def main():
    List = []

    N = int(input("Enter number of elements: "))

    for i in range(N):
        no = int(input("Enter number: "))
        List.append(no)

    Ret = Minimum(List)

    print("Minimum number is:", Ret)


if __name__ == "__main__":
    main()
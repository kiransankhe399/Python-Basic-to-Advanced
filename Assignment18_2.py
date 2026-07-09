def Maximum(Data):
    Max = Data[0]

    for no in Data:
        if no > Max:
            Max = no

    return Max


def main():
    List = []

    N = int(input("Enter number of elements: "))

    for i in range(N):
        no = int(input("Enter number: "))
        List.append(no)

    Ret = Maximum(List)

    print("Maximum number is:", Ret)


if __name__ == "__main__":
    main()
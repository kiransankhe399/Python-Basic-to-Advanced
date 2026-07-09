def ChkPrime(no):
    if no <= 1:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True


def ListPrime(Data):
    Sum = 0

    for no in Data:
        if ChkPrime(no):
            Sum = Sum + no

    return Sum


def main():
    List = []

    N = int(input("Enter number of elements: "))

    for i in range(N):
        no = int(input("Enter number: "))
        List.append(no)

    Ret = ListPrime(List)

    print("Addition of prime numbers is:", Ret)


if __name__ == "__main__":
    main()
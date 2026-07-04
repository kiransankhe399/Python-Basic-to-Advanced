#Factor

def Factor(No):
    factors = []

    for i in range(1, No + 1):
        if No % i == 0:
            factors.append(i)

    return factors


def main():
    Value = int(input("Enter a Num : "))
    Res = Factor(Value)
    print(Res)

if __name__ == "__main__":
    main()
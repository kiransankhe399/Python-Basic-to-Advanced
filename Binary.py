def to_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary


def main():
    n = int(input("Enter a number: "))
    print("Binary equivalent:", to_binary(n))


if __name__ == "__main__":
    main()
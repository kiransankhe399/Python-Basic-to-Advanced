#Perfect Number

def Perfect(n):
    if n <= 1:
        return False

    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n

def main():
    No = int(input("Enter a number : "))
    if Perfect(No):
        print(No, "is a Perfect Number")
    else:
        print(No, "is NOT a Perfect Number")

if __name__ == "__main__":
    main()
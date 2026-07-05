# Square of number using lambda

Cube = lambda No : No * No *No

def main():
    Value = int(input("Enter a number:"))
    Ret = Cube(Value)
    print(f"Cube of {Value} is : {Ret}")

if __name__ == "__main__":
    main()

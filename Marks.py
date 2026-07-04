grade = lambda m: (
    "Distinction" if m >= 75 else
    "First Class" if m >= 60 else
    "Second Class" if m >= 50 else
    "Fail"
)

def main():
    marks = int(input("Enter marks: "))
    print(grade(marks))


if __name__ == "__main__":
    main()
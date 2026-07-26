
def CountLine(FileName):
    try: 
        with open(FileName, "r") as fobj:
          count = sum(1 for line in fobj)
        return count
    except Exception as eobj:
        print("Exception is :", eobj)

def main():
    FileName = input("Enter a file name : ")
    Ret = CountLine(FileName)
    print("Total number of line is :", Ret)


if __name__ == "__main__":
    main()
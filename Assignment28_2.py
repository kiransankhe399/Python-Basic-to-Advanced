
def CountLine(FileName):
    count = 0
    try: 
        with open (FileName, "r") as fobj:
            for line in fobj:
                words = line.split()
                count = len(words)
          
    except Exception as eobj:
        print("Exception is :", eobj)
    return count

def main():
    FileName = input("Enter a file name : ")
    Ret = CountLine(FileName)
    print("Total number of words is :", Ret)


if __name__ == "__main__":
    main()

def CountLine(FileName):
    Ret = []
    try: 
        with open (FileName, "r") as fobj:
            for line in fobj:
              Ret.append(line)
        
    except Exception as eobj:
        print("Exception is :", eobj)

    return Ret
 
def main():
    FileName = input("Enter a file name : ")
    Ret = CountLine(FileName)
    for r in Ret:
        print(r)


if __name__ == "__main__":
    main()

def ReadFile(FileName):
    try: 
        with open (FileName, "r") as fobj:
            return fobj.read()
                  
    except Exception as eobj:
        print("Exception is :", eobj)
    


def main():
    FileName = input("Enter a file name : ")
    Ret = ReadFile(FileName)
    print(Ret)


if __name__ == "__main__":
    main()
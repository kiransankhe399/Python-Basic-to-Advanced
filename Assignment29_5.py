import sys

def Compare(FileName,SearchStr):
    occurance = 0
    try: 
        with open (FileName, "r") as fobj:
            for line in fobj:
              occurance += line.count(SearchStr)
                         
    except Exception as eobj:
        print("Exception is :", eobj)

    return occurance

def main():
    FileName = input("Enter a file name : ")
    StrData = input("Enter a name : ")

    occurence = Compare(FileName,StrData )
    print(f"{StrData} occurance in File Data {FileName} is {occurence}")



if __name__ == "__main__":
    main()
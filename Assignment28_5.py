
def FindWord(FileName,Word):
    existingD = []
    try: 
        with open (FileName, "r") as fobj:
            for line in fobj:
              existingD.append(line)
            if Word in line:
                return True
            else:
                return False  
            
    except Exception as eobj:
        print("Exception is :", eobj)

    return (existingD,True)

def main():
    FileName = input("Enter a Existing File name : ")
    Word = input("Enter a word in File name : ")

    FileData = FindWord(FileName,Word)
    if FileData == True:
        print(f"In File Name : {FileName} word : {Word} exist")
    else:
        print(f"In File Name : {FileName} word : {Word} does not exist")




if __name__ == "__main__":
    main()
import sys

def GetData(FileName):
    existingD = []
    try: 
        with open (FileName, "r") as fobj:
            for line in fobj:
              existingD.append(line)
        
    except Exception as eobj:
        print("Exception is :", eobj)

    return existingD

def CopyData(FileName,existingData):
    newD =[]
    try:
        with open(FileName, "w") as fobj:
          for w in existingData:
            fobj.write(w)

        with open (FileName, "r") as fobj:
            for line in fobj:
              newD.append(line)
              
    except Exception as eobj:
        print("Exception is :", eobj)

    return newD
    

def main():
    ExistingFile = sys.argv[1]

    OldData = GetData(ExistingFile)
    NewData = CopyData("NewFile.txt",OldData)
    print(f"Existing file Name is : {ExistingFile} and Data is : {OldData}")
    print(f"New file Name is : NewFile.txt and Data is : {NewData}")



if __name__ == "__main__":
    main()
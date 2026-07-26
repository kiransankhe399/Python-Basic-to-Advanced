
import os

def CheckDirectory(DirName):
    return  os.path.exists(DirName)

         
def main():
    DirName = input("Enter a DirectoryName :")
    if CheckDirectory(DirName):
        print(f"Directory Name {DirName} present")
    else:
        print(f"Directory Name {DirName} is not present")


if __name__ == "__main__":
    main()



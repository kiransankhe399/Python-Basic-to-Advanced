#PRoject : disk sanitizer
# Find files from directory and store in Dictionary and filter duplicate files from dictionary amd delete
import sys
import os   # lib for walk
import hashlib # lib for md5

def CalculateChecksum(FileName):
   fobj = open(FileName,"rb")  # rb- read in binary / r - read in text
   hobj = hashlib.md5() 
   Buffer = fobj.read(1024) # read first 1000 byte 

   #Check file byte till zero
   while(len(Buffer)> 0):
      hobj.update(Buffer)
      Buffer = fobj.read(1024)  # read next 1000 byte 

   fobj.close()
   return hobj.hexdigest()  #

def FindDuplicate(DirectoryName):
    Duplicate = {}

    Ret = False
    Ret = os.path.exists(DirectoryName) #Check if directory present
    if Ret == False :          
        print("Path is invalid")
        return  
      
    Ret = os.path.isdir(DirectoryName)     # check if it is a directory
    if Ret == False:
        print("It is not a directory")
      
    for FolderName,SubFolder,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            Checksum = CalculateChecksum(fname)
              
        #    print(f"{fname} : {Checksum}")      

            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]
     
    return Duplicate
 
def DeleteDuplicate(DirectoryName):
    MyDict = FindDuplicate(DirectoryName)
    #Result = MyDict.values()

    Result = list(filter(lambda x : len(x) > 1,MyDict.values()))

    Count = 0
    TotalDeleted= 0
    for value in Result:
        for subValue in value:
            Count = Count + 1
            if(Count > 1):
                os.remove(subValue)
                print("Duplicate found", subValue)
                TotalDeleted = TotalDeleted + 1
        
        Count = 0
    print("Total Deleted files :", TotalDeleted)


def main():
  Data = DeleteDuplicate("Test") #Directory name

if __name__ == "__main__":
    main()


#add logger
#add sheduler
#add exception handling
#add --h, --u 
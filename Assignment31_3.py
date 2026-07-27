import schedule
import time
import os
import datetime

def DirectoryScan(dirName):
    countFiles = 0
    CountSub = 0
    if not os.path.exists(dirName):
        print("Directory does not exist")
        return
    
    for root, dirs, files in os.walk(dirName):
        CountSub += len(dirs)
        countFiles += len(files)

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("Total number of files in directory: ", countFiles)
    print("Total number of sub-directories in directory: ", CountSub)
    print("Scan completed at: ", current_time)        
          
    return
    
    
def main():
        DirName = input("Enter a Directory name: ")
        schedule.every(5).seconds.do(DirectoryScan,DirName)
        while True:
            schedule.run_pending()
            time.sleep(1)
            


if __name__ == "__main__":
    main()
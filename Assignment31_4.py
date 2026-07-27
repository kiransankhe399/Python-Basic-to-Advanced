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
    
    
    with open("MarvelleousLog.txt", "w") as files:
        files.write("Total number of files in directory: " + str(countFiles) + "\n")
        files.write("Total number of sub-directories in directory: " + str(CountSub) + "\n")
        files.write("Scan completed at: " + str(current_time) + "\n")          
    return
    
    
def main():
        DirName = input("Enter a Log file name: ")
        schedule.every(10).minutes.do(DirectoryScan,DirName)
        while True:
            schedule.run_pending()
            time.sleep(1)
            


if __name__ == "__main__":
    main()
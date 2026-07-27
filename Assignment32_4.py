#Scheduler

import schedule,time
import datetime

def FileBackup(SFilePath, DFilePath):
    BackupList =[]
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(SFilePath, "r") as f:
        for file in f:
            BackupList.append("backup_"+file.strip() + " : " + current_time)
    with open(DFilePath, "a") as f:
        for backup in BackupList:
            f.write(backup + "\n")
    
    
def main():
    
    SourcePath = input("Enter the file path: ")
    DestinationPath = input("Enter the destination path: ")
    
    schedule.every(5).minutes.do(FileBackup, SourcePath, DestinationPath)
    while True:
        schedule.run_pending()
        time.sleep(1)
    
        

if __name__ == "__main__":
    main()

import schedule
import time
import os
import datetime

def CreateLogs():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    FileName = "MarvelleousLog.txt"
    with open(FileName, "a") as files:
        files.write(f"{FileName } + {current_time}\n")
    return
    
    
def main():
        schedule.every(10).minutes.do(CreateLogs)
        while True:
            schedule.run_pending()
            time.sleep(1)
            


if __name__ == "__main__":
    main()
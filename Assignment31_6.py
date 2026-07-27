import schedule
import time
import os
import datetime

def Goal():
    current_time = datetime.datetime.now()
    print(f"{current_time} : Start your Weekly goal...")                 
    return
def Progress():
    current_time = datetime.datetime.now()
    print(f"{current_time} : Review your Weekly progress...")                 
    return

def Daily():
    current_time = datetime.datetime.now()
    print(f"{current_time} : Weekly work completed....")
    return
    
    
def main():
        schedule.every().monday.at("09:00").do(Goal)
        schedule.every().wednesday.at("17:00").do(Progress)
        schedule.every().friday.at("18:00").do(Daily)


        while True:
            schedule.run_pending()
            time.sleep(1)
            


if __name__ == "__main__":
    main()
#Scheduler

import schedule,time
import datetime

def time():
    
    Current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print("Current Time:", Current_time)
    
def main():
    schedule.every(1).minutes.do(schedule.time)
    while True:
        schedule.run_pending(time)
        time.sleep(1)
        
        

if __name__ == "__main__":
    main()
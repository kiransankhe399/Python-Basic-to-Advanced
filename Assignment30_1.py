#Scheduler

import schedule,time

def job():
    print("Jay Ganesh...")
    
def main():
    schedule.every(1).seconds.do(schedule.job)
    while True:
        schedule.run_pending(job)
        time.sleep(1)
        

if __name__ == "__main__":
    main()
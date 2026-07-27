#Scheduler

import schedule,time

def doJob():
        print("Coding Kar...")
    
def main():
    schedule.every(30).minutes.do(schedule.doJob)
    while True:
        schedule.run_pending(doJob)
        time.sleep(1)
        

if __name__ == "__main__":
    main()
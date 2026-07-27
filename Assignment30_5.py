#Scheduler

import schedule,time
import datetime

def doJob():
        with open("Marvelleous.txt", "a") as f:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"Task Executed at  : {current_time} \n")

    
def main():
    schedule.every(5).minutes.do(doJob)
    while True:
        schedule.run_pending()
        time.sleep(1)
        

if __name__ == "__main__":
    main()
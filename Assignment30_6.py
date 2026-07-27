#Scheduler

import schedule,time

def LunchTime():
       print("Lunch Time...")
       
def WrapTime():
         print("Wrap Time...")

    
def main():
    schedule.every(5).days.at("01:00").do(LunchTime)
    schedule.every(5).days.at("06:00").do(WrapTime)
    while True:
        schedule.run_pending()
        time.sleep(1)
    
        

if __name__ == "__main__":
    main()
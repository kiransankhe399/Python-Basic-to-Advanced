#Scheduler

import schedule,time

def doJob():
        print("Namaskar...")
    
def main():
    schedule.every().day.at("09:30").do(doJob)
    while True:
        schedule.run_pending()
        time.sleep(1)
        

if __name__ == "__main__":
    main()
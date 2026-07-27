import datetime
import schedule

def doJob(message, time):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Job executed at {current_time}: {message} after {current_time} seconds." )
    return 
    
    
def main():
        message = input("Enter a message: ")
        time = int(input("Enter the time in seconds: "))
        schedule.every(time).seconds.do(doJob, message, time)
        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == "__main__":
    main()
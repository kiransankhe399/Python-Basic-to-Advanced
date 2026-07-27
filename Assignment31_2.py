import datetime
import schedule
import time

def DisplayMessages(message):
    print(f"{message}" )
    return 
    
    
def main():
        message = input("Enter a message: ")
        schedule.every(5).seconds.do(DisplayMessages, message)
        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == "__main__":
    main()
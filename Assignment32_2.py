import schedule
import time
import os
import datetime


def FileSize(fileName):
    if not os.path.exists(fileName):
        print(f"File '{fileName}' does not exist.")
        return

    file_size = os.path.getsize(fileName)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{current_time}] File Size of '{fileName}' is {file_size} bytes")


def main():
    fileName = input("Enter a file name: ")

    schedule.every(30).seconds.do(FileSize, fileName)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
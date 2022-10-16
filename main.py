import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Please Drink Water",
            message="You need to atleast take one sip of water after every hour",
            app_icon="C:\\Users\\SUBHAJIT\\OneDrive\\Desktop\\Python_Projects\\water.ico",
            timeout=10
        )
        time.sleep(20)
        # exit()
        # Or ctrl + C for exiting or kill the task in the task manager

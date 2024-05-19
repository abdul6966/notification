import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Did you drink enough water today?",
            message="About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon=r"C:\Users\Abdul Nayeem\Desktop\Python projects\notification\icon.ico",
            timeout=
        )
        time.sleep(10)

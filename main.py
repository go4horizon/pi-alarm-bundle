import time
import RPi.GPIO as GPIO

from env import B_PIN
from src.ButtonPublisher import ButtonPublisher
from src.LanPublisher import LanPublisher
from src.Status import Status
from src.StatusObserver import StatusObserver

status = Status()
observer = StatusObserver()

status.attach(observer)

lanListener = LanPublisher(status)

# GPIO.setmode(GPIO.BCM) # not required for current logic

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)
GPIO.setup(B_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
buttonListener = ButtonPublisher(status)
GPIO.add_event_detect(B_PIN, GPIO.RISING, callback=buttonListener.publish_status)



def run():
    while True:
        for i in range(6):
            lanListener.publish_status()
            time.sleep(10)


if __name__ == '__main__':
    run()

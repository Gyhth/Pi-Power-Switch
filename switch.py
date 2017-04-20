import RPi.GPIO as GPIO
from subprocess import call
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        call("shutdown -h now \"Shut down by button.\"", shell=True)
		time.sleep(0.2)

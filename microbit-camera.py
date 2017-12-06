from picamera import PiCamera
from gpiozero import Button
from time import sleep
button = Button(4, pull_up = False)

while True:
    with PiCamera() as camera:
        camera.start_preview()
        sleep(5)
        button.wait_for_press()
        camera.capture('selfie.jpg')
        camera.stop_preview()

from picamera import PiCamera
from gpiozero import Button
from time import sleep
import glob, os

button = Button(4, pull_up = False)

while True:
    with PiCamera() as camera:
        button.wait_for_press()
        camera.start_preview()
        sleep(5)
        n = len(glob.glob('./images/img_*.jpg'))
        filename = './images/img_' + str(n) + '.jpg'
        camera.capture(filename)
        os.system('xdg-open ' + filename)
        camera.stop_preview()

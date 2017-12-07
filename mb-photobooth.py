from microbit import *

while True:
    if pin0.is_touched():
        for i in range(4):
            curr_count = 3 - i
            
            if curr_count > 0:
                display.show(str(curr_count))
                sleep(1000)
        pin1.write_digital(1)
        sleep(100)
        display.show(' ')
        pin1.write_digital(0)

import RPi.GPIO as GIPO     # import RPi.GPOP module (to control the GPIO Pins)
import time                 # import time module (to use time operations)
GIPO.setmode(GIPO.BOARD)    # set to the use of board numbering
GIPO.setup(13,GIPO.OUT)     # set the GIPO pin 13 as an input
GIPO.setup(15,GIPO.IN)

    GIPO.output(13,True)
    time.sleep(1)
    GIPO.output(13,False)
    time.sleep(1)

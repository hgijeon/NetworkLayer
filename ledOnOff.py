from RPi.GPIO import cleanup, setmode, setup, output, BOARD, OUT
from time import sleep

setmode(BOARD)

setup(7, OUT)

def on(): output(7, True)
def off(): output(7, False)

def blink(n = 5, s = .1):
    for i in range(n):
        on()
        sleep(s)
        off()
        sleep(s)

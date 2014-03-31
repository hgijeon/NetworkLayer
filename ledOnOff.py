from RPi.GPIO import cleanup, setmode, setup, output, BOARD, OUT, setwarnings
from time import sleep

setmode(BOARD)

setwarnings(False)

setup(7, OUT)

def on():
    setup(7, OUT)
    output(7, True)
def off():
    output(7, False)
    setup(7, IN)
    

def blink(n = 5, s = .1):
    for i in range(n):
        on()
        sleep(s)
        off()
        sleep(s)

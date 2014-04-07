from RPi.GPIO import cleanup, setmode, setup, output, BOARD, OUT, IN, setwarnings
from time import sleep

setmode(BOARD)

setwarnings(False)

setup(7, IN)

def on():
    setup(7, OUT)
    output(7, True)
def off():
    setup(7, IN)
    

def blink(n = 5, s = .1):
    for i in range(n):
        on()
        sleep(s)
        off()
        sleep(s)

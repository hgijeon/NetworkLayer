import RPi.GPIO as G
from time import sleep
import morse

G.setmode(G.BOARD)

def chargetime(s = .01):

    ct = 0

    G.setup(12, G.OUT)
    G.output(12, G.LOW)
    sleep(s)
    G.setup(12, G.IN)

    while not G.input(12):
        ct = ct + 1

    return ct

def chargetimes(n = 100, s = .1):
    return [chargetime(s) for i in range(n)]

def mean(l):
    return sum(l)/len(l)

def printGT(l):
    avg = mean(l)
    for x in l:
        if x > avg:
            print("|")
        else:
            print("|=====")


def isOn(value):
    return value < 10

def getLed(s = .1):
    return isOn(chargetime(s))

def led2seq():
    li = chargetimes(500, 0.02)
    #print(li)
    avg = mean(li)
    return ['1' if isOn(e) else '0' for e in li]

def led2morse():
    return morse.seq2an(led2seq())

def test():
    ##
    ##print(chargetime())
    tmp = chargetimes()
    print(tmp)
    #seq = led2seq()
    #print(seq)

    #print(led2morse())

import ledOnOff
import chargetimes
import time

ledOnOff.on()
time.sleep(0.1)
print("Detect LED 'on': " + str(chargetimes.getLed()))

ledOnOff.off()
time.sleep(0.1)
print("Detect LED 'off': " +  str(not chargetimes.getLed()))


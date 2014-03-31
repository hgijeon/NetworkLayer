import ledOnOff
import chargetimes
import time

ledOnOff.on()
time.sleep(0.001)
print("Detect LED 'on': " + str(chargetimes.getLedResistor()))

ledOnOff.off()
time.sleep(0.001)
print("Detect LED 'off': " +  str(not chargetimes.getLedResistor()))



import physicalLayer

pl = physicalLayer.PhysicalLayer()

while True:
    ret = pl.receiveResistor()
    if ret != None:
        print(ret)
        

#Instructions:
#Run the Receiver - wait for it to be set up
#Run the Sender

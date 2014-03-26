import physicalLayer

pl = physicalLayer.PhysicalLayer()

while True:
    ret = pl.receiveResistor()
    if ret != None:
        print(ret)
        

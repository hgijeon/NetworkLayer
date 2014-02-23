import physicalLayer

pl = physicalLayer.PhysicalLayer()

while True:
    ret = pl.receive()
    if ret != None:
        print(ret)
        

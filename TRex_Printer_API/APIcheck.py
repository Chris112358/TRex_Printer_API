
from trexprinterapi import  TRexObserver
import time
import asyncio

if __name__ == "__main__":
    
    scan = 20

    trex = TRexObserver("192.168.178.98", port=8899, scan_intervall=scan )

    print(asyncio.run(trex.force_get()))

    print(asyncio.run(trex.get()))

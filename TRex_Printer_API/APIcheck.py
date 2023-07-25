
from trexprinterapi import  TRexObserver
import time
import asyncio
import logging


'''logging.basicConfig(filename='trexprinterapi/API.log', 
                    filemode='w',
                    encoding='utf-8', 
                    level=logging.DEBUG,
                    format='%(asctime)s : %(name)-8s : %(levelname)-10s :: %(message)s')'''

if __name__ == "__main__":
    
    scan = 2

    trex = TRexObserver("192.168.178.98", port=8899, scan_intervall=scan )

    print(asyncio.run(trex.force_get()))

    for i in range(10):

        print(asyncio.run(trex.force_get()))
        time.sleep(5)

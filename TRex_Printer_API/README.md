This package will provide an API to connect to a trex 3d printer.
Currently its on development.


To install this package use 
```
pip install trexprinterapi
```

Than import it in your python program and initialise the Api with the following command

```
from trexprinterapi import TRexObserver
trex = TRexObserver(ip)
```

Observe that you need to specify at least the ip address. Additionally you can set the port (default 8899) and scan_intervall (default 600)

The scan_intervall should not be to small or else other programms comunicating with the printer may be disconnected.

This package is fully asyncrounus so you need to await all the methods for fetching data.

The following methods are available:

```
trex.update_server(ip:str=None, port:int=None, scan_intervall:int=None)
```
This method updates the ip address, port and scan_intervall. 

```
data = await trex.get()
data = await trex.force_get()
```
methods to fetch the data. the force_get ignores the scan_intervall and connects to the printer immediately.


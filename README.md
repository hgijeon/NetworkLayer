NetworkLayer
============

NetworkLayer contains code for chat server and client. The hope is to create one that communicates, through a router, from one LAN to other LANs.

How it Works
============

Client/Server <-- newSocket [socket_received and socket_sender] <-- IP Layer <-- DataLink --> PhysicalLayer [chargetimes,ledOnOff,morse,Receiver,Sender,routingIn,routingOut] --> StandardSocket 

Ethernet communicates through routingIn and routingOut

timeAlarm affects DataLink and newSocket

How to Run it
=============

Run UDP_Client and/or UDP_Server

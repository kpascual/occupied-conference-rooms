# Occupied Conference Rooms - IoT Sensors

Problem: It's very difficult to find an unoccupied conference room. Can we create something that makes that search less painful?

Objective: Create visualization and set of sensors that detect when a conference room is unoccupied 

## Architecture Diagram

![Architecture Diagram](https://github.com/kpascual/occupied-conference-rooms/blob/master/architecture_diagram.png)

## Solution

In each of 3 small conference rooms, I installed an ESP8266 attached to two sensors: a reed switch attached to the door, and a passive infrared sensor (PIR) pointing at the room's interior. The reed switch would detect whether the door was open or closed, while the PIR sensor detected movement inside the room.

Upon any stimulus, each sensors would publish its state via MQTT to a message broker on a remote Raspberry Pi. The ESP8266 modules and Pi were connected to an intermediate router, which happened to be my phone (I had trouble setting up an access point on the Raspberry Pi, and given I only had 2 days to complete this, using my phone's hotspot functionality seemed most expedient).

Also on the Raspberry Pi was a static HTML file, containing a Javascript-based MQTT subscriber that would listen to messages from the broker. This listener utilized Websockets via a Paho client. The HTML file displayed a representation of the three conference room states. When the door was closed, the borders of the rooms would appear red, and when open it would be green. Same for the infrared sensor, when it sensed movement the room interior would appear red, and green when no movement sensed. 

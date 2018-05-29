import paho.mqtt.client as mqtt
import os
import datetime


TOPIC = 'doorsensor'

def on_connect(client, userdata, flags, rc):
    client.subscribe(TOPIC)   


def on_message(client, userdata, msg):
    print (msg.payload, userdata, datetime.datetime.now())
    room, doorVal, pirVal = msg.payload.split(';')
    map_roomnotes = {
        'F0': 'C',
        'F1': 'D',
        'F2': 'E'
    }

    if doorVal == '1' and userdata[room] == '0':
        os.system('omxplayer -o local ' + map_roomnotes[room] + '_good.wav')

    userdata[room] = doorVal
    


priors = {
    'F0': 1,
    'F1': 1,
    'F2': 1
}

client = mqtt.Client(userdata=priors)
client.on_connect = on_connect
client.on_message = on_message


client.connect("localhost", 1883, 60)

client.loop_forever()

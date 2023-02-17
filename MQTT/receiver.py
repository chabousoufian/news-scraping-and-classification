import paho.mqtt.client as mqtt
import time
import xmltodict
import json
import pymongo #for the connection with mongodb
import bson


MONGO_HOST ="localhost"
MONGO_PORT = "27017"
MONGO_TIMEOUT = 1000
MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PORT+"/"

Connected = False


brocker_address = "localhost"
port = 1883



print("creating new instance")
client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connect to brocker")
        global Connected
        Connected = True
    else:
        print("Connection faild")

def on_message(client, userdata, message):
    #print("message received ", str(message.payload.decode("utf-8")))
    Data = str(message.payload.decode("utf-8"))
    try:
        client=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIMEOUT)
        client.server_info()
        print("connected to DB")
    except Exception:
        pass
    db = client["Mosquitto"]
    collection = db["scraping"]
    my_dict = json.loads(Data)

    Insertion_result = collection.insert_many(my_dict)
    print(Insertion_result)
    print("insert successfully")
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


client.on_message = on_message
client.on_connect = on_connect

print("connecting to broker")
client.connect(brocker_address, port)
client.loop_start()


while Connected != True:
    time.sleep(0.1)


print("Subscribing to topic","mongodb")
client.subscribe("mongodb")

#------------------------------------------------------------------------- 
try:
    while True: 
        time.sleep(1)
#------------------------------------------------------------------------- 
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()
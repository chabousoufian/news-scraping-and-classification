import json
import paho.mqtt.client as mqtt
import time
import csv
## text to XML

csv_path_file = "/Users/soufianchabou/Desktop/Web Scraping/News/dataset.csv"

data = {}

def convert_csv_to_json(text_path_file):
    with open(text_path_file) as File:
        data = json.dumps(list(csv.DictReader(File)))
    return data

data = convert_csv_to_json(csv_path_file)



######################################################################## 
def on_connect(client, userdata, flags, rc):
        if rc == 0:
                print("Connected to broker")
                global Connected 
                Connected = True
        else:
                print("Connection failed")
########################################################################

def on_publish(client,userdata,result):
        print("data published \n")
        pass
########################################################################
# Code principal  
########################################################################

Connected = False
#broker_address= "broker.hivemq.com" 
broker_address= "localhost" #Mosquitto en local
port = 1883
client = mqtt.Client("news_publisher") #create new instance
client.on_connect= on_connect #attach function to callback
client.on_publish = on_publish #attach function to callback 
client.connect(broker_address, port=port) #connect to broker
client.loop_start() #start the loop


while Connected != True: #Wait for connection
        time.sleep(0.1)


#------------------------------------------------------------------------
try:
    print("publishing to mongodb")
    client.publish("mongodb", payload=str(data))
    time.sleep(1)
    print("News published with success to mongodb")

#-------------------------------------------------------------------------
except KeyboardInterrupt:
        print("sortir de la boucle exiting")
        client.disconnect()
        client.loop_stop()
 
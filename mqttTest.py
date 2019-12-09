#MQTT TestmqttClient GUI
import paho.mqtt.client as mqtt
from time import sleep
import threading
import time


#Connect to Server
def process_connect2Server():
    ##connect to MQTTServer:  
    print("start connect")
    mqttClient.connect("broker.hivemq.com", 1883, 60)
    mqttClient.loop_start()
    

#after connection was established
def on_connect(mqttClient, userdata, flags, rc):
    print("connected")
    #subscribe for topics
    mqttClient.subscribe("t0", 0)
    print("subscribed for topic t0")
    

#Reseive messages: startRound, stopRound
def on_message(mosq, obj, msg):
    try: 
        if msg.topic.startswith("t0"):
            s = str(msg.payload).replace('b', '')
            s = s.replace('\'', '')
            print(s)
            print(str(msg.payload))
            thread1 = myTimerThread(1, "Thread-1")
            thread1.start()
    except:
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(sys.exc_info()[2])
        

class myTimerThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      print ("Starting " + self.name)
      sec=15
      while (sec>0):
        time.sleep(1)
        print(str(sec))
        sec=sec-1
      print("Stop")
      ok = mqttClient.publish("t1", "fertig")



#Main-Program
print("START")
mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message

process_connect2Server()

while True:
    time.sleep(2)



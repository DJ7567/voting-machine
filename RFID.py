import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import pandas as pd

reader = SimpleMFRC522()


def write(text):
   reader.write(text)
   print("Written")
      
def Register():
   df=pd.read_csv("data.csv")
   num=df.shape[0]
   print("place your card near the sensor to register :")
   id, text = reader.read()
   for i in range(num):
   	if df["RFID"][i]==id:
   		print("\n\nThis card is already registerd\n\n")
   		return False
   	else:
   		pass
   print(id)
   return id
        
def check_RFID():
   df=pd.read_csv("data.csv")
   num=df.shape[0]
   print("\n\nplace your card near the sensor to vote:")
   id, text = reader.read()
   for i in range(num): 
        if id==df["RFID"][i]:
            
                print("\n\nRFID MATCH YOU CAN VOTE NOW\n\n")
                ID = df["RFID"][i]
                return i
   return -1

       


import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import pandas as pd

reader = SimpleMFRC522()

df=pd.read_csv("data.csv")
num=df.shape[0]

print(num)

def write(text):
   reader.write(text)
   print("Written")
      
def Register():
   print("place your card near the sensor to register :")
   id, text = reader.read()
   for i in range(num):
   	if df["RFID"][i]==id:
   		print("This card is already registerd")
   		return False
   	else:
   		pass
   print(id)
   return id
        
def check_RFID():
   for i in range(num):
   	id, text = reader.read()
   	if id==df["RFID"][i]:
       		print("RFID MATCH YOU CAN VOTE NOW")
       		ID = df["RFID"][i]
        	return i
   	else:
        	print("RFID NOT MATCHED ARE YOU A SCAMER ")
        	return False
            


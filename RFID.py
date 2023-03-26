import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()


def write(text):
   reader.write(text)
   print("Written")
      
def Register():
   print("place your card near the sensor to register :")
   id, text = reader.read()
   print(id)
   return id
        
def check_RFID(ID):
   id, text = reader.read()
   if id==ID:
       print("RFID MATCH YOU CAN VOTE NOW")
       return True
   else:
       print("SORRY YOU ARE NOT REGISTERED OR ALREADY VOTED SO PLEASE GET OUT")
       return False
            


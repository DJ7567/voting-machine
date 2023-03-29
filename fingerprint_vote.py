# importing R305 lib and Serial lib for uart comunication 
import time
import serial
import pandas as pd
import adafruit_fingerprint

# Intiallizing the Uart 
uart = serial.Serial("/dev/ttyS0", baudrate=57600, timeout=1)

finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

#pins TX -14/ RX -15



def Max_Size():
	if finger.read_sysparam() != adafruit_fingerprint.OK:
        	raise RuntimeError("Failed to get system parameters")
	max_size=finger.library_size
	max_size = max_size -1
	return max_size 
	
def vaild_location(a):
	Max= Max_Size()
	if a>=0 and a<Max:
		return a
	else:
		return False
        
def Register_New_FP():
    df=pd.read_csv("data.csv")
    num=df.shape[0]  
    location=vaild_location(num) 
    
    if location == False and location !=0:
    	print("location problem")
    	return False
    #################################################  checking that data not already registered
    
    ID=Find_fingerprint()
    for i in range(num):
    	if ID==df["PF"][i]:
    		print("Finger print already registered")
    		return -1
    		
    if finger.count_templates() != adafruit_fingerprint.OK:
        raise RuntimeError("Failed to read templates")
    print("Number of templates found: ", finger.template_count)
####################################
    for fingerimg in range(1, 3):
        if fingerimg == 1:
            print("Place finger on sensor...", end="")
        else:
            print("Place same finger again...", end="")

        while True:
            i = finger.get_image()
            if i == adafruit_fingerprint.OK:
                print("Image taken")
                break
            if i == adafruit_fingerprint.NOFINGER:
                print(".", end="")
            elif i == adafruit_fingerprint.IMAGEFAIL:
                print("Imaging error")
                return -1
            else:
                print("Other error")
                return -1
             
## Creating a Templete

        print("Templating...", end="")
        i = finger.image_2_tz(fingerimg)
        if i == adafruit_fingerprint.OK:
            print("Templated")
        else:
            if i == adafruit_fingerprint.IMAGEMESS:
                print("Image too messy")
            elif i == adafruit_fingerprint.FEATUREFAIL:
                print("Could not identify features")
            elif i == adafruit_fingerprint.INVALIDIMAGE:
                print("Image invalid")
            else:
                print("Other error")
            return -1

#remove
        if fingerimg == 1:
        	print("Remove finger")
        	time.sleep(1)
        while i != adafruit_fingerprint.NOFINGER:
        	i = finger.get_image()
                
# Creating a model                

    print("Creating model...", end="")
    i = finger.create_model()
    if i == adafruit_fingerprint.OK:
        print("Created")
    else:
        if i == adafruit_fingerprint.ENROLLMISMATCH:
            print("Prints did not match")
        else:
            print("Other error")
        return -1

# storing the model

    print("Storing model #%d..." % location, end="")
    i = finger.store_model(location)
    if i == adafruit_fingerprint.OK:
        print("Stored")
    else:
        if i == adafruit_fingerprint.BADLOCATION:
            print("Bad storage location")
        elif i == adafruit_fingerprint.FLASHERR:
            print("Flash storage error")
        else:
            print("Other error")
        return -1

    return location


def Find_fingerprint():
  print("Waiting for image...")
  while finger.get_image() != adafruit_fingerprint.OK:
  	pass
  print("Templating...")
    	
  if finger.image_2_tz(1) != adafruit_fingerprint.OK:
        return -1
  print("Searching...")
    	
  if finger.finger_search() != adafruit_fingerprint.OK:
        return -1
  print("Detected #", finger.finger_id, "with confidence", finger.confidence)
  
  return finger.finger_id
    
def delete_pf(num):
  if finger.delete_model(num) == adafruit_fingerprint.OK:
            print("Deleted!")
            if finger.count_templates() != adafruit_fingerprint.OK:
            	raise RuntimeError("Failed to read templates")
            print("Number of templates found: ", finger.template_count)
  else:
            print("Failed to delete")
	
   


	

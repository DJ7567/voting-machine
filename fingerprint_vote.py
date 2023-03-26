# importing R305 lib and Serial lib for uart comunication 

import serial
import adafruit_fingerprint

# Intiallizing the Uart 
uart = serial.Serial("/dev/ttyAMA1", baudrate=57600, timeout=1)

finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

#pins TX -0/ RX -1


def Max_Size():
	if finger.read_sysparam() != adafruit_fingerprint.OK:
        	raise RuntimeError("Failed to get system parameters")
	max_size=finger.library_size
	max_size = max_size -1
	return max_size 
	
def vaild_location(a):
	Max= Max_Size()
	if a>0 and a<Max:
		return a
	else:
		return -1
        
def Register_New_FP(location):
    
    for i in range(1, 3):
        if i == 1:
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
                return False
            else:
                print("Other error")
                return False

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
            return False


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
        return False

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
        return False

    return True


def Find_fingerprint():
  print("Waiting for image...")
  while finger.get_image() != adafruit_fingerprint.OK:
  	pass
  print("Templating...")
    	
  if finger.image_2_tz(1) != adafruit_fingerprint.OK:
        return False
  print("Searching...")
    	
  if finger.finger_search() != adafruit_fingerprint.OK:
        return False
    	#print("Detected #", finger.finger_id, "with confidence", finger.confidence)
    
  return finger.finger_id
    
def delete_pf(location):
  if finger.delete_model(location) == adafruit_fingerprint.OK:
            print("Deleted!")
  else:
            print("Failed to delete")
	
   


	

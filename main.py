import fingerprint_vote as fp
import RFID
import time
import pandas as pd

########################################################### phone number ############################################## 
def Phone_numer():
  for i in range(2):
      Phone_number=input("Phone number")
      if Phone_number.isdigit() and len(Phone_number) == 10:
          return Phone_number
          break
      else:
          if i==1:
          	return False
          print("plase Enter vaild number 10 digit number(One attempt left:")
  
########################################################### Register ##################################################
def Registration():
	
#Name
  name=input("Enter your full name ex[First Last] :")	
  
#Phone number
  Phone_number=Phone_numer()
  if Phone_number == False:
       return False
     
#RFID	
  for i in range(2):	
       ID=RFID.Register()
       if ID != False:
          print("ID is taken :......................")
       else:
          if i==1:
          	ID = True
          	return False
          print("try again ....last attempt")
		
       
#Finger_print
  ID_finger=fp.Register_New_FP()
  if ID_finger== False:
  	return False
  print("Finger print registered.....")
  
	
# data added to csv
  df=pd.read_csv("data.csv")
  data = { "RFID" :[ID],"Name" :[name],"Number":[Phone_number],"PF":[ID_finger] }
  df1 = pd.DataFrame(data)
  df = pd.concat([df,df1],ignore_index=True)
  df.to_csv("data.csv",index=False)
  time.sleep(2)
  print("The data is registerd.............Thank you")
	
############################################################# Verification #############################################

def verify():
  df=pd.read_csv("data.csv")
  location=RFID.check_RFID()
  if location!= False:
       print("Name :" + df["Name"][locaton])
       #print("Number :" + str(df["Number"][location]))
  else:
       print("incorrect")
       return False
  
  print("Verify your finger Print")
  ID_finger=fp.Find_fingerprint()
  if location==False:
       print("incorrect")
       return False
  if df["PF"][location]==ID_finger:
       print("Now you can vote")
       return Ture

################################################################# Delete ################################################

def delete():
    df=pd.read_csv("data.csv")
    df.drop(index=2)
    fp.delete_pf(2)

################################################################ Display ################################################

def display():
	df=pd.read_csv("data.csv")
	print(df)
	
#################################################################  Main #################################################

Registration()
display()
verify()
delete()
display()






  
	

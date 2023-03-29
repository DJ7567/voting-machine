import fingerprint_vote as fp
import RFID
import time
import pandas as pd

########################################################### phone number ############################################## 
def Phone_numer():
  for i in range(2):
      Phone_number=input("Phone number")
      df=pd.read_csv("data.csv")
      lenght=df.shape[0]
      flag=1
      ##  checking in data base ##
      for i in range(lenght):
          if int(Phone_number)==df["Number"][i]:
          	flag=0
      ##  checking is valid ##
      if Phone_number.isdigit() and len(Phone_number) == 10 and flag: 
          return int(Phone_number)
          break
      else:
          if i==1:
  
          	return False
          print("plase Enter vaild and unregisted number 10 digit number(One attempt left:")
  
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
          print("\nID is taken :......................\n\n")
          break
       else:
          if i==1:
          	ID = True
          	return False
          print("try again ....last attempt")
          time.sleep(2)
		
       
#Finger_print

  for i in range (2):
	  ID_finger=fp.Register_New_FP()
	  print(ID_finger)
	  if ID_finger== -1 and i==1:
	  	return False
	  if ID_finger== -1 :
	  	print("Try...again for last time")
	  	time.sleep(3);
	  else:
	  	break
  print("\n\nFinger print registered.....\n\n")
  
	
# data added to csv
  df=pd.read_csv("data.csv")
  data = { "RFID" :[ID],"Name" :[name],"Number":[Phone_number],"PF":[ID_finger] ,"status" : [0]}
  df1 = pd.DataFrame(data)
  df = pd.concat([df,df1],ignore_index=True)
  df.to_csv("data.csv",index=False)
  time.sleep(2)
  print("\n\n\nThe data is registerd.............Thank you\n\n")
	
############################################################# Verification #############################################

def verify():
  df=pd.read_csv("data.csv")
  location=RFID.check_RFID()
  print(location)
  if location!= -1:
       print("Name :" + df["Name"][location])
       #print("Number :" + str(df["Number"][location]))
  else:
       print("!!!! RFID NOT MATCHING WITH DATABASE")
       return False
  
  print("Verify your finger Print")
  ID_finger=fp.Find_fingerprint()
  
  if df["PF"][location]==ID_finger:
       print("Now you can vote")
       df["status"][location]=1;
       #df["status"][location]=0;
       df.to_csv("data.csv",index=False)
       return True
  else:
       print("Verification fail")
       return False
  return True

################################################################# Delete ################################################

def delete():
    df=pd.read_csv("data.csv")
    num=df.shape[0] -1
    df=df.drop(index=num)
    fp.delete_pf(num)
    df.to_csv("data.csv",index=False)
    

################################################################ Display ################################################

def display():
	df=pd.read_csv("data.csv")
	print(df)
	
#################################################################  Main #################################################


while True:
	print("GIVE OUR INPUT HERE :")
	print("a.display")
	print("b.Registration")
	print("c.vote")
	print("d.delete")
	
	Input = input("input :");
	
	if Input =="a":
		display()
	if Input =="b":
		Registration()
	if Input =="c":
		a=verify()
		if a:
			print("vote done")
		else:
			print("vote not done")
	if Input =="d":
		delete()
	
	









  
	

import fingerprint_vote as fp
import RFID
import time
import pandas as pd



########################################################### phone number ############################################## 
def Phone_numer(Phone_number):

      df=pd.read_csv("data.csv")
      lenght=df.shape[0]
      flag=1
      
      ##  checking in data base ##
      for j in range(lenght):
          if int(Phone_number)==df["Number"][j]:
          	flag=0
          
      ##  checking is valid ##
      if Phone_number.isdigit() and len(Phone_number) == 10 and flag: 
          return True
          
      else:
          print("invaild number")
          return False
###############################

def RFID():
	ID=RFID.Register()
	if ID != False:
		print("\nID is taken :......................\n\n")
		return ID
	else:
        	
          	return False
        
########################################################### Register ##################################################
def finger_print_R():
	return fp.Register_New_FP()
	
	
########################################################### FP #######################################################

def data_update(name,Phone_number,ID,ID_finger):
	df=pd.read_csv("data.csv")
	data = { "RFID" :[ID],"Name" :[name],"Number":[Phone_number],"PF":[ID_finger] ,"status" : [0]}
	df1 = pd.DataFrame(data)
	df = pd.concat([df,df1],ignore_index=True)
	df.to_csv("data.csv",index=False)
	time.sleep(2)
	print("\n\n\nThe data is registerd.............Thank you\n\n")	
	
# data added to csv
  
def finger_print_C():
	return fp.Find_fingerprint()
	
############################################################# Verification #############################################
"""
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
"""
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
""""

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
	
	

"""







  
	

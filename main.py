#import fingerprint_vote as fp
import RFID
import time
import pandas as pd

#ata = {"RFID" :[1],"Name" :["helo"],"Number":[775],"PF":[0]}
#df =pd.DataFrame(data)
#df.to_csv("data.csv",index=False)
df=pd.read_csv("data.csv")

"""
for i in range(3):
 
  ID=RFID.Register()
  print("ID is taken :....")
  name=input("Enter your name:")
  number=int(input("phone number"))
  data = { "RFID" :[ID],"Name" :[name],"Number":[number],"PF":[i] }
  df1 = pd.DataFrame(data)
  df = df.append(df1,ignore_index=True)
  df.to_csv("data.csv",index=False)
  
  time.sleep(2)
  print(df)"""

for i in range(3):
	flag=RFID.check_RFID(df["RFID"][i])
	if flag==1:
		print("Name :" + df["Name"][i])
		print("Number :" + str(df["Number"][i]))
		print("Now you can vote")
		break
		



"""
location=fp.vaild_location(a)

fp.Register_New_FP(location)

fp.time.sleep(1)

ID=fp.Find_fingerprint()

print("ID :"+ str(ID) +" \n")

fp.delete_pf(location)"""


  
	

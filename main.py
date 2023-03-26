import fingerprint_vote as fp


a = 1


location=fp.vaild_location(a)

fp.Register_New_FP(location)
fp.time.sleep(1)
ID=fp.Find_fingerprint()

print("ID :"+ str(ID) +" \n")

fp.delete_pf(location)


  
	

import tkinter as tk
import time 
import function as main 
import GSM 
import pandas as pd

######################################################   Main Classs   ##########################################
class Voting(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Voting System")
        self.h=self.winfo_screenheight()
        self.w=self.winfo_screenwidth()
        self.r= str(self.w)+"x"+str(self.h)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.geometry(self.r)
        self.current_frame = None
        self.switch_frame(LoginFrame)
        
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack()
        
        
        
        
######################################################    Login Frame ##############################################         

class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        self.canvas = tk.Canvas(self, width=300, height=300)
        self.label = tk.Label(self, text="Login ID :",font=("Helvetica", 20),fg="blue")
        self.username_entry = tk.Entry(self,width = 40 )
        self.label_new = tk.Label(self, text="Password :",font=("Helvetica", 20),fg="blue")
        self.password_entry = tk.Entry(self, show="*",width = 40 )
        self.image2 = tk.PhotoImage(file="images.png")
        self.canvas.create_image(0, 0, anchor="nw", image=self.image2,tag="image")
        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.configure(bg="black", fg="white", font=("Arial", 20))
        
        self.canvas.grid(column=1,pady=20)
        self.label.grid(row=1, column=0,pady=20)
        self.label_new.grid(row=2, column=0)
        self.username_entry.grid(row=1, column=1)
        self.password_entry.grid(row=2, column=1 ,pady=30)
        self.login_button.grid(column=1)
        
        
        
    def login(self):
    	if self.username_entry.get()== "Narendra" and self.password_entry.get() == "vote" :
            self.master.switch_frame(Select)
    	else:
    		print("not valid")
        
        
        
######################################################   Verify   ##############################################   
class Verify(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
      
        
        self.label = tk.Label(self,text="Verifing the User is Valid",font=("Helvetica",30))
        
        self.label_RFID = tk.Label(self,text="RFID :",font=("Helvetica",20),fg="orange",)
        self.label_RFID_status = tk.Label(self,text="",font=("Helvetica",20))
        self.label_button_RFID = tk.Button(self, text="RFID Registration", command=self.RFID,font=("Helvetica", 15))
        
        self.label_PF = tk.Label(self ,text="Finger Print :",font=("Helvetica",20),fg="black")
        self.label_PF_status = tk.Label(self,text="",font=("Helvetica",20))
        self.login_button_PF= tk.Button(self, text="Finger Print Registration",command=self.finger_print,font=("Helvetica", 15))
        self.OTP_entry = tk.Entry(self,width = 40)
        self.label_OTP = tk.Label(self ,text="Enter The OTP :",font=("Helvetica",20),fg="green")
        self.label_OTP_status = tk.Label(self,text="",font=("Helvetica",20))
        
        
        self.verify_button = tk.Button(self, text="Verify", command=self.submit,font=("Helvetica",20))
        
        
        self.label.grid(row=0,column=1,pady=100,ipadx=100)
        
        
        self.label_RFID.grid(row=1,column=0)
        self.label_RFID_status.grid(row=1,column=2,pady=30)
        self.label_button_RFID.grid(row=1,column=1,pady=30)
        
        self.label_PF.grid(row=2,column=0)
        self.login_button_PF.grid(row=2,column=1,pady=30)
        self.label_PF_status.grid(row=2,column=2,pady=30)
        
        self.label_OTP.grid(row=3,column=0)
        self.OTP_entry.grid(row=3,column=1)
        self.label_OTP_status.grid(row=3,column=2,pady=30)
        
        self.verify_button.grid(row=4,column=1,ipadx=100)
        
        
    def RFID(self):
    	self.ID=main.RFID_C()
    	df=pd.read_csv("data.csv")
    	num=df.shape[0]
    	print(num)
    	for i in range(num): 
    		print(df["RFID"][i])
    		if self.ID==df["RFID"][i]:
    			print(i)
    			print(df["Number"][i])
    			self.i=i
    			print(self.i)
    		if self.ID==False:
    			self.label_RFID_status.configure(text="Invalid ",fg="red")
    		else:
    			self.label_RFID_status.configure(text="valid ",fg="green")
    				
    def finger_print(self):
    	self.ID_finger=main.finger_print_C()
    	df=pd.read_csv("data.csv")
    	num = df.shape[0]
    	for j in range(num): 
    		print(df["PF"][j])
    		if self.ID_finger==df["PF"][j]:
    			self.j=j
    			print(self.j)
    	if self.ID_finger==-1 or self.i!=self.j:
    			self.label_PF_status.configure(text="Invalid ",fg="red")
    	else:
    		self.label_PF_status.configure(text="valid ",fg="green")
    		if self.ID_finger !=-1 and self.ID != False:
    			self.OTP=GSM.GSM_OTP(df["Number"][self.j])
    			print(df["Number"][self.j])
   
    def submit(self):
            self.otp=int(self.OTP_entry.get())
            #self.OTP=12345
            if self.otp==self.OTP:
                    self.label_OTP_status.configure(text="correct",fg="green")
            else:
                    self.label_OTP_status.configure(text="not correct",fg="red")
            if self.otp == self.OTP and self.ID != False and self.ID_finger !=-1:
                            self.master.switch_frame(Vote)
	    		
                    
	    		
######################################################  Registration   ############################################## 

class Registration(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.name_label =tk.Label(self, text="Name:",font=("Helvetica", 15),fg="orange")
        self.name_entry = tk.Entry(self,width = 40 )
        
        
        self.phone_label = tk.Label(self, text="Phone Number",font=("Helvetica", 15),fg="orange")
        self.phone_label_status = tk.Label(self, text="",font=("Helvetica", 15))
        self.phone_entry = tk.Entry(self,width = 40)
        
        
        self.label_button_RFID = tk.Button(self, text="RFID Registration", command=self.RFID,font=("Helvetica", 15),bg="black",fg="white")
        self.lable_RFID_status = tk.Label(self, text="",font=("Helvetica", 15))
        self.label_RFID = tk.Label(self, text="Place user RFID",font=("Helvetica", 15))
        
        
        self.label_PF = tk.Label(self, text="Place your RFID card",font=("Helvetica", 15),fg="green")
        self.label_PF_status = tk.Label(self, text="",font=("Helvetica", 15))
        self.login_button_PF= tk.Button(self, text="Finger Print Registration",command=self.finger_print,font=("Helvetica", 15),bg="black",fg="white")
          
        self.button = tk.Button(self, text="Verify", command=self.take_info,font=("Helvetica", 15),bg="black",fg="white")
        
        
        self.save_button = tk.Button(self, text="Save",font=("Helvetica", 15),command=self.save)
        self.back_button = tk.Button(self, text="Back",font=("Helvetica", 15),command=self.Back)
        self.save_button.configure(state="disabled")
        
        
        
        self.name_label.grid(row=0,column=0)
        self.name_entry.grid(row=0,column=1,pady=30)
        
        self.phone_label.grid(row=1,column=0)
        self.phone_label_status.grid(row=2,column=1,pady=30)
        self.phone_entry.grid(row=1,column=1,)
        
        self.label_RFID.grid(row=3,column=0)
        self.lable_RFID_status.grid(row=3,column=2)
        self.label_button_RFID.grid(row=3,column=1,pady=30)
        
        self.label_PF.grid(row=4,column=0)
        self.label_PF_status.grid(row=4,column=2)
        self.login_button_PF.grid(row=4,column=1,pady=30)
        
        self.button.grid(row=5,column=1,ipadx=100,pady=30)
        self.back_button.grid(row=6,column=0,ipadx=100)
        self.save_button.grid(row=6,column=1,ipadx=100)
        
        
    def take_info(self):
    	self.name=self.name_entry.get()
    	self.phone=self.phone_entry.get()
    	self.Phone(self.phone)
    	
    	if self.phone != "False" and self.RFID != False and self.finger_print !=-1 :
    		self.save_button.configure(state="normal",bg="black",fg="white")
    		
    	
    def	Phone(self,phone):
    	self.flag=main.Phone_numer(phone)
    	if self.flag==False:
    		self.phone_label_status.configure(text="Invalid phone number",fg="red")
    	else:
    		self.phone_label_status.configure(text="phone number is valid",fg="green")
    def RFID(self):	
    	self.ID=main.RFID_I()
    	
    	if self.ID==False:
    		self.lable_RFID_status.configure(text="Invalid RFID",fg="red")
    	else:
    		self.lable_RFID_status.configure(text="Valid RFID",fg="green")
    		
    def finger_print(self):
    	self.ID_finger=main.finger_print_R()
    	if self.ID_finger==-1:
    		self.label_PF_status.configure(text="Invalid figer print",fg="red")
    	else:
    		self.label_PF_status.configure(text="Valid finger print",fg="green")
    		
    def save(self):
    	main.data_update(self.name,self.phone,self.ID,self.ID_finger)
    	self.master.switch_frame(Select)
    	
    def Back(self):
        self.master.switch_frame(Select)
   
    	
    
            
    

#########################################################   select ###############################################        
class Select(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.label = tk.Label(self,text="What do you want to do",font=("Helvetica", 40))
        
        self.select_registration_button = tk.Button(self, text="Click Here to Registration New user", command=self.reg,font=("Helvetica", 20),bg="black",fg="white")
        
        
        self.select_vote_button = tk.Button(self, text="Click Here to Vote", command=self.verify,font=("Helvetica",20),bg="black",fg="white")
        
        self.label.grid(row=0,column=0)
        self.select_registration_button.grid(row=1,column=0,pady=100)
        self.select_vote_button.grid(row=2,column=0)

    def reg(self):
        	self.master.switch_frame(Registration)
        	
    def verify(self):
    		self.master.switch_frame(Verify)
    		
    		
    		
    
        	
###########################################################   Verify  #############################################     	

class Vote(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master  
        self.label = tk.Label(self,text="click a botton to vote",font=("Helvetica", 30))
        self.label.grid(row=0,column=0,pady=100)
        self.vote_option1_button = tk.Button(self, text="BJP", command=self.submit_1,font=("Helvetica",30),bg="black",fg="white")
        
        self.vote_option1_button.grid(row=1,column=0,pady=30)
        
        self.vote_option2_button = tk.Button(self, text="AAP", command=self.submit_1,font=("Helvetica",30),bg="black",fg="white")
        
        self.vote_option2_button.grid(row=2,column=0)
        
        
    def submit_1(self):
        	self.master.switch_frame(Voting_done)
        	
    def submit_2(self):
        	self.master.switch_frame(Vote_not_done)
        	
        	
        	
class Vote_done(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        self.canvas_done = tk.Canvas(self, width=300, height=300)
        self.canvas_done.pack(pady=200)
        self.image2 = tk.PhotoImage(file="11.png")
        self.canvas_done.create_image(0, 0,anchor="nw", image=self.image2,tag="image")
        
        self.label = tk.Label(self, text="You are Verified user, you can vote now ",font=("Helvetica", 35))
        self.label.pack(pady=10)
        
        self.button = tk.Button(self, text="vote", command=self.vote_now)
        self.button.pack(padx=0,pady=10)
        self.button.configure(bg="black", fg="white", font=("Arial", 35))

     
    def vote_now(self):
        	self.master.switch_frame(Vote)
        	
        	
        
        
class Vote_not_done(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        self.canvas_done = tk.Canvas(self, width=300, height=300)
        self.canvas_done.pack(pady=200)
        self.label = tk.Label(self, text="Not Verified user, Sorry you can't vote",font=("Helvetica", 40))
        self.label.pack(pady=10)
        self.image2 = tk.PhotoImage(file="2.png")
        self.canvas_done.create_image(0, 0, anchor="nw",image=self.image2,tag="image")
        
        
        self.button = tk.Button(self, text="Back ", command=self.back)
        self.button.pack(padx=0,pady=10)
        self.button.configure(bg="black", fg="white", font=("Arial", 35))
        
    def back(self):
        	self.master.switch_frame(Verify)
        
    	
    	
    	
    	
class Voting_done(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.canvas_done = tk.Canvas(self, width=300, height=300)
        self.canvas_done.pack(pady=100)
        self.image2 = tk.PhotoImage(file="11.png")
        self.canvas_done.create_image(0, 0,anchor="nw", image=self.image2,tag="image")
         
        self.button = tk.Button(self, text="Vote with new user again", command=self.back)
        self.button.pack(padx=0,pady=10)
        self.button.configure(bg="black", fg="white", font=("Helvetica", 35))
        
        self.button = tk.Button(self, text="Voting done", command=self.done)
        self.button.pack(padx=0,pady=10)
        self.button.configure(bg="red", fg="black", font=("Helvetica", 35))

     
    def back(self):
        	self.master.switch_frame(Verify)
        	
    def done(self):
        	self.master.switch_frame(Select)
        		
app = Voting() 
app.mainloop()

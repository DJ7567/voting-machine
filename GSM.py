import serial
import time
import random

# configure the serial port

ser = serial.Serial('/dev/ttyAMA1', 9600, timeout=1)


def GSM_OTP(num):
	otp=0
	for i in range(4):
		otp = otp +random.randint(1,9)
		otp =otp*10
	msg='OTP '+str(otp)+'\r\n'
	strg='AT+CMGS="'+str(num)+'"\r\n'
	# send an SMS message
	ser.write('AT\r\n'.encode())
	time.sleep(1)
	ser.write('AT+CMGF=1\r\n'.encode())
	time.sleep(1)

	# set SMS mode to text
	ser.write(strg.encode())
	time.sleep(1)# replace PHONE_NUMBER with the recipient's phone number
	
	
	ser.write(msg.encode())
	time.sleep(1)# replace with your message
	ser.write(chr(26).encode()) # send the message (Ctrl+Z)

	# wait for the response
	response = ser.read(1024)

	# print the response
	print(response.decode())
	

GSM_OTP(6353935962)



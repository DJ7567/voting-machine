import serial

ser = serial.Serial('/dev/ttyAMA0', baudrate=9600, timeout=1)
print("started")


ser.write(b'AT+CMGF=1\r\n')
ser.write(b'AT+CMGS="+"918200412217"\r\n')
ser.write(b'Hello, this is a test message.\r\n')
ser.write(chr(26).encode())


# read the response
response = ser.readlines()
for line in response:
    print(line.decode('utf-8').strip())


ser.close()


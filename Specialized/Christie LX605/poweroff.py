import serial
import time

print('Opening connection and sending command')
cmd = 'C01\r'
ser = serial.Serial(
	port='COM1',
	baudrate=19200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
        timeout = 1
)

print(ser.isOpen())
ser.write(bytearray(cmd,'ascii'))
time.sleep(0.5)

while 1:
    data = ser.read(5)
    if len(data) == 0:
        print(data)
        break
    if len(data) > 0:
        print(data)
        break


ser.flush()
print('Closing serial port')
ser.close()
print(ser.isOpen())
print('Done')








import serial

#Opening serial ports
# ser = serial.Serial('COM1',115200,timeout=5)
# print(ser.name)
# ser.write(b'hello')
# ser.close()
#
# with serial.Serial('COM1', 19200, timeout=1) as ser:
#     x = ser.read()          # read one byte
#     s = ser.read(10)        # read up to ten bytes (timeout)
#     line = ser.readline()   # read a '\n' terminated line
#     # line = ser.read_all()
#     print(type(line))

#Configuring ports later
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM1'
print(ser)
print(ser.isOpen())
ser.open()
print(ser.isOpen())

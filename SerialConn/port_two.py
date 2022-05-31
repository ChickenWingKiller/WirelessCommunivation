import serial
import serial.tools.list_ports
import Serial_port
import threading

port2 = Serial_port.Port('COM3', 115200, 0)

def port_write():
    while True:
        s = input()
        port2.write(s + ' ---from COM3')
def port_read():
    while True:
        port2.read()

thread1 = threading.Thread(target=port_write).start()
thread2 = threading.Thread(target=port_read()).start()
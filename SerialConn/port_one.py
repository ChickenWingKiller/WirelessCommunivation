import serial
import serial.tools.list_ports
import Serial_port
import threading

port1 = Serial_port.Port('COM2', 115200, 0)

def port_write():
    while True:
        s = input()
        port1.write(s + ' ---from COM2')
def port_read():
    while True:
        port1.read()

thread1 = threading.Thread(target=port_write).start()
thread2 = threading.Thread(target=port_read()).start()
import serial
import serial.tools.list_ports

class Port():
    def __init__(self, name, bps, timex):
        self.name = name
        self.bps = bps
        self.timex = timex
        self.port = serial.Serial(self.name, self.bps, timeout=self.timex)

    def view_all_ports(self):
        print('-----------------')
        print('查看全部可用串口')
        port_list = list(serial.tools.list_ports.comports())
        print(port_list)
        if len(port_list) == 0:
            print('无串口可用')
        else:
            for i in range(len(port_list)):
                print(port_list[i])
    def test(self):
        print(1)

    def init_port(self):
        return self.port

    def close_port(self):
        self.port.close()

    def write(self, data):
        result = self.port.write(str(data).encode("gbk"))
        return result

    def read(self):
        data = self.port.readall()
        if len(data) != 0:
            print('\n' + data.decode('gbk'))

    def writeBinary(self, data):
        result = self.port.write(data)
        return result

    def readBinary(self):
        data = self.port.readall()
        return data

if __name__ == '__main__':
    # port1 = Port('COM2', 115200, 0)
    # port2 = Port('COM3', 115200, 0)
    # port1.write(123)
    # port2.read()
    Port.view_all_ports(Port)
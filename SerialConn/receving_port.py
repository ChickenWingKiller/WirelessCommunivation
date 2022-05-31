import Serial_port
import threading
import process_data

name = 'COM2'
bps = 115200
timex = 0
receving_port = Serial_port.Port(name, bps, timex)

if __name__ == '__main__':
    # receive_data = receving_port.readBinary()
    #
    # print('原数据：', receive_data)
    # print('经gbk解码后：', int(receive_data.decode('gbk')))
    # print('原数据第一位：', receive_data[0])
    # print('原数据第一位的类型：', type(receive_data[0]))
    # print('原数据bytes转换为整数类型：', hex(int.from_bytes(receive_data, byteorder='big')))
    # data_list = [i for i in receive_data]
    # print(data_list)

    # send_data = b'123'
    # receving_port.writeBinary(send_data)
    # receving_port.write(123)

    processor = process_data.DataProcessor()
    while True:
        data = receving_port.readBinary()
        if (len(data) != 0):
            # print(data[0])
            processor.processing(data)

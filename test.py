import serial
import serial.tools.list_ports
# 串口通信是指外设和计算机间，通过数据信号线 、地线、控制线等，按位进行传输数据的一种通讯方式。这种通信方式使用的数据线少，在远距离通信中可以节约通信成本，但其传输速度比并行传输低。串口是计算机上一种非常通用的设备通信协议。pyserial模块封装了python对串口的访问，为多平台的使用提供了统一的接口。

# print('-----------------')
# print('获取可用串口列表')
# port_list = list(serial.tools.list_ports.comports())
# print(port_list)
# if len(port_list) == 0:
#     print('无串口可用')
# else:
#     for i in range(len(port_list)):
#         print(port_list[i])

# print('-----------------')
# print('发送端串口程序实现:')
# try:
#     portx = 'COM2'  # 端口
#     bps = 115200  # 波特率
#     timex = 0  # 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
#     ser = serial.Serial(portx, bps, timeout=timex)  # 打开串口，并得到串口对象
#     # print('type(ser):', type(ser))
#     # print('ser: ', ser)
#     # while True:
#     #     result = ser.write('串口通信'.encode('gbk'))
#     result = ser.write('123'.encode('utf-8'))
#     print('写总字节数：', result)
#     # line = ser.readall()
#     # print(type(line))
#     # print(line)
#     ser.close()
#
# except Exception as e:
#     print('异常：', e)

# print('-----------------')
# print('接收端串口程序实现:')
# try:
#     port2 = 'COM2'
#     bps = 115200
#     time2 = 0
#     ser = serial.Serial(port2, bps, timeout=time2)
#     while True:
#         result = ser.readall()
#         if len(result) != 0:
#             print(result.decode('gbk'))
#     # result = ser.readall()
#     # print(result)
# except Exception as e:
#     print('异常：', e)
#
# ser = None
# def openPort():
#     port2 = 'COM2'
#     bps = 115200
#     time2 = 0
#     global ser
#     ser = serial.Serial(port2, bps, timeout=time2)
# def receive_data():
#     print(ser.readall())

# print('-----------------')
# print('十六进制处理')
# try:
#     portx = 'COM3'
#     bps = 115200
#     timex = 1
#     ser = serial.Serial(portx, bps, timeout=timex)
#     # receive_data = ser.readall()
#     # print(len(receive_data))
#     # print(receive_data)
#     # 十六进制的发送
#     result = ser.write(chr(0x06).encode('utf-8'))  # 写数据
#     print('写总字节数：', result)
#
# #     # 十六进制的读取
#     porty = 'COM2'
#     bps = 115200
#     timex = 1
#     ser2 = serial.Serial(porty, bps, timeout=timex)
#     print(ser2.read().hex())  # 读一个字节
#     # print(len(ser2.read().hex()))
# #     print('hello')
# #
#     ser.close()
# except Exception as e:
#     print('异常：', e)

# print('-----------------')
# print('收发数据')
# portx = 'COM3'
# bps=115200
# # bps=128000
# timex=0
# ser = serial.Serial(portx, bps, timeout=timex)  # 打开串口，并得到串口对象
# while 1:
#     str = input('请输入要发送的数据（非中文)并同时接收数据：')
#     ser.write((str+'\n').encode('gbk'))
#     print(ser.readline())
# while 1:
#     result = ser.read()
#     result = ser.read()
#     if result != b'':
#         print(result)
#         print(result.hex())
#         print(type(result))
#         print(result == 0x5A)
#     print(result)
# res = ser.readall()
# print(res)
# print(type(res))
# print(ord(res))
# ser.close()

# print('-----------------')
# print('python端两个串口互相通信')
# port1 = 'COM2'
# port2 = 'COM3'
# bps = 115200
# timex = 0
# sender = serial.Serial(port1, bps, timeout=timex)
# receiver = serial.Serial(port2, bps, timeout=timex)
# while 1:
#     str = input('sender输入：')
#     sender.write((str+'\n').encode('gbk'))
#     print('receiver接收：' + receiver.readall().decode('gbk'))
#     print(ord(receiver.read()))

print(90==0x5a)
print(b'a'[0])
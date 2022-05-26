import serial
import serial.tools.list_ports

# print('简单串口程序实现:')
# try:
#     portx = 'COM3'  # 端口
#     bps = 115200  # 波特率
#     timex = 2  # 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
#     ser = serial.Serial(portx, bps, timeout=timex)  # 打开串口，并得到串口对象
#
#     result = ser.write('串口通信'.encode('gbk'))
#     print('写总字节数：', result)
#     # ser.close()  # 关闭串口
#     line = ser.readall()
#     print(type(line))
#     # ser1 = serial.Serial()
#     ser.close()
#
# except Exception as e:
#     print('异常：', e)
# print(type(result))
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
# print('十六进制处理')
# try:
#     portx = 'COM3'
#     bps = 115200
#     timex = 1
#     ser = serial.Serial(portx, bps, timeout=timex)
#     print('串口详情参数：', ser)
#
#     # 十六进制的发送
#     result = ser.write(chr(0x06).encode('utf-8'))  # 写数据
#     print('写总字节数：', result)
#
#     # 十六进制的读取
#     print(ser.read().hex())  # 读一个字节
#     print('hello')
#
#     ser.close()
# except Exception as e:
#     print('异常：', e)

print('-----------------')
print('收发数据')
portx = 'COM3'
bps=115200
# bps=128000
timex=0
ser = serial.Serial(portx, bps, timeout=timex)  # 打开串口，并得到串口对象
# while 1:
#     str = input('请输入要发送的数据（非中文)并同时接收数据：')
#     ser.write((str+'\n').encode('gbk'))
#     print(ser.readline())
while 1:
    result = ser.read()
    # result = ser.read()
    if result != b'':
        print(result)
        print(result.hex())
        # print(type(result))
        # print(result == 0x5A)
    # print(result)
# res = ser.readall()
# print(res)
# print(type(res))
# print(ord(res))
ser.close()

# print('-----------------')
# print('python端两个串口互相通信')
# port1 = 'COM3'
# port2 = 'COM6'
# bps = 115200
# timex = 0
# sender = serial.Serial(port1, bps, timeout=timex)
# receiver = serial.Serial(port2, bps, timeout=timex)
# while 1:
#     str = input('sender输入：')
#     sender.write((str+'\n').encode('gbk'))
#     print('receiver接收：' + receiver.readall().decode('gbk'))
    # sender.write(str)
    # print('receiver接收：' + receiver.readall())
    # print(ord(receiver.read()))
ser2.close()
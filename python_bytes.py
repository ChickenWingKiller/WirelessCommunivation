# b1 = bytes() #通过构造函数创建空 bytes
# b2 = b'' #通过空字符串创建空 bytes
# b3 = b'abc' #通过b前缀将字符串转换成 bytes
# b3 = b'http://c.biancheng.net/python/'
# print("b3: ", b3)
# print(b3[3])
# print(b3[7:22])
# print('--------------------')
# b4 = bytes('我是李岳峰'.encode('UTF-8')) #为 bytes() 方法指定字符集
# print('b4:', b4)
# b5 = '我是李岳峰'.encode('UTF-8')
# print('b5:',b5[0])
# print('你好'.encode('UTF-8'))
# print('你好'.encode('gbk'))
# b = bytes()
b = b'1'
print(str(b)[0])
print(b)
print(b[0])
print(bin(b[0]))
print(hex(b[0]))
i = 97
print(i.to_bytes(2, byteorder='big'))
int_list = [1, 2, 3]
print(bytes(int_list))
for i in bytes(int_list):
    print(i)
print(type(b'\x01\x02\x03'))
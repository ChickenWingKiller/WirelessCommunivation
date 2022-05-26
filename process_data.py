class DataProcessor():
    def __init__(self):
        self.start_byte = 0x5a
        self.start_point_count = 0
        self.start_flag = False
        self.end_byte = 0x7e
        self.end_point_count = 0
        self.end_flag = False
        self.last_byte = 0
        self.data_buffer = []
        self.valid_data = []
        self.package_count = 0

    def determine_start(self, num):
        if num == self.start_byte:
            if self.last_byte == self.start_byte:
                # if self.start_point_count == 0:
                #     self.start_point_count += 1
                #     self.last_byte = num
                if self.start_point_count == 3:
                    self.start_flag = True
                    self.start_point_count = 0
                else:
                    self.start_point_count += 1
                    # self.last_byte = num
            else:
                # self.last_byte = num
                self.start_point_count = 1

    def determine_end(self, num):
        if num == self.end_byte and self.start_flag:
            if self.last_byte == self.end_byte:
                # if self.end_point_count == 0:
                #     self.end_point_count += 1
                #     self.last_byte = num
                if self.end_point_count == 3 and self.start_flag:
                    self.end_flag = True
                    self.end_point_count = 0
                else:
                    self.end_point_count += 1
                    # self.last_byte = num
            else:
                # self.last_byte = num
                self.end_point_count = 1

    def processing(self, byte):
        num = byte[0]
        self.determine_start(num)
        self.determine_end(num)
        # 已经开始接收数据
        if self.start_flag and (not self.end_flag):
            self.data_buffer.append(num)
        # 尚未开始接收数据
        elif (not self.start_flag) and (not self.end_flag):
            pass
        # 数据接收完成
        elif self.start_flag and self.end_flag:
            self.package_count += 1
            print('----------------------------')
            print('第%d个数据包接收完成' % self.package_count)
            return self.data_buffer
        self.last_byte = num


if __name__ == '__main__':
    data_processor = DataProcessor()
    type_in = 0
    byte = b''
    while True:
        type_in = int(input())
        byte = b

import random
from PyQt5.QtCore import QThread


# import system_ui

def box1_data():
    data = []
    # data_type = ['温度','箱外压力','氮气浓度','湿度','箱内外压力差（倍数）','四氧化二氮浓度','箱内压力','电池电量','一甲基肼浓度']
    # for type in data_type:
    #     data[type] = random.randint(1,100)
    for i in range(9):
        data.append(random.randint(1, 10))
    return data


def box2_data():
    data = []
    for i in range(9):
        data.append(random.randint(1, 10))
    return data


def box3_data():
    data = []
    for i in range(9):
        data.append(random.randint(1, 10))
    return data


def box4_data():
    data = []
    for i in range(9):
        data.append(random.randint(1, 10))
    return data


def box5_data():
    data = []
    for i in range(9):
        data.append(random.randint(1, 10))
    return data


def box6_data():
    data = []
    for i in range(9):
        data.append(random.randint(1, 10))
    return data


def send_data():
    data = []
    data.append(box1_data())
    data.append(box2_data())
    data.append(box3_data())
    data.append(box4_data())
    data.append(box5_data())
    data.append(box6_data())
    return data

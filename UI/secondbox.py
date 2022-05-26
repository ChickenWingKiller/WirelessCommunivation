# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondbox.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import random

# from UI import dataSender
import dataSender


class Ui_Box1_Window(object):
    '''
    温度：label_5
    箱外压力：label_6
    氮气浓度：label_7
    湿度：label_8
    箱内外压力差（倍数）：label_9
    四氧化二氮浓度：label_10
    箱内压力：label_11
    电池电量：label_12
    一甲基浓度：label_13
    '''

    def __init__(self):
        self.labels = ['温度', '箱外压力', '氮气浓度', '湿度', '箱内外压力差(倍数)', '四氧化二氮浓度', '箱内压力', '电池电量', '一甲基肼浓度']
        self.pass_intervals = [[0, 7], [0, 7], [0, 7], [0, 7], [0, 7], [0, 7], [0, 7], [0, 7], [0, 7]]

    def setupUi(self, Box1_Window):
        Box1_Window.setObjectName("Box1_Window")
        Box1_Window.resize(1920, 1200)
        Box1_Window.setStyleSheet("background-color: rgb(21, 32, 42);")
        self.centralwidget = QtWidgets.QWidget(Box1_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1921, 111))
        self.frame.setStyleSheet("background-color: rgb(25, 104, 179);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("image: url(:/jpg/images/logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(50, 180, 1801, 991))
        self.frame_2.setStyleSheet("color: rgb(140, 192, 222);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(120, 40, 301, 101))
        self.label_4.setObjectName("label_4")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(120, 180, 1621, 561))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(60)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setStyleSheet("*{background-color: rgb(255, 255, 255);\n"
"border-left: 20px solid rgb(140, 192, 222);\n"
"color: rgb(0, 0, 0);}")
        self.label_6.setIndent(40)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-left: 20px solid rgb(140, 192, 222);")
        self.label_11.setIndent(40)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-left: 20px solid rgb(140, 192, 222);")
        self.label_7.setIndent(40)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setEnabled(True)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setAutoFillBackground(False)
        self.label_12.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-left: 20px solid rgb(140, 192, 222);")
        self.label_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_12.setLineWidth(1)
        self.label_12.setScaledContents(False)
        self.label_12.setIndent(40)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-left: 20px solid rgb(140, 192, 222);")
        self.label_9.setIndent(40)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setStyleSheet("*{background-color: rgb(255, 255, 255);\n"
"border-left: 20px solid rgb(140, 192, 222);\n"
"color: rgb(0, 0, 0);}")
        self.label_8.setIndent(40)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-left: 20px solid rgb(140, 192, 222);")
        self.label_10.setIndent(40)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-left: 20px solid rgb(140, 192, 222);")
        self.label_13.setIndent(40)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setBaseSize(QtCore.QSize(0, 0))
        self.label_5.setStyleSheet("*{background-color: rgb(255, 255, 255);\n"
"border-left: 20px solid rgb(140, 192, 222);\n"
"color: rgb(0, 0, 0);}")
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_5.setLineWidth(1)
        self.label_5.setMidLineWidth(0)
        self.label_5.setIndent(40)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(730, 870, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(140, 192, 222);\n"
"color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(1450, 60, 271, 81))
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        Box1_Window.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.back) #返回主界面的button

        self.datetime = QtCore.QDateTime()
        self.timeTimer = QtCore.QTimer()
        self.dataTimer = QtCore.QTimer()
        self.timeTimer.timeout.connect(self.show_time)
        self.dataTimer.timeout.connect(self.receive_data)
        self.timeTimer.start(1000)
        self.dataTimer.start(2000)

        self.retranslateUi(Box1_Window)
        QtCore.QMetaObject.connectSlotsByName(Box1_Window)

    def receive_data(self):
        box2Data = dataSender.send_data()[1]
        label_list = [self.label_5, self.label_6, self.label_7, self.label_8, self.label_9, self.label_10,
                      self.label_11, self.label_12, self.label_13]
        abnormal = False
        for i in range(len(box2Data)):
            label_list[i].setText(
                "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">" + self.labels[
                    i] + ':' + str(
                    box2Data[i]) + "</span></p></body></html>")
            if (box2Data[i] > self.pass_intervals[i][0]) and (box2Data[i] < self.pass_intervals[i][1]):
                label_list[i].setStyleSheet("*{background-color: rgb(255, 163, 163);\n"
                                            "border-left: 20px solid rgb(206, 0, 0);\n"
                                            "color: rgb(0, 0, 0);}")
            else:
                abnormal = True
                label_list[i].setStyleSheet("*{background-color: rgb(255, 255, 255);\n"
                                            "border-left: 20px solid rgb(140, 192, 222);\n"
                                            "color: rgb(0, 0, 0);}")
        if abnormal:
            self.label_14.setText("<html><head/><body><p><span style=\" font-size:48pt; font-weight:600; color:#f01111;\">异常</span></p></body></html>")
            self.label_14.setStyleSheet("background-color: rgb(255, 163, 163);")
        else:
            self.label_14.setText("<html><head/><body><p><span style=\" font-size:48pt; font-weight:600; color:#ffffff;\">运行正常</span></p></body></html>")
            self.label_14.setStyleSheet("background-color: rgb(21, 32, 42);")

    # def receive_data(self):
    #     data = dataSender.send_data()
    #     for i in range(len(data[0])):
    #         temp = data[0][i]
    #         if temp:
    #             if i == 0:
    #                 self.label_5.setStyleSheet("*{background-color: rgb(255, 163, 163);\n"
    #                                            "border-left: 20px solid rgb(206, 0, 0);\n"
    #                                            "color: rgb(0, 0, 0);}")
    #             elif i == 1:
    #                 self.label_6.setStyleSheet("*{background-color: rgb(255, 163, 163);\n"
    #                                            "border-left: 20px solid rgb(206, 0, 0);\n"
    #                                            "color: rgb(0, 0, 0);}")
    #             elif i == 2:
    #                 self.label_7.setStyleSheet("*{background-color: rgb(255, 163, 163);\n"
    #                                            "border-left: 20px solid rgb(206, 0, 0);\n"
    #                                            "color: rgb(0, 0, 0);}")
    #             elif i == 3:
    #                 self.label_8.setStyleSheet("*{background-color: rgb(255, 163, 163);\n"
    #                                            "border-left: 20px solid rgb(206, 0, 0);\n"
    #                                            "color: rgb(0, 0, 0);}")
    #             elif i == 4:
    #                 self.label_9.setStyleSheet("*{background-color: rgb(255, 163, 163);\n"
    #                                            "border-left: 20px solid rgb(206, 0, 0);\n"
    #                                            "color: rgb(0, 0, 0);}")
    #             elif i == 5:
    #                 self.label_10.setStyleSheet("*{background-color: rgb(255, 163, 163);\n"
    #                                            "border-left: 20px solid rgb(206, 0, 0);\n"
    #                                            "color: rgb(0, 0, 0);}")
    #             elif i == 6:
    #                 self.label_11.setStyleSheet("*{background-color: rgb(255, 163, 163);\n"
    #                                            "border-left: 20px solid rgb(206, 0, 0);\n"
    #                                            "color: rgb(0, 0, 0);}")
    #             elif i == 7:
    #                 self.label_12.setStyleSheet("*{background-color: rgb(255, 163, 163);\n"
    #                                            "border-left: 20px solid rgb(206, 0, 0);\n"
    #                                            "color: rgb(0, 0, 0);}")
    #             else:
    #                 self.label_13.setStyleSheet("*{background-color: rgb(255, 163, 163);\n"
    #                                            "border-left: 20px solid rgb(206, 0, 0);\n"
    #                                            "color: rgb(0, 0, 0);}")

    def show_time(self):
        text = self.datetime.currentDateTime().toString(QtCore.Qt.DefaultLocaleLongDate)
        self.label_3.setText("<html><head/><body><p><span style=\" font-size:13pt; font-weight:200; color:#ffffff;\">" + text + "</span></p></body></html>")

    def back(self):
        pass

    def retranslateUi(self, Box1_Window):
        _translate = QtCore.QCoreApplication.translate
        Box1_Window.setWindowTitle(_translate("Box1_Window", "MainWindow"))
        self.label_2.setText(_translate("Box1_Window", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">贮运设备环境参数监测显示系统</span></p></body></html>"))
        self.label_3.setText(_translate("Box1_Window", "<html><head/><body><p><span style=\" font-size:13pt; font-weight:200; color:#ffffff;\">(获取系统时间中...)</span></p></body></html>"))
        self.label_4.setText(_translate("Box1_Window", "<html><head/><body><p><span style=\" font-size:60pt; font-weight:792;\">02</span><span style=\" font-size:30pt; font-weight:96;\">号 贮运箱</span></p></body></html>"))
        self.label_6.setText(_translate("Box1_Window", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">箱外压力：</span></p></body></html>"))
        self.label_11.setText(_translate("Box1_Window", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">箱内压力：</span></p></body></html>"))
        self.label_7.setText(_translate("Box1_Window", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">氮气浓度：</span></p></body></html>"))
        self.label_12.setText(_translate("Box1_Window", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">电池电量：</span></p></body></html>"))
        self.label_9.setText(_translate("Box1_Window", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">箱内外压力差（倍数）：</span></p></body></html>"))
        self.label_8.setText(_translate("Box1_Window", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">湿度：</span></p></body></html>"))
        self.label_10.setText(_translate("Box1_Window", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">四氧化二氮浓度：</span></p></body></html>"))
        self.label_13.setText(_translate("Box1_Window", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">一甲基浓度：</span></p></body></html>"))
        self.label_5.setText(_translate("Box1_Window", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">温度：</span></p></body></html>"))
        self.pushButton.setText(_translate("Box1_Window", "返回"))
        self.label_14.setText(_translate("Box1_Window", "<html><head/><body><p><span style=\" font-size:48pt; font-weight:600; color:#ffffff;\">运行正常</span></p></body></html>"))
import images_box_rc

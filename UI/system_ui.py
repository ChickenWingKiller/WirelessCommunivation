from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import mainWindow, firstbox, secondbox, thirdbox, fourthbox, fifthbox, sixthbox
import dataSender


class mainui(mainWindow.Ui_MainWindow):
    def open1(self):
        # label_5 - label_13
        self.timeTimer.stop()
        self.dataTimer.stop()
        box1_ui.setupUi(MainWindow)

    def open2(self):
        self.timeTimer.stop()
        self.dataTimer.stop()
        box2_ui.setupUi(MainWindow)

    def open3(self):
        self.timeTimer.stop()
        self.dataTimer.stop()
        box3_ui.setupUi(MainWindow)

    def open4(self):
        self.timeTimer.stop()
        self.dataTimer.stop()
        box4_ui.setupUi(MainWindow)

    def open5(self):
        self.timeTimer.stop()
        self.dataTimer.stop()
        box5_ui.setupUi(MainWindow)

    def open6(self):
        self.timeTimer.stop()
        self.dataTimer.stop()
        box6_ui.setupUi(MainWindow)


class box1ui(firstbox.Ui_Box1_Window):
    def back(self):
        self.timeTimer.stop()
        self.dataTimer.stop()
        main_ui.setupUi(MainWindow)


class box2ui(secondbox.Ui_Box1_Window):
    def back(self):
        self.timeTimer.stop()
        self.dataTimer.stop()
        main_ui.setupUi(MainWindow)


class box3ui(thirdbox.Ui_Box1_Window):
    def back(self):
        self.timeTimer.stop()
        self.dataTimer.stop()
        main_ui.setupUi(MainWindow)


class box4ui(fourthbox.Ui_Box1_Window):
    def back(self):
        self.timeTimer.stop()
        self.dataTimer.stop()
        main_ui.setupUi(MainWindow)


class box5ui(fifthbox.Ui_Box1_Window):
    def back(self):
        self.timeTimer.stop()
        self.dataTimer.stop()
        main_ui.setupUi(MainWindow)


class box6ui(sixthbox.Ui_Box1_Window):
    def back(self):
        self.timeTimer.stop()
        self.dataTimer.stop()
        main_ui.setupUi(MainWindow)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
    main_ui = mainui()  # 创建主界面的窗体对象
    box1_ui = box1ui()  # 创建贮运箱1号的窗体对象
    box2_ui = box2ui()  # 创建贮运箱2号的窗体对象
    box3_ui = box3ui()  # 创建贮运箱3号的窗体对象
    box4_ui = box4ui()  # 创建贮运箱4号的窗体对象
    box5_ui = box5ui()  # 创建贮运箱5号的窗体对象
    box6_ui = box6ui()  # 创建贮运箱6号的窗体对象
    main_ui.setupUi(MainWindow)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
    MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程

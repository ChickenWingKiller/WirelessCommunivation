from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import mainwinodw
import box1

class mainui(mainwinodw.Ui_Main):
    # def function(self):
    #     self.pushButton.clicked.connect(self.open)

    def open(self):
        # print(123)
        # self.m = box1ui()
        # self.m.setupUi(MainWindow)
        box1_ui.setupUi(MainWindow)
        # self.m = box1ui()
        # self.m.setupUi(MainWindow)


class box1ui(box1.Ui_box1_objectName):
    def back(self):
        main_ui.setupUi(MainWindow)
        # self.m = mainui()
        # self.m.setupUi(MainWindow)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
    main_ui = mainui()  # 创建PyQt设计的窗体对象
    box1_ui = box1ui()
    main_ui.setupUi(MainWindow)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
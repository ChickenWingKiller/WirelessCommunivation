# from PyQt5 import QtCore, QtGui, QtWidgets
# import sys
# from UI import fristbox
# from UI import mainWindow
#
# if __name__ == '__main__':
#
#     while(True):
#         flag = int(input())
#         if (flag == 1):
#             app = QtWidgets.QApplication(sys.argv)
#             MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
#             # MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
#             ui = fristbox.Ui_MainWindow()  # 创建PyQt设计的窗体对象
#             ui.setupUi(MainWindow)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
#             # MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
#             MainWindow.show()  # 显示窗体
#             sys.exit(app.exec_())  # 程序关闭时退出进程
#         else:
#             app = QtWidgets.QApplication(sys.argv)
#             MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
#             # MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
#             ui = mainWindow.Ui_MainWindow()  # 创建PyQt设计的窗体对象
#             ui.setupUi(MainWindow)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
#             # MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
#             MainWindow.show()  # 显示窗体
#             sys.exit(app.exec_())  # 程序关闭时退出进程

import sys
from PyQt5.QtWidgets import *
import time

class WinForm(QWidget):
    def __init__(self, parent = None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('实时刷新页面例子')
        self.listFile = QListWidget()
        self.btnStart = QPushButton('开始')
        layout = QGridLayout(self)
        layout.addWidget(self.listFile, 0, 0, 1, 2)
        layout.addWidget(self.btnStart, 1, 1)

        self.btnStart.clicked.connect(self.slotAdd)
        self.setLayout(layout)

    def slotAdd(self):
        for n in range(10):
            str_n = 'file index {0}'.format(n)
            self.listFile.addItem(str_n)
            QApplication.processEvents()
            time.sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())

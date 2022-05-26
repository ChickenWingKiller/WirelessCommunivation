from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import main,box1
import random

class mainui(main.Ui_MainWindow):
    def showBox1(self):
        box1Ui.setupUi(MainWindow)
class box1ui(box1.Ui_MainWindow):
    def back(self):
        mainUi.setupUi(MainWindow)
        # self.timer.stop()
    # def func(self):
    #     temp = random.randint(0, 10)
    #     print(temp)
    #     self.label.setText(
    #         "<html><head/><body><p><span style=\" font-size:28pt;\">温度：" + str(temp) + "</span></p></body></html>")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    mainUi = mainui()
    # mainUi = main.Ui_MainWindow()
    box1Ui = box1ui()
    # box1Ui = box1.Ui_MainWindow()
    mainUi.setupUi(MainWindow)
    # box1Ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
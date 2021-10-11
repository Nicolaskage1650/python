from demo import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

def b1_clicked():
   print ("Button 1 clicked")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.RTX_BUTTON.clicked.connect(b1_clicked)
    MainWindow.show()
    sys.exit(app.exec_())

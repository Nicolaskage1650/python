from PyQt5 import QtCore, QtGui, QtWidgets
from demo import Ui_MainWindow
ui = None
def b1_clicked():
   print ("Button 1 clicked")
   name = ui.input_name.text()
   print(name)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    # class ui start
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.RTX_BUTTON.clicked.connect(b1_clicked)
    
    # class ui end
    MainWindow.show()
    sys.exit(app.exec_())

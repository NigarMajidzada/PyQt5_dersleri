import  sys

from PyQt5 import QtWidgets

def  Pencere():
    app=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("PyQT5  Ders1")
    pencere.show()

    sys.exit(app.exec())

Pencere()

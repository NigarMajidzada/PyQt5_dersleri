import  sys

from PyQt5 import QtWidgets,QtGui

def  Pencere():
    app=QtWidgets.QApplication(sys.argv)
    okay=QtWidgets.QPushButton("Tamam")
    cancel=QtWidgets.QPushButton("Iptal")

    h_box=QtWidgets.QHBoxLayout()

    h_box.addWidget(okay)
    h_box.addWidget(cancel)
    h_box.addStretch()
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("PyQT5  Ders4")

    pencere.setLayout(h_box)

    pencere.setGeometry(100,100,500,500)
    pencere.show()

    sys.exit(app.exec())

Pencere()

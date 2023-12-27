import  sys

from PyQt5 import QtWidgets,QtGui

def  Pencere():
    app=QtWidgets.QApplication(sys.argv)

    pencere=QtWidgets.QWidget()

    button=QtWidgets.QPushButton(pencere)
    button.setText("Burasi bir butondur")
    etiket=QtWidgets.QLabel(pencere)
    etiket.setText("Merhaba Dunya")
    etiket.move(200,50)
    button.move(180,100)

    pencere.setWindowTitle("PyQT5  Ders3")

    pencere.setGeometry(100,100,500,500)
    pencere.show()

    sys.exit(app.exec())

Pencere()

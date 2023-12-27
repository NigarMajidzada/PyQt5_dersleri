import  sys

from PyQt5 import QtWidgets,QtGui

def  Pencere():
    app=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("PyQT5  Ders2")
    etiket1=QtWidgets.QLabel(pencere)
    etiket2=QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("Logo.png"))
    etiket1.setText("Burasi bir yazidir")
    etiket1.move(200,30)
    etiket2.move(170,50)
    pencere.setGeometry(100,100,500,500)
    pencere.show()

    sys.exit(app.exec())

Pencere()

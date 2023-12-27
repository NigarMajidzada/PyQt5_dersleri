import  sys

from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()
    def init_ui(self):

        self.yazi_alani=QtWidgets.QLabel("Bana henuz tiklanmadi")
        self.button=QtWidgets.QPushButton("Bana tikla")
        self.say=0


        v_box  =QtWidgets.QVBoxLayout()

        v_box.addWidget(self.button)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()

        self.setLayout(v_box)
        self.show()

app=QtWidgets.QApplication(sys.argv)
pencere1=Pencere()
sys.exit(app.exec_())

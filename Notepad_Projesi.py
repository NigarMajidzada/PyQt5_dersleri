import sys
import os

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout

from PyQt5.QtWidgets import QAction,qApp,QMainWindow

class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.yazi_alani=QTextEdit()
        self.temizle=QPushButton("Temizle")
        self.ac=QPushButton("Ac")
        self.kaydet=QPushButton("Kaydet")


        h_box=QHBoxLayout()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)


        v_box=QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.setWindowTitle("Notepad")
        self.temizle.clicked.connect(self.yaziyi_temizle)
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)


    def yaziyi_temizle(self):
        self.yazi_alani.clear()

    def dosya_ac(self):
        dosya_ismi=QFileDialog.getOpenFileName(self,"dosya ac",os.getenv("HOME"))

        with open(dosya_ismi[0],'r') as file:
            self.yazi_alani.setText(file.read())

    def dosya_kaydet(self):
        dosya_ismi=QFileDialog.getSaveFileName(self,"dosya_kaydet",os.getenv("HOME"))

        with open(dosya_ismi[0],'w') as file:
            file.write(self.yazi_alani.toPlainText())


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.pencere=Notepad()
        self.setCentralWidget(self.pencere)

        self.menuleri_olustur()
    def menuleri_olustur(self):
        menubar=self.menuBar()

        dosya=menubar.addMenu("Dosya")
        dosya_ac=QAction("dosya ac",self)
        dosya_ac.setShortcut("Ctrl+a")

        dosya_kaydet=QAction("dosya kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+k")

        temizle=QAction("temizle",self)
        temizle.setShortcut("Ctrl+t")

        cikis=QAction("cikis",self)
        cikis.setShortcut("Ctrl+c")



        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(temizle)
        dosya.addAction(cikis)

        dosya.triggered.connect(self.response)

        self.setWindowTitle("Metin editoru")
        self.show()


    def response(self,action):

        if action.text()=="dosya ac":
            self.pencere.dosya_ac()
        elif action.text()=="dosya kaydet":
            self.pencere.dosya_kaydet()
        elif action.text()=="temizle":
            self.pencere.yaziyi_temizle()
        elif action.text()=="cikis":
            qApp.quit()



app=QApplication(sys.argv)
menu=Menu()

sys.exit(app.exec_())

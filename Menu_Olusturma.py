import  sys
from PyQt5.QtWidgets import  QApplication,QAction,qApp,QMainWindow

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        menubar=self.menuBar()
        dosya=menubar.addMenu("Dosya")
        dosya_ac=QAction("Dosya ac",self)
        dosya_ac.setShortcut("Ctrl+0")

        dosya_kaydet=QAction("Dosya kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+k")

        cikis=QAction("Cikis",self)
        cikis.setShortcut("Ctrl+a")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cikis)



        duzenle=menubar.addMenu("Duzenle")


        ara_ve_degistir=duzenle.addMenu("ara ve degistir")
        ara=QAction("Ara",self)
        degistir=QAction("Degistir",self)
        temizle=QAction("Temizle",self)
        duzenle.addAction(temizle)

        cikis.triggered.connect(self.cikis_yap)
        dosya.triggered.connect(self.response)


        ara_ve_degistir.addAction(ara)
        ara_ve_degistir.addAction(degistir)


        self.setWindowTitle("Menuler")
        self.show()

    def cikis_yap(self):
        app.quit()
    def response(self,action):
        if action.text()=="Dosya ac":
            print("Dosya ac-a basildi")
        elif action.text()=="Dosya kaydet":
            print("Dosya kaydet-e basildi")
        elif action.text()=="Cikis":
            print("Cikis-a basildi")



app=QApplication(sys.argv)

menu=Menu()
sys.exit(app.exec_())

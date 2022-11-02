
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from main import Ui_MainWindow
import sys
import os

class Invocador(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Invocador, self).__init__(parent)
        self.setupUi(self)
        self.show()
        self.btn_azul.clicked.connect(self.azul)
        self.btn_reutilizar.clicked.connect(self.reutilizar)
        self.pushButton_3.clicked.connect(self.no_aprovechables)
        self.btn_Estadisticas.clicked.connect(self.estadisticas)

    def reutilizar(self):
        #abrir el siguiente link 'https://co.pinterest.com/search/pins/?rs=ac&len=2&q=reciclables%20manualidades&eq=reciclab&etslf=58200'
        import webbrowser
        webbrowser.open('https://co.pinterest.com/search/pins/?rs=ac&len=2&q=reciclables%20manualidades&eq=reciclab&etslf=58200')
    

    def no_aprovechables(self):
        from PIL import Image
        img = Image.open("/home/juancastro/reciclapp/restos de comida(1).png")
        img.show()

    def azul(self):
        #abrir una imagen con PIL
        from PIL import Image
        img = Image.open("/home/juancastro/reciclapp/fondo_1.2.jpg")
        img.show()

    def estadisticas(self):
        from PIL import Image
        import webbrowser
        img = Image.open("/home/juancastro/reciclapp/mapa.png")
        img.show()
        webbrowser.open('/home/juancastro/reciclapp/Report.html')

        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    invocador = Invocador()
    invocador.show()
    sys.exit(app.exec_())

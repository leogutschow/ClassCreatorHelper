from UI.raws.PythonUI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
import os

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.class_name = self.ClassNameEdit
        self.new_func = self.NewFunction.clicked.connect()
        self.new_attr = self.NewAttribute.clicked.connect()
        self.create_class = self.CreateClass.clicked.connect()

        #Dicionário para armazenar as informações da classes, funções e seus atributos
        class_creator = {}

    

        

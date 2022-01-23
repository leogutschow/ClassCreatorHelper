from contextlib import AbstractAsyncContextManager
from re import A
from UI.raws.PythonUI import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QFrame
import os

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.class_name = self.ClassNameEdit
        self.NewFunction.clicked.connect(self.new_func)
        self.NewAttribute.clicked.connect(self.new_attr)
        # self.create_class = self.CreateClass.clicked.connect()

        #Dicionário para armazenar as informações da classes, funções e seus atributos

        self.class_creator = {
            'class': {
                'name': None,
                'functions': {
                    'function1': {
                        'type': None,
                        'name': None,
                        'attrs': {
                            'attr1': None
                        }
                    }
                }   
            }
        }

    #Cria um novo Frame na Janela de UI para uma nova função ser inserida
    def new_func(self):

        #Conta o número de funções já existentes
        functions_count = len(self.class_creator['class']['functions'])

        #Cria uma nova função vazia no dicionário
        self.class_creator['class']['functions'][f'function{functions_count + 1}'] = {'type': None, 'name': 'None', 'attrs': {'attr1': None}}

        #Conta o número de funções atualizado
        functions_count = len(self.class_creator['class']['functions'])

        #Cria um novo Frame para a UI
        function_frame = QtWidgets.QFrame(self.FunctionFrame)
        function_frame.setObjectName(f'FunctionCreator{functions_count}')
        function_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        function_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.grid_layout = QtWidgets.QGridLayout(function_frame)
        self.grid_layout.setObjectName(f'FunctionGridLayout{functions_count}')

        self.gridLayout_2.addWidget(function_frame, functions_count, 0)
        
        type_label = QtWidgets.QLabel(function_frame)
        type_label.setObjectName(f'FunctionType{functions_count}')
        type_label.setText('Function Type')

        self.grid_layout.addWidget(type_label, 0, 0)

        type_combo = QtWidgets.QComboBox(function_frame)
        type_combo.setObjectName(f'FunctionTypeEdit{functions_count}')
        type_combo.addItem("Custom")
        type_combo.addItem("__init__")
        type_combo.addItem("__str__")
        type_combo.addItem("__call__")


        self.grid_layout.addWidget(type_combo, 0, 1)

        type_label2 = QtWidgets.QLabel(function_frame)
        type_label2.setObjectName(f'FunctionName{functions_count}')
        type_label2.setText('Function Name')

        self.grid_layout.addWidget(type_label2, 1, 0)

        name_edit = QtWidgets.QLineEdit(function_frame)
        name_edit.setObjectName(f'FunctionNameEdit{functions_count}')

        self.grid_layout.addWidget(name_edit, 1, 1)

        attr_frame = QtWidgets.QFrame(function_frame)
        attr_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        attr_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        attr_frame.setObjectName(f'FunctionAttrFrame{functions_count}')

        horizontal_layout = QtWidgets.QHBoxLayout(attr_frame)
        horizontal_layout.setObjectName(f'horizontalLayout{functions_count}')

        attr_name = QtWidgets.QLabel(attr_frame)
        attr_name.setObjectName(f'attr_name{functions_count}')
        attr_name.setText('Attribute Name')

        horizontal_layout.addWidget(attr_name)

        attr_edit = QtWidgets.QLineEdit(attr_frame)
        attr_edit.setObjectName(f'AttributeNameEdit{functions_count}')

        horizontal_layout.addWidget(attr_edit)

        attr_type = QtWidgets.QComboBox(attr_frame)
        attr_type.setObjectName(f'AttrType{functions_count}')
        attr_type.addItem("None")
        attr_type.addItem("Int")
        attr_type.addItem("Float")
        attr_type.addItem("String")
        attr_type.addItem("List")
        attr_type.addItem("Tuple")
        attr_type.addItem("Dict")
        attr_type.addItem("Function")
        attr_type.addItem("Class")
        
        horizontal_layout.addWidget(attr_type)

        self.grid_layout.addWidget(attr_frame, 2, 0, 1, 3)

        self.push_btn = QtWidgets.QPushButton(function_frame)
        self.push_btn.setObjectName(f'NewAttribute{functions_count}')
        self.push_btn.setText('New Attriute')
        self.push_btn.clicked.connect(self.new_attr)

        self.grid_layout.addWidget(self.push_btn, 3, 0, 1, 3)

        self.gridLayout_2.removeWidget(self.NewFunction)
        self.gridLayout_2.addWidget(self.NewFunction)
   
    #Cria um novo Atributo para a Função Correspondente
    def new_attr(self):

        btn = self.sender()

        if btn != None: #Talvez reutilizar o código para a parte de criar a Função?
            parent = btn.parent()

            #Criando a variavel dentro do Dicionário da Criação de Classe
            if parent.objectName()[-1].isnumeric():
                attr_count = len(self.class_creator['class']['functions'][f'function{parent.objectName()[-1]}']['attrs']) + 1
                self.class_creator['class']['functions'][f'function{parent.objectName()[-1]}']['attrs'][f'attr{attr_count}'] = None
                attr_count = len(self.class_creator['class']['functions'][f'function{parent.objectName()[-1]}']['attrs'])
            
            else:
                attr_count = len(self.class_creator['class']['functions']['function1']['attrs']) + 1
                self.class_creator['class']['functions']['function1']['attrs'][f'attr{attr_count}'] = None
                attr_count = len(self.class_creator['class']['functions']['function1']['attrs'])
            
            layout = parent.findChild(QtWidgets.QGridLayout)

            #Localizando o botão dentro do grid para referência
            idx = layout.indexOf(btn)
            location = list(layout.getItemPosition(idx))
            location[0] = location[0] + 1
            location = tuple(location)
            a = location[0]
            b = location[1]
            c = location[2]
            d = location[3]

            #Criando a parte da UI
            attr_frame = QtWidgets.QFrame(parent)
            attr_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            attr_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            attr_frame.setObjectName(f'FunctionAttrFrame_{attr_count}')

            horizontal_layout = QtWidgets.QHBoxLayout(attr_frame)
            horizontal_layout.setObjectName(f'horizontalLayout_1{attr_count}')

            attr_name = QtWidgets.QLabel(attr_frame)
            attr_name.setObjectName(f'attr_name_{attr_count}')
            attr_name.setText('Attribute Name')

            horizontal_layout.addWidget(attr_name)

            attr_edit = QtWidgets.QLineEdit(attr_frame)
            attr_edit.setObjectName(f'AttributeNameEdit_{attr_count}')

            horizontal_layout.addWidget(attr_edit)

            attr_type = QtWidgets.QComboBox(attr_frame)
            attr_type.setObjectName(f'AttrType_{attr_count}')
            attr_type.addItem("None")
            attr_type.addItem("Int")
            attr_type.addItem("Float")
            attr_type.addItem("String")
            attr_type.addItem("List")
            attr_type.addItem("Tuple")
            attr_type.addItem("Dict")
            attr_type.addItem("Function")
            attr_type.addItem("Class")
            
            horizontal_layout.addWidget(attr_type)

            layout.addWidget(attr_frame, a, b, c, d)

            layout.removeWidget(btn)
            layout.addWidget(btn, a+1, b, c, d)



            


        

    

        

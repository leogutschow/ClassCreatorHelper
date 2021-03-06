# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/raws/RawUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 516)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 722, 435))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.ClassNameFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.ClassNameFrame.setAutoFillBackground(False)
        self.ClassNameFrame.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.ClassNameFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ClassNameFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ClassNameFrame.setObjectName("ClassNameFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ClassNameFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ClassName = QtWidgets.QLabel(self.ClassNameFrame)
        self.ClassName.setObjectName("ClassName")
        self.horizontalLayout.addWidget(self.ClassName)
        self.ClassNameEdit = QtWidgets.QLineEdit(self.ClassNameFrame)
        self.ClassNameEdit.setObjectName("ClassNameEdit")
        self.horizontalLayout.addWidget(self.ClassNameEdit)
        self.gridLayout.addWidget(self.ClassNameFrame, 0, 0, 1, 1)
        self.FunctionFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.FunctionFrame.setAutoFillBackground(False)
        self.FunctionFrame.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.FunctionFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FunctionFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FunctionFrame.setObjectName("FunctionFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.FunctionFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.NewFunction = QtWidgets.QPushButton(self.FunctionFrame)
        self.NewFunction.setCheckable(False)
        self.NewFunction.setObjectName("NewFunction")
        self.gridLayout_2.addWidget(self.NewFunction, 1, 0, 1, 1)
        self.FunctionCreator = QtWidgets.QFrame(self.FunctionFrame)
        self.FunctionCreator.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FunctionCreator.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FunctionCreator.setObjectName("FunctionCreator")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.FunctionCreator)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.FunctionNameEdit = QtWidgets.QLineEdit(self.FunctionCreator)
        self.FunctionNameEdit.setObjectName("FunctionNameEdit")
        self.gridLayout_3.addWidget(self.FunctionNameEdit, 1, 2, 1, 1)
        self.FunctionType = QtWidgets.QLabel(self.FunctionCreator)
        self.FunctionType.setObjectName("FunctionType")
        self.gridLayout_3.addWidget(self.FunctionType, 0, 0, 1, 1)
        self.FunctionName = QtWidgets.QLabel(self.FunctionCreator)
        self.FunctionName.setObjectName("FunctionName")
        self.gridLayout_3.addWidget(self.FunctionName, 1, 0, 1, 1)
        self.FunctionAttrsFrame = QtWidgets.QFrame(self.FunctionCreator)
        self.FunctionAttrsFrame.setAutoFillBackground(False)
        self.FunctionAttrsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FunctionAttrsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FunctionAttrsFrame.setObjectName("FunctionAttrsFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.FunctionAttrsFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.FunctionAttrsFrame)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.AttributeNameEdit = QtWidgets.QLineEdit(self.FunctionAttrsFrame)
        self.AttributeNameEdit.setObjectName("AttributeNameEdit")
        self.horizontalLayout_2.addWidget(self.AttributeNameEdit)
        self.AttrType = QtWidgets.QComboBox(self.FunctionAttrsFrame)
        self.AttrType.setEditable(True)
        self.AttrType.setObjectName("AttrType")
        self.AttrType.addItem("")
        self.AttrType.addItem("")
        self.AttrType.addItem("")
        self.AttrType.addItem("")
        self.AttrType.addItem("")
        self.AttrType.addItem("")
        self.AttrType.addItem("")
        self.AttrType.addItem("")
        self.AttrType.addItem("")
        self.horizontalLayout_2.addWidget(self.AttrType)
        self.gridLayout_3.addWidget(self.FunctionAttrsFrame, 2, 0, 1, 3)
        self.FunctionTypeEdit = QtWidgets.QComboBox(self.FunctionCreator)
        self.FunctionTypeEdit.setEditable(False)
        self.FunctionTypeEdit.setObjectName("FunctionTypeEdit")
        self.FunctionTypeEdit.addItem("")
        self.FunctionTypeEdit.addItem("")
        self.FunctionTypeEdit.addItem("")
        self.FunctionTypeEdit.addItem("")
        self.gridLayout_3.addWidget(self.FunctionTypeEdit, 0, 2, 1, 1)
        self.NewAttribute = QtWidgets.QPushButton(self.FunctionCreator)
        self.NewAttribute.setObjectName("NewAttribute")
        self.gridLayout_3.addWidget(self.NewAttribute, 3, 0, 1, 3)
        self.gridLayout_2.addWidget(self.FunctionCreator, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.FunctionFrame, 1, 0, 1, 1)
        self.CreateClass = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.CreateClass.setObjectName("CreateClass")
        self.gridLayout.addWidget(self.CreateClass, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 762, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Class Helper"))
        self.ClassName.setText(_translate("MainWindow", "Class Name"))
        self.NewFunction.setText(_translate("MainWindow", "New Function"))
        self.FunctionType.setText(_translate("MainWindow", "Function Type"))
        self.FunctionName.setText(_translate("MainWindow", "Function Name"))
        self.label.setText(_translate("MainWindow", "Parameter Name"))
        self.AttrType.setItemText(0, _translate("MainWindow", "None"))
        self.AttrType.setItemText(1, _translate("MainWindow", "Int"))
        self.AttrType.setItemText(2, _translate("MainWindow", "Float"))
        self.AttrType.setItemText(3, _translate("MainWindow", "String"))
        self.AttrType.setItemText(4, _translate("MainWindow", "List"))
        self.AttrType.setItemText(5, _translate("MainWindow", "Tuple"))
        self.AttrType.setItemText(6, _translate("MainWindow", "Dict"))
        self.AttrType.setItemText(7, _translate("MainWindow", "Function"))
        self.AttrType.setItemText(8, _translate("MainWindow", "Class"))
        self.FunctionTypeEdit.setItemText(0, _translate("MainWindow", "Custom"))
        self.FunctionTypeEdit.setItemText(1, _translate("MainWindow", "__init__"))
        self.FunctionTypeEdit.setItemText(2, _translate("MainWindow", "__str__"))
        self.FunctionTypeEdit.setItemText(3, _translate("MainWindow", "__call__"))
        self.NewAttribute.setText(_translate("MainWindow", "New Parameter"))
        self.CreateClass.setText(_translate("MainWindow", "Create Class"))

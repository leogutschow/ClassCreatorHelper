# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\VisualStudioCode\ClassCreator\ClassCreatorHelper\UI\raws\RawUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 774)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 722, 693))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
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
        self.verticalLayout_7.addWidget(self.ClassNameFrame)
        self.FunctionFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.FunctionFrame.setAutoFillBackground(False)
        self.FunctionFrame.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.FunctionFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FunctionFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FunctionFrame.setObjectName("FunctionFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.FunctionFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.FunctionFrame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.FunctionTypeFrame = QtWidgets.QFrame(self.frame_2)
        self.FunctionTypeFrame.setAutoFillBackground(False)
        self.FunctionTypeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FunctionTypeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FunctionTypeFrame.setObjectName("FunctionTypeFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.FunctionTypeFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.FunctionType = QtWidgets.QLabel(self.FunctionTypeFrame)
        self.FunctionType.setObjectName("FunctionType")
        self.horizontalLayout_3.addWidget(self.FunctionType)
        self.FunctionTypeEdit = QtWidgets.QComboBox(self.FunctionTypeFrame)
        self.FunctionTypeEdit.setEditable(False)
        self.FunctionTypeEdit.setObjectName("FunctionTypeEdit")
        self.FunctionTypeEdit.addItem("")
        self.FunctionTypeEdit.addItem("")
        self.FunctionTypeEdit.addItem("")
        self.FunctionTypeEdit.addItem("")
        self.horizontalLayout_3.addWidget(self.FunctionTypeEdit)
        self.verticalLayout_6.addWidget(self.FunctionTypeFrame)
        self.FunctionNameFrame = QtWidgets.QFrame(self.frame_2)
        self.FunctionNameFrame.setAutoFillBackground(False)
        self.FunctionNameFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FunctionNameFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FunctionNameFrame.setObjectName("FunctionNameFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.FunctionNameFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.FunctionName = QtWidgets.QLabel(self.FunctionNameFrame)
        self.FunctionName.setObjectName("FunctionName")
        self.horizontalLayout_2.addWidget(self.FunctionName)
        self.FunctionNameEdit = QtWidgets.QLineEdit(self.FunctionNameFrame)
        self.FunctionNameEdit.setObjectName("FunctionNameEdit")
        self.horizontalLayout_2.addWidget(self.FunctionNameEdit)
        self.verticalLayout_6.addWidget(self.FunctionNameFrame)
        self.FunctionAttrsFrame = QtWidgets.QFrame(self.frame_2)
        self.FunctionAttrsFrame.setAutoFillBackground(False)
        self.FunctionAttrsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FunctionAttrsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FunctionAttrsFrame.setObjectName("FunctionAttrsFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.FunctionAttrsFrame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.FunctioNameLabelFrame = QtWidgets.QFrame(self.FunctionAttrsFrame)
        self.FunctioNameLabelFrame.setAutoFillBackground(False)
        self.FunctioNameLabelFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FunctioNameLabelFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FunctioNameLabelFrame.setObjectName("FunctioNameLabelFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.FunctioNameLabelFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.FunctionAttributes = QtWidgets.QLabel(self.FunctioNameLabelFrame)
        self.FunctionAttributes.setObjectName("FunctionAttributes")
        self.verticalLayout_4.addWidget(self.FunctionAttributes)
        self.verticalLayout_5.addWidget(self.FunctioNameLabelFrame)
        self.SingleAttrFrame = QtWidgets.QFrame(self.FunctionAttrsFrame)
        self.SingleAttrFrame.setAutoFillBackground(False)
        self.SingleAttrFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SingleAttrFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SingleAttrFrame.setObjectName("SingleAttrFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.SingleAttrFrame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.SingleAttrFrame)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.AttributeNameEdit = QtWidgets.QLineEdit(self.SingleAttrFrame)
        self.AttributeNameEdit.setObjectName("AttributeNameEdit")
        self.horizontalLayout_4.addWidget(self.AttributeNameEdit)
        self.AttrType = QtWidgets.QComboBox(self.SingleAttrFrame)
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
        self.AttrType.addItem("")
        self.horizontalLayout_4.addWidget(self.AttrType)
        self.verticalLayout_5.addWidget(self.SingleAttrFrame)
        self.NewAttribute = QtWidgets.QPushButton(self.FunctionAttrsFrame)
        self.NewAttribute.setObjectName("NewAttribute")
        self.verticalLayout_5.addWidget(self.NewAttribute)
        self.verticalLayout_6.addWidget(self.FunctionAttrsFrame)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.NewFunction = QtWidgets.QPushButton(self.FunctionFrame)
        self.NewFunction.setCheckable(False)
        self.NewFunction.setObjectName("NewFunction")
        self.verticalLayout_3.addWidget(self.NewFunction)
        self.verticalLayout_7.addWidget(self.FunctionFrame)
        self.CreateClass = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.CreateClass.setObjectName("CreateClass")
        self.verticalLayout_7.addWidget(self.CreateClass)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ClassName.setText(_translate("MainWindow", "Class Name"))
        self.FunctionType.setText(_translate("MainWindow", "Function Type"))
        self.FunctionTypeEdit.setItemText(0, _translate("MainWindow", "Custom"))
        self.FunctionTypeEdit.setItemText(1, _translate("MainWindow", "__init__"))
        self.FunctionTypeEdit.setItemText(2, _translate("MainWindow", "__str__"))
        self.FunctionTypeEdit.setItemText(3, _translate("MainWindow", "__call__"))
        self.FunctionName.setText(_translate("MainWindow", "Function Name"))
        self.FunctionAttributes.setText(_translate("MainWindow", "Function Attributes"))
        self.label.setText(_translate("MainWindow", "Attribute Name"))
        self.AttrType.setItemText(0, _translate("MainWindow", "Type"))
        self.AttrType.setItemText(1, _translate("MainWindow", "None"))
        self.AttrType.setItemText(2, _translate("MainWindow", "Int"))
        self.AttrType.setItemText(3, _translate("MainWindow", "Float"))
        self.AttrType.setItemText(4, _translate("MainWindow", "String"))
        self.AttrType.setItemText(5, _translate("MainWindow", "List"))
        self.AttrType.setItemText(6, _translate("MainWindow", "Tuple"))
        self.AttrType.setItemText(7, _translate("MainWindow", "Dict"))
        self.AttrType.setItemText(8, _translate("MainWindow", "Function"))
        self.AttrType.setItemText(9, _translate("MainWindow", "Class"))
        self.NewAttribute.setText(_translate("MainWindow", "New Attibute"))
        self.NewFunction.setText(_translate("MainWindow", "New Function"))
        self.CreateClass.setText(_translate("MainWindow", "Create Class"))

# Form implementation generated from reading ui file 'Dialogo.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(378, 232)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 49, 16))
        self.label.setObjectName("label")
        self.lineEditRoute = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEditRoute.setGeometry(QtCore.QRect(40, 60, 301, 31))
        self.lineEditRoute.setObjectName("lineEditRoute")
        self.btnAceptar = QtWidgets.QPushButton(parent=Dialog)
        self.btnAceptar.setGeometry(QtCore.QRect(170, 120, 75, 24))
        self.btnAceptar.setObjectName("btnAceptar")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 120, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Route"))
        self.btnAceptar.setText(_translate("Dialog", "Aceptar"))
        self.pushButton_2.setText(_translate("Dialog", "Cancelar"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(850, 500)
        self.registerBtn = QtWidgets.QPushButton(Dialog)
        self.registerBtn.setGeometry(QtCore.QRect(490, 380, 150, 61))
        font = QtGui.QFont()
        font.setFamily("Nanum Gothic")
        font.setPointSize(18)
        self.registerBtn.setFont(font)
        self.registerBtn.setAutoDefault(False)
        self.registerBtn.setObjectName("registerBtn")
        self.id_label = QtWidgets.QLabel(Dialog)
        self.id_label.setGeometry(QtCore.QRect(220, 230, 130, 61))
        font = QtGui.QFont()
        font.setFamily("Nanum Gothic")
        font.setPointSize(24)
        self.id_label.setFont(font)
        self.id_label.setAlignment(QtCore.Qt.AlignCenter)
        self.id_label.setObjectName("id_label")
        self.name_edit = QtWidgets.QLineEdit(Dialog)
        self.name_edit.setGeometry(QtCore.QRect(340, 170, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Nanum Gothic")
        font.setPointSize(18)
        self.name_edit.setFont(font)
        self.name_edit.setText("")
        self.name_edit.setObjectName("name_edit")
        self.title_label_2 = QtWidgets.QLabel(Dialog)
        self.title_label_2.setGeometry(QtCore.QRect(280, 40, 311, 71))
        font = QtGui.QFont()
        font.setFamily("BM Hanna 11yrs Old")
        font.setPointSize(48)
        self.title_label_2.setFont(font)
        self.title_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label_2.setObjectName("title_label_2")
        self.name_label = QtWidgets.QLabel(Dialog)
        self.name_label.setGeometry(QtCore.QRect(230, 160, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Nanum Gothic")
        font.setPointSize(24)
        self.name_label.setFont(font)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.title_label = QtWidgets.QLabel(Dialog)
        self.title_label.setGeometry(QtCore.QRect(180, 110, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Nanum Gothic")
        font.setPointSize(24)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.id_edit = QtWidgets.QLineEdit(Dialog)
        self.id_edit.setGeometry(QtCore.QRect(340, 240, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.id_edit.setFont(font)
        self.id_edit.setText("")
        self.id_edit.setObjectName("id_edit")
        self.pw_label = QtWidgets.QLabel(Dialog)
        self.pw_label.setGeometry(QtCore.QRect(200, 300, 130, 61))
        font = QtGui.QFont()
        font.setFamily("Nanum Gothic")
        font.setPointSize(24)
        self.pw_label.setFont(font)
        self.pw_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pw_label.setObjectName("pw_label")
        self.pw_edit = QtWidgets.QLineEdit(Dialog)
        self.pw_edit.setGeometry(QtCore.QRect(340, 310, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pw_edit.setFont(font)
        self.pw_edit.setText("")
        self.pw_edit.setObjectName("pw_edit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.registerBtn.setText(_translate("Dialog", "회원가입"))
        self.id_label.setText(_translate("Dialog", "학번:"))
        self.title_label_2.setText(_translate("Dialog", "LockerSpot"))
        self.name_label.setText(_translate("Dialog", "이름:"))
        self.title_label.setText(_translate("Dialog", "회원가입"))
        self.pw_label.setText(_translate("Dialog", "비밀번호:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

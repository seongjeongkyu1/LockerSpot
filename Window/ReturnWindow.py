# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReturnWindow.ui'
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
        self.title_label = QtWidgets.QLabel(Dialog)
        self.title_label.setGeometry(QtCore.QRect(10, 10, 832, 51))
        font = QtGui.QFont()
        font.setFamily("Nanum Gothic")
        font.setPointSize(30)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.returnBox = QtWidgets.QGroupBox(Dialog)
        self.returnBox.setGeometry(QtCore.QRect(40, 90, 361, 371))
        font = QtGui.QFont()
        font.setFamily("Nanum Gothic")
        font.setPointSize(20)
        self.returnBox.setFont(font)
        self.returnBox.setStyleSheet("")
        self.returnBox.setObjectName("returnBox")
        self.name_label = QtWidgets.QLabel(self.returnBox)
        self.name_label.setGeometry(QtCore.QRect(20, 110, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Nanum Gothic")
        font.setPointSize(18)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.locker_label = QtWidgets.QLabel(self.returnBox)
        self.locker_label.setGeometry(QtCore.QRect(20, 160, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Nanum Gothic")
        font.setPointSize(18)
        self.locker_label.setFont(font)
        self.locker_label.setObjectName("locker_label")
        self.returnBtn = QtWidgets.QPushButton(self.returnBox)
        self.returnBtn.setGeometry(QtCore.QRect(20, 300, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.returnBtn.setFont(font)
        self.returnBtn.setAutoDefault(False)
        self.returnBtn.setObjectName("returnBtn")
        self.usageHistoryBox = QtWidgets.QGroupBox(Dialog)
        self.usageHistoryBox.setGeometry(QtCore.QRect(440, 90, 361, 371))
        font = QtGui.QFont()
        font.setFamily("Nanum Gothic")
        font.setPointSize(20)
        self.usageHistoryBox.setFont(font)
        self.usageHistoryBox.setStyleSheet("")
        self.usageHistoryBox.setObjectName("usageHistoryBox")
        self.usageHistoryBtn = QtWidgets.QPushButton(self.usageHistoryBox)
        self.usageHistoryBtn.setGeometry(QtCore.QRect(20, 300, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.usageHistoryBtn.setFont(font)
        self.usageHistoryBtn.setAutoDefault(False)
        self.usageHistoryBtn.setObjectName("usageHistoryBtn")
        self.usageHistoryList = QtWidgets.QListWidget(self.usageHistoryBox)
        self.usageHistoryList.setGeometry(QtCore.QRect(30, 60, 301, 221))
        self.usageHistoryList.setObjectName("usageHistoryList")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title_label.setText(_translate("Dialog", "사물함 반납"))
        self.returnBox.setTitle(_translate("Dialog", "사물함 반납하기"))
        self.name_label.setText(_translate("Dialog", "학생 이름 : "))
        self.locker_label.setText(_translate("Dialog", "대여중인 사물함 : "))
        self.returnBtn.setText(_translate("Dialog", "반납하기"))
        self.usageHistoryBox.setTitle(_translate("Dialog", "사물함 이용 내역 확인하기"))
        self.usageHistoryBtn.setText(_translate("Dialog", "확인하기"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
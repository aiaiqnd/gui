# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        self.frame = QtWidgets.QFrame(Widget)
        self.frame.setGeometry(QtCore.QRect(20, 230, 351, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnClose = QtWidgets.QPushButton(self.frame)
        self.btnClose.setGeometry(QtCore.QRect(200, 20, 75, 23))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/DOORCLOSE_EXIT_NORMAL.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClose.setIcon(icon)
        self.btnClose.setObjectName("btnClose")
        self.groupBox_Age = QtWidgets.QGroupBox(Widget)
        self.groupBox_Age.setGeometry(QtCore.QRect(20, 10, 351, 111))
        self.groupBox_Age.setObjectName("groupBox_Age")
        self.editAgeint = QtWidgets.QLineEdit(self.groupBox_Age)
        self.editAgeint.setGeometry(QtCore.QRect(172, 50, 161, 20))
        self.editAgeint.setObjectName("editAgeint")
        self.editAgeistr = QtWidgets.QLineEdit(self.groupBox_Age)
        self.editAgeistr.setGeometry(QtCore.QRect(172, 80, 161, 20))
        self.editAgeistr.setObjectName("editAgeistr")
        self.sliderSetage = QtWidgets.QScrollBar(self.groupBox_Age)
        self.sliderSetage.setGeometry(QtCore.QRect(190, 20, 160, 16))
        self.sliderSetage.setOrientation(QtCore.Qt.Horizontal)
        self.sliderSetage.setObjectName("sliderSetage")
        self.label = QtWidgets.QLabel(self.groupBox_Age)
        self.label.setGeometry(QtCore.QRect(30, 20, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_Age)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_Age)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 131, 16))
        self.label_3.setObjectName("label_3")
        self.groupBox_Name = QtWidgets.QGroupBox(Widget)
        self.groupBox_Name.setGeometry(QtCore.QRect(20, 130, 351, 91))
        self.groupBox_Name.setObjectName("groupBox_Name")
        self.btnSetName = QtWidgets.QPushButton(self.groupBox_Name)
        self.btnSetName.setGeometry(QtCore.QRect(270, 30, 75, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/favicon[1].ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSetName.setIcon(icon1)
        self.btnSetName.setObjectName("btnSetName")
        self.editNameIput = QtWidgets.QLineEdit(self.groupBox_Name)
        self.editNameIput.setGeometry(QtCore.QRect(150, 30, 113, 20))
        self.editNameIput.setObjectName("editNameIput")
        self.editNameHello = QtWidgets.QLineEdit(self.groupBox_Name)
        self.editNameHello.setGeometry(QtCore.QRect(150, 60, 181, 20))
        self.editNameHello.setObjectName("editNameHello")
        self.label_4 = QtWidgets.QLabel(self.groupBox_Name)
        self.label_4.setGeometry(QtCore.QRect(50, 30, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_Name)
        self.label_5.setGeometry(QtCore.QRect(20, 60, 121, 20))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.btnClose.setText(_translate("Widget", "关闭"))
        self.groupBox_Age.setTitle(_translate("Widget", "GroupBox"))
        self.label.setText(_translate("Widget", "设置年龄（0-100）"))
        self.label_2.setText(_translate("Widget", "ageChanged响应（int）"))
        self.label_3.setText(_translate("Widget", "ageChanged响应（str）"))
        self.groupBox_Name.setTitle(_translate("Widget", "GroupBox"))
        self.btnSetName.setText(_translate("Widget", "设置姓名"))
        self.label_4.setText(_translate("Widget", "输入姓名"))
        self.label_5.setText(_translate("Widget", "nameChanged(str)响应"))
import res_rc

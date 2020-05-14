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
        Widget.resize(643, 327)
        self.groupBox = QtWidgets.QGroupBox(Widget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 331, 301))
        self.groupBox.setObjectName("groupBox")
        self.btnGetTime = QtWidgets.QPushButton(self.groupBox)
        self.btnGetTime.setGeometry(QtCore.QRect(50, 60, 121, 23))
        self.btnGetTime.setObjectName("btnGetTime")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(210, 60, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(12, 92, 24, 16))
        self.label_2.setObjectName("label_2")
        self.timeEdit = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEdit.setGeometry(QtCore.QRect(42, 92, 141, 20))
        self.timeEdit.setObjectName("timeEdit")
        self.editTime = QtWidgets.QLineEdit(self.groupBox)
        self.editTime.setGeometry(QtCore.QRect(190, 90, 133, 20))
        self.editTime.setObjectName("editTime")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(12, 161, 24, 16))
        self.label_3.setObjectName("label_3")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(42, 161, 141, 20))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.editDate = QtWidgets.QLineEdit(self.groupBox)
        self.editDate.setGeometry(QtCore.QRect(190, 160, 133, 20))
        self.editDate.setObjectName("editDate")
        self.btnSetTime = QtWidgets.QPushButton(self.groupBox)
        self.btnSetTime.setGeometry(QtCore.QRect(210, 120, 91, 23))
        self.btnSetTime.setObjectName("btnSetTime")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(12, 231, 48, 16))
        self.label_4.setObjectName("label_4")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit.setGeometry(QtCore.QRect(66, 231, 120, 20))
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.editDateTime = QtWidgets.QLineEdit(self.groupBox)
        self.editDateTime.setGeometry(QtCore.QRect(192, 231, 133, 20))
        self.editDateTime.setObjectName("editDateTime")
        self.btnSetDateTime = QtWidgets.QPushButton(self.groupBox)
        self.btnSetDateTime.setGeometry(QtCore.QRect(210, 260, 91, 23))
        self.btnSetDateTime.setObjectName("btnSetDateTime")
        self.btnSetDate = QtWidgets.QPushButton(self.groupBox)
        self.btnSetDate.setGeometry(QtCore.QRect(210, 190, 91, 23))
        self.btnSetDate.setObjectName("btnSetDate")
        self.groupBox_2 = QtWidgets.QGroupBox(Widget)
        self.groupBox_2.setGeometry(QtCore.QRect(370, 40, 271, 271))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label_5.setObjectName("label_5")
        self.editCalendar = QtWidgets.QLineEdit(self.groupBox_2)
        self.editCalendar.setGeometry(QtCore.QRect(90, 20, 113, 20))
        self.editCalendar.setObjectName("editCalendar")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.groupBox_2)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 50, 251, 191))
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "日期时间"))
        self.groupBox.setTitle(_translate("Widget", "日期时间"))
        self.btnGetTime.setText(_translate("Widget", "读取当前日期时间"))
        self.label.setText(_translate("Widget", "字符串显示"))
        self.label_2.setText(_translate("Widget", "时间"))
        self.label_3.setText(_translate("Widget", "日期"))
        self.btnSetTime.setText(_translate("Widget", "设置时间"))
        self.label_4.setText(_translate("Widget", "日期时间"))
        self.btnSetDateTime.setText(_translate("Widget", "设置日期时间"))
        self.btnSetDate.setText(_translate("Widget", "设置日期"))
        self.groupBox_2.setTitle(_translate("Widget", "日历选择"))
        self.label_5.setText(_translate("Widget", "选择的日期："))

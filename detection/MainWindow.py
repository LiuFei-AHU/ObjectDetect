# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 588)
        MainWindow.setMinimumSize(QtCore.QSize(800, 588))
        MainWindow.setMaximumSize(QtCore.QSize(800, 588))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 50, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 100, 761, 361))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 759, 359))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.showImg = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.showImg.setGeometry(QtCore.QRect(20, 20, 721, 311))
        self.showImg.setObjectName("showImg")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.showInfo = QtWidgets.QLabel(self.centralwidget)
        self.showInfo.setGeometry(QtCore.QRect(20, 480, 751, 31))
        self.showInfo.setTextFormat(QtCore.Qt.RichText)
        self.showInfo.setScaledContents(True)
        self.showInfo.setWordWrap(True)
        self.showInfo.setObjectName("showInfo")
        self.generateButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateButton.setGeometry(QtCore.QRect(160, 50, 141, 31))
        self.generateButton.setObjectName("generateButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Object Detection"))
        self.pushButton.setText(_translate("MainWindow", "Open Image"))
        self.showImg.setText(_translate("MainWindow", "showImage"))
        self.showInfo.setText(_translate("MainWindow", "showInfo"))
        self.generateButton.setText(_translate("MainWindow", "Generate && Test"))

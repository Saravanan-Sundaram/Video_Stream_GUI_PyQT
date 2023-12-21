# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setStyleSheet("color: rgb(255, 255, 255);")
        self.start.setObjectName("start")
        self.gridLayout.addWidget(self.start, 1, 0, 1, 1)
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setStyleSheet("color: rgb(255, 255, 255);")
        self.stop.setObjectName("stop")
        self.gridLayout.addWidget(self.stop, 1, 1, 1, 1)
        self.capture = QtWidgets.QPushButton(self.centralwidget)
        self.capture.setStyleSheet("color: rgb(255, 255, 255);")
        self.capture.setObjectName("capture")
        self.gridLayout.addWidget(self.capture, 1, 2, 1, 1)
        self.camera = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.camera.setFont(font)
        self.camera.setStyleSheet("color: rgb(255, 255, 255);")
        self.camera.setAlignment(QtCore.Qt.AlignCenter)
        self.camera.setObjectName("camera")
        self.gridLayout.addWidget(self.camera, 0, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start.setText(_translate("MainWindow", "START"))
        self.stop.setText(_translate("MainWindow", "STOP"))
        self.capture.setText(_translate("MainWindow", "CAPTURE"))
        self.camera.setText(_translate("MainWindow", "Live Camera..."))



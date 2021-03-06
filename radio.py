# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'radio.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.setWindowModality(QtCore.Qt.ApplicationModal)
        MainForm.resize(1024, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainForm.sizePolicy().hasHeightForWidth())
        MainForm.setSizePolicy(sizePolicy)
        MainForm.setMinimumSize(QtCore.QSize(1024, 600))
        MainForm.setMaximumSize(QtCore.QSize(1024, 600))
        MainForm.setStyleSheet("")
        MainForm.setModal(True)
        self.slider_volume = QtWidgets.QSlider(MainForm)
        self.slider_volume.setEnabled(True)
        self.slider_volume.setGeometry(QtCore.QRect(945, 200, 41, 281))
        self.slider_volume.setTabletTracking(False)
        self.slider_volume.setToolTipDuration(0)
        self.slider_volume.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(32, 32, 33, 255), stop:1 rgba(98, 100, 100, 255));\n"
"border-radius: 8px;")
        self.slider_volume.setPageStep(10)
        self.slider_volume.setSliderPosition(0)
        self.slider_volume.setOrientation(QtCore.Qt.Vertical)
        self.slider_volume.setInvertedAppearance(False)
        self.slider_volume.setInvertedControls(False)
        self.slider_volume.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_volume.setObjectName("slider_volume")
        self.label_frequency = QtWidgets.QLabel(MainForm)
        self.label_frequency.setGeometry(QtCore.QRect(270, 110, 471, 141))
        font = QtGui.QFont()
        font.setFamily("SignPainter")
        font.setPointSize(120)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_frequency.setFont(font)
        self.label_frequency.setStyleSheet("color: rgb(250, 255, 255);\n"
"font: italic 120pt \"SignPainter\";")
        self.label_frequency.setAlignment(QtCore.Qt.AlignCenter)
        self.label_frequency.setObjectName("label_frequency")
        self.label_info = QtWidgets.QLabel(MainForm)
        self.label_info.setGeometry(QtCore.QRect(150, 280, 701, 41))
        self.label_info.setStyleSheet("font: 24pt \"Gill Sans\";\n"
"color: rgb(207, 211, 211);")
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")
        self.frame_interaction = QtWidgets.QFrame(MainForm)
        self.frame_interaction.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.frame_interaction.setStyleSheet("")
        self.frame_interaction.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_interaction.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_interaction.setObjectName("frame_interaction")
        self.button_add = QtWidgets.QPushButton(self.frame_interaction)
        self.button_add.setGeometry(QtCore.QRect(10, 8, 101, 101))
        self.button_add.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.button_add.setStyleSheet("color: rgb(140, 140, 140);\n"
"font: 100pt \"Gill Sans\";\n"
"text-align: center;")
        self.button_add.setFlat(True)
        self.button_add.setObjectName("button_add")
        self.button_p1 = QtWidgets.QPushButton(self.frame_interaction)
        self.button_p1.setGeometry(QtCore.QRect(130, 20, 140, 24))
        self.button_p1.setStyleSheet("color: rgb(130, 130, 130);\n"
"font: 18pt \"Gill Sans\";")
        self.button_p1.setFlat(True)
        self.button_p1.setObjectName("button_p1")
        self.button_p2 = QtWidgets.QPushButton(self.frame_interaction)
        self.button_p2.setGeometry(QtCore.QRect(280, 20, 140, 24))
        self.button_p2.setStyleSheet("color: rgb(255, 215, 0);\n"
"font: 18pt \"Gill Sans\";")
        self.button_p2.setFlat(True)
        self.button_p2.setObjectName("button_p2")
        self.button_p3 = QtWidgets.QPushButton(self.frame_interaction)
        self.button_p3.setGeometry(QtCore.QRect(430, 20, 140, 24))
        self.button_p3.setStyleSheet("color: rgb(130, 130, 130);\n"
"font: 18pt \"Gill Sans\";")
        self.button_p3.setFlat(True)
        self.button_p3.setObjectName("button_p3")
        self.button_p4 = QtWidgets.QPushButton(self.frame_interaction)
        self.button_p4.setGeometry(QtCore.QRect(580, 20, 140, 24))
        self.button_p4.setStyleSheet("color: rgb(130, 130, 130);\n"
"font: 18pt \"Gill Sans\";")
        self.button_p4.setFlat(True)
        self.button_p4.setObjectName("button_p4")
        self.button_p5 = QtWidgets.QPushButton(self.frame_interaction)
        self.button_p5.setGeometry(QtCore.QRect(730, 20, 140, 24))
        self.button_p5.setStyleSheet("color: rgb(130, 130, 130);\n"
"font: 18pt \"Gill Sans\";")
        self.button_p5.setFlat(True)
        self.button_p5.setObjectName("button_p5")
        self.button_p6 = QtWidgets.QPushButton(self.frame_interaction)
        self.button_p6.setGeometry(QtCore.QRect(880, 20, 140, 24))
        self.button_p6.setStyleSheet("color: rgb(130, 130, 130);\n"
"font: 18pt \"Gill Sans\";")
        self.button_p6.setFlat(True)
        self.button_p6.setObjectName("button_p6")
        self.line = QtWidgets.QFrame(self.frame_interaction)
        self.line.setGeometry(QtCore.QRect(123, 50, 891, 16))
        self.line.setStyleSheet("color: rgb(130, 130, 130);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.button_stop = QtWidgets.QPushButton(self.frame_interaction)
        self.button_stop.setGeometry(QtCore.QRect(15, 480, 101, 101))
        self.button_stop.setStyleSheet("border-style: outset;\n"
"border-radius: 50px;")
        self.button_stop.setText("")
        self.button_stop.setFlat(True)
        self.button_stop.setObjectName("button_stop")
        self.button_previous = QtWidgets.QPushButton(self.frame_interaction)
        self.button_previous.setGeometry(QtCore.QRect(330, 480, 101, 101))
        self.button_previous.setStyleSheet("border-style: outset;\n"
"border-radius: 50px;")
        self.button_previous.setText("")
        self.button_previous.setFlat(True)
        self.button_previous.setObjectName("button_previous")
        self.button_play = QtWidgets.QPushButton(self.frame_interaction)
        self.button_play.setGeometry(QtCore.QRect(460, 480, 101, 101))
        self.button_play.setStyleSheet("border-style: outset;\n"
"border-radius: 50px;")
        self.button_play.setText("")
        self.button_play.setFlat(True)
        self.button_play.setObjectName("button_play")
        self.button_next = QtWidgets.QPushButton(self.frame_interaction)
        self.button_next.setGeometry(QtCore.QRect(595, 480, 101, 101))
        self.button_next.setStyleSheet("border-style: outset;\n"
"border-radius: 50px;")
        self.button_next.setText("")
        self.button_next.setFlat(True)
        self.button_next.setObjectName("button_next")
        self.button_volume = QtWidgets.QPushButton(self.frame_interaction)
        self.button_volume.setGeometry(QtCore.QRect(910, 480, 101, 101))
        self.button_volume.setStyleSheet("border-style: outset;\n"
"border-radius: 50px;")
        self.button_volume.setText("")
        self.button_volume.setFlat(True)
        self.button_volume.setObjectName("button_volume")
        self.button_input_dab = QtWidgets.QPushButton(self.frame_interaction)
        self.button_input_dab.setGeometry(QtCore.QRect(35, 130, 71, 31))
        self.button_input_dab.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"Gill Sans\";\n"
"text-align: left;")
        self.button_input_dab.setFlat(True)
        self.button_input_dab.setObjectName("button_input_dab")
        self.button_input_fm = QtWidgets.QPushButton(self.frame_interaction)
        self.button_input_fm.setGeometry(QtCore.QRect(35, 152, 71, 31))
        self.button_input_fm.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_input_fm.setStyleSheet("color: rgb(140, 140, 140);\n"
"font: 18pt \"Gill Sans\";\n"
"text-align: left;")
        self.button_input_fm.setFlat(True)
        self.button_input_fm.setObjectName("button_input_fm")
        self.frame_dashboard = QtWidgets.QFrame(MainForm)
        self.frame_dashboard.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.frame_dashboard.setStyleSheet("image: url(:/resources/images/dash_play.png);")
        self.frame_dashboard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dashboard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dashboard.setObjectName("frame_dashboard")
        self.frame_dashboard.raise_()
        self.frame_interaction.raise_()
        self.slider_volume.raise_()
        self.label_frequency.raise_()
        self.label_info.raise_()

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Radio"))
        self.label_frequency.setText(_translate("MainForm", "96.2 Mhz"))
        self.label_info.setText(_translate("MainForm", "Bruce Springsteen - Tunnel of Love"))
        self.button_add.setText(_translate("MainForm", "+"))
        self.button_p1.setText(_translate("MainForm", "P1: KinkFM"))
        self.button_p2.setText(_translate("MainForm", "P1: KinkFM"))
        self.button_p3.setText(_translate("MainForm", "P1: KinkFM"))
        self.button_p4.setText(_translate("MainForm", "P1: KinkFM"))
        self.button_p5.setText(_translate("MainForm", "P1: KinkFM"))
        self.button_p6.setText(_translate("MainForm", "P1: KinkFM"))
        self.button_input_dab.setText(_translate("MainForm", "DAB+"))
        self.button_input_fm.setText(_translate("MainForm", "FM"))
import resources_rc

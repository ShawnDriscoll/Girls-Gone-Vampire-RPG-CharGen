# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alertdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_alertDialog(object):
    def setupUi(self, alertDialog):
        alertDialog.setObjectName("alertDialog")
        alertDialog.resize(340, 235)
        alertDialog.setMinimumSize(QtCore.QSize(340, 235))
        alertDialog.setMaximumSize(QtCore.QSize(340, 235))
        self.aboutOKButton = QtWidgets.QPushButton(alertDialog)
        self.aboutOKButton.setGeometry(QtCore.QRect(130, 170, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.aboutOKButton.setFont(font)
        self.aboutOKButton.setObjectName("aboutOKButton")
        self.textLabel = QtWidgets.QLabel(alertDialog)
        self.textLabel.setGeometry(QtCore.QRect(20, 40, 301, 131))
        self.textLabel.setTextFormat(QtCore.Qt.RichText)
        self.textLabel.setScaledContents(False)
        self.textLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.textLabel.setWordWrap(True)
        self.textLabel.setOpenExternalLinks(True)
        self.textLabel.setObjectName("textLabel")

        self.retranslateUi(alertDialog)
        QtCore.QMetaObject.connectSlotsByName(alertDialog)

    def retranslateUi(self, alertDialog):
        _translate = QtCore.QCoreApplication.translate
        alertDialog.setWindowTitle(_translate("alertDialog", "ALERT!"))
        self.aboutOKButton.setText(_translate("alertDialog", "OK"))
        self.textLabel.setText(_translate("alertDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Build 0.0.1 (Beta) of GGV CharGen has</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">EXPIRED</span><span style=\" font-size:10pt; font-weight:600;\">.</span></p><p align=\"center\"><span style=\" font-size:10pt;\">Check for a newer release from </span><a href=\"https://github.com/ShawnDriscoll/Girls-Gone-Vampire-RPG-CharGen\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">GitHub</span></a><span style=\" font-size:10pt;\">.</span><br/><span style=\" font-size:10pt;\">For support, email </span><a href=\"mailto:shawndriscoll@hotmail.com?subject=GGV CharGen 0.0.1 [EXPIRED Beta]\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">shawndriscoll@hotmail.com</span></a></p><p align=\"center\"><span style=\" font-size:10pt;\">Thank you for participating.</span></p></body></html>"))

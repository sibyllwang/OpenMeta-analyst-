# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_study_dlg.ui'
#
# Created: Wed Apr 17 14:37:20 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_new_study_dialog(object):
    def setupUi(self, new_study_dialog):
        new_study_dialog.setObjectName(_fromUtf8("new_study_dialog"))
        new_study_dialog.setEnabled(True)
        new_study_dialog.resize(301, 132)
        new_study_dialog.setMinimumSize(QtCore.QSize(301, 132))
        new_study_dialog.setMaximumSize(QtCore.QSize(301, 132))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        new_study_dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/meta.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        new_study_dialog.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(new_study_dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 90, 281, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.layoutWidget = QtGui.QWidget(new_study_dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 281, 71))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.study_lbl = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.study_lbl.setFont(font)
        self.study_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.study_lbl.setObjectName(_fromUtf8("study_lbl"))
        self.gridLayout.addWidget(self.study_lbl, 0, 1, 1, 1)

        self.retranslateUi(new_study_dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), new_study_dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), new_study_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(new_study_dialog)

    def retranslateUi(self, new_study_dialog):
        new_study_dialog.setWindowTitle(_translate("new_study_dialog", "add new study", None))
        self.label_2.setText(_translate("new_study_dialog", "study ", None))

import icons_rc

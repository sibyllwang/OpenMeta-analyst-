# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ma_specs2.ui'
#
# Created: Mon Nov 08 09:15:16 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(551, 573)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/meta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.tab)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.method_cbo_box = QtGui.QComboBox(self.tab)
        self.method_cbo_box.setObjectName("method_cbo_box")
        self.gridLayout.addWidget(self.method_cbo_box, 0, 1, 1, 1)
        self.parameter_grp_box = QtGui.QGroupBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.parameter_grp_box.sizePolicy().hasHeightForWidth())
        self.parameter_grp_box.setSizePolicy(sizePolicy)
        self.parameter_grp_box.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.parameter_grp_box.setFont(font)
        self.parameter_grp_box.setTitle("")
        self.parameter_grp_box.setObjectName("parameter_grp_box")
        self.gridLayout.addWidget(self.parameter_grp_box, 1, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.col1_str_edit = QtGui.QLineEdit(self.groupBox)
        self.col1_str_edit.setObjectName("col1_str_edit")
        self.gridLayout_2.addWidget(self.col1_str_edit, 0, 1, 1, 1)
        self.show_1 = QtGui.QCheckBox(self.groupBox)
        self.show_1.setChecked(True)
        self.show_1.setObjectName("show_1")
        self.gridLayout_2.addWidget(self.show_1, 0, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.col2_str_edit = QtGui.QLineEdit(self.groupBox)
        self.col2_str_edit.setObjectName("col2_str_edit")
        self.gridLayout_2.addWidget(self.col2_str_edit, 1, 1, 1, 1)
        self.show_2 = QtGui.QCheckBox(self.groupBox)
        self.show_2.setChecked(True)
        self.show_2.setObjectName("show_2")
        self.gridLayout_2.addWidget(self.show_2, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.col3_str_edit = QtGui.QLineEdit(self.groupBox)
        self.col3_str_edit.setObjectName("col3_str_edit")
        self.gridLayout_2.addWidget(self.col3_str_edit, 2, 1, 1, 1)
        self.show_3 = QtGui.QCheckBox(self.groupBox)
        self.show_3.setChecked(True)
        self.show_3.setObjectName("show_3")
        self.gridLayout_2.addWidget(self.show_3, 2, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.col4_str_edit = QtGui.QLineEdit(self.groupBox)
        self.col4_str_edit.setObjectName("col4_str_edit")
        self.gridLayout_2.addWidget(self.col4_str_edit, 3, 1, 1, 1)
        self.show_4 = QtGui.QCheckBox(self.groupBox)
        self.show_4.setChecked(True)
        self.show_4.setObjectName("show_4")
        self.gridLayout_2.addWidget(self.show_4, 3, 2, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.x_lbl_le = QtGui.QLineEdit(self.tab_2)
        self.x_lbl_le.setObjectName("x_lbl_le")
        self.gridLayout_3.addWidget(self.x_lbl_le, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.x_ticks_le = QtGui.QLineEdit(self.tab_2)
        self.x_ticks_le.setObjectName("x_ticks_le")
        self.gridLayout_3.addWidget(self.x_ticks_le, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.image_path = QtGui.QLineEdit(self.tab_2)
        self.image_path.setObjectName("image_path")
        self.horizontalLayout_4.addWidget(self.image_path)
        self.save_btn = QtGui.QPushButton(self.tab_2)
        self.save_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_4.addWidget(self.save_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Method & Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "analysis method:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog", "method", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "column labels", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "col 1 label:", None, QtGui.QApplication.UnicodeUTF8))
        self.col1_str_edit.setText(QtGui.QApplication.translate("Dialog", "Studies", None, QtGui.QApplication.UnicodeUTF8))
        self.show_1.setText(QtGui.QApplication.translate("Dialog", "show", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "col 2 label:", None, QtGui.QApplication.UnicodeUTF8))
        self.col2_str_edit.setText(QtGui.QApplication.translate("Dialog", "ES (LL, UL)", None, QtGui.QApplication.UnicodeUTF8))
        self.show_2.setText(QtGui.QApplication.translate("Dialog", "show", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "col 3 label:", None, QtGui.QApplication.UnicodeUTF8))
        self.col3_str_edit.setText(QtGui.QApplication.translate("Dialog", "Ev/Trt", None, QtGui.QApplication.UnicodeUTF8))
        self.show_3.setText(QtGui.QApplication.translate("Dialog", "show", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "col 4 label:", None, QtGui.QApplication.UnicodeUTF8))
        self.col4_str_edit.setText(QtGui.QApplication.translate("Dialog", "Ev/Ctrl", None, QtGui.QApplication.UnicodeUTF8))
        self.show_4.setText(QtGui.QApplication.translate("Dialog", "show", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "x label:", None, QtGui.QApplication.UnicodeUTF8))
        self.x_lbl_le.setText(QtGui.QApplication.translate("Dialog", "Effect size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "x ticks:", None, QtGui.QApplication.UnicodeUTF8))
        self.x_ticks_le.setText(QtGui.QApplication.translate("Dialog", "[default]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "save image to:", None, QtGui.QApplication.UnicodeUTF8))
        self.image_path.setText(QtGui.QApplication.translate("Dialog", "./r_tmp/forest.png", None, QtGui.QApplication.UnicodeUTF8))
        self.save_btn.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Dialog", "forest plot", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc

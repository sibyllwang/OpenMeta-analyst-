# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_new_projectdlg.ui'
#
# Created: Fri Apr 12 15:38:24 2013
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_newprojectdialog(object):
    def setupUi(self, newprojectdialog):
        newprojectdialog.setObjectName(_fromUtf8("newprojectdialog"))
        newprojectdialog.setEnabled(True)
        newprojectdialog.resize(504, 551)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(newprojectdialog.sizePolicy().hasHeightForWidth())
        newprojectdialog.setSizePolicy(sizePolicy)
        newprojectdialog.setSizeGripEnabled(True)
        newprojectdialog.setModal(False)
        self.verticalLayout = QtGui.QVBoxLayout(newprojectdialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.what_type_of_data_Label = QtGui.QLabel(newprojectdialog)
        self.what_type_of_data_Label.setMinimumSize(QtCore.QSize(281, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.what_type_of_data_Label.setFont(font)
        self.what_type_of_data_Label.setObjectName(_fromUtf8("what_type_of_data_Label"))
        self.verticalLayout.addWidget(self.what_type_of_data_Label)
        self.groupBox = QtGui.QGroupBox(newprojectdialog)
        self.groupBox.setMinimumSize(QtCore.QSize(480, 0))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.onearm_single_reg_coef_Button = QtGui.QToolButton(self.groupBox)
        self.onearm_single_reg_coef_Button.setMinimumSize(QtCore.QSize(120, 65))
        self.onearm_single_reg_coef_Button.setMaximumSize(QtCore.QSize(120, 65))
        self.onearm_single_reg_coef_Button.setBaseSize(QtCore.QSize(10, 10))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/new_dataset/startscreens/single_reg_coef.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.onearm_single_reg_coef_Button.setIcon(icon)
        self.onearm_single_reg_coef_Button.setIconSize(QtCore.QSize(40, 40))
        self.onearm_single_reg_coef_Button.setCheckable(True)
        self.onearm_single_reg_coef_Button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.onearm_single_reg_coef_Button.setObjectName(_fromUtf8("onearm_single_reg_coef_Button"))
        self.buttonGroup = QtGui.QButtonGroup(newprojectdialog)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.onearm_single_reg_coef_Button)
        self.gridLayout.addWidget(self.onearm_single_reg_coef_Button, 1, 2, 1, 1)
        self.twoarm_smds_Button = QtGui.QToolButton(self.groupBox)
        self.twoarm_smds_Button.setMinimumSize(QtCore.QSize(90, 65))
        self.twoarm_smds_Button.setMaximumSize(QtCore.QSize(90, 65))
        self.twoarm_smds_Button.setBaseSize(QtCore.QSize(10, 10))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/new_dataset/startscreens/smd.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.twoarm_smds_Button.setIcon(icon1)
        self.twoarm_smds_Button.setIconSize(QtCore.QSize(40, 40))
        self.twoarm_smds_Button.setCheckable(True)
        self.twoarm_smds_Button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.twoarm_smds_Button.setObjectName(_fromUtf8("twoarm_smds_Button"))
        self.buttonGroup.addButton(self.twoarm_smds_Button)
        self.gridLayout.addWidget(self.twoarm_smds_Button, 5, 2, 1, 1)
        self.onearm_generic_effect_size_Button = QtGui.QToolButton(self.groupBox)
        self.onearm_generic_effect_size_Button.setMinimumSize(QtCore.QSize(90, 65))
        self.onearm_generic_effect_size_Button.setMaximumSize(QtCore.QSize(90, 65))
        self.onearm_generic_effect_size_Button.setBaseSize(QtCore.QSize(10, 10))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/new_dataset/startscreens/gen_eff_size.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.onearm_generic_effect_size_Button.setIcon(icon2)
        self.onearm_generic_effect_size_Button.setIconSize(QtCore.QSize(40, 40))
        self.onearm_generic_effect_size_Button.setCheckable(True)
        self.onearm_generic_effect_size_Button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.onearm_generic_effect_size_Button.setArrowType(QtCore.Qt.NoArrow)
        self.onearm_generic_effect_size_Button.setObjectName(_fromUtf8("onearm_generic_effect_size_Button"))
        self.buttonGroup.addButton(self.onearm_generic_effect_size_Button)
        self.gridLayout.addWidget(self.onearm_generic_effect_size_Button, 1, 3, 1, 1)
        self.onearm_mean_Button = QtGui.QToolButton(self.groupBox)
        self.onearm_mean_Button.setMinimumSize(QtCore.QSize(90, 65))
        self.onearm_mean_Button.setMaximumSize(QtCore.QSize(90, 65))
        self.onearm_mean_Button.setBaseSize(QtCore.QSize(10, 10))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/new_dataset/startscreens/mean.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.onearm_mean_Button.setIcon(icon3)
        self.onearm_mean_Button.setIconSize(QtCore.QSize(40, 40))
        self.onearm_mean_Button.setCheckable(True)
        self.onearm_mean_Button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.onearm_mean_Button.setObjectName(_fromUtf8("onearm_mean_Button"))
        self.buttonGroup.addButton(self.onearm_mean_Button)
        self.gridLayout.addWidget(self.onearm_mean_Button, 1, 1, 1, 1)
        self.onearm_proportion_Button = QtGui.QToolButton(self.groupBox)
        self.onearm_proportion_Button.setMinimumSize(QtCore.QSize(90, 65))
        self.onearm_proportion_Button.setMaximumSize(QtCore.QSize(90, 65))
        self.onearm_proportion_Button.setBaseSize(QtCore.QSize(10, 10))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/new_dataset/startscreens/proportion.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.onearm_proportion_Button.setIcon(icon4)
        self.onearm_proportion_Button.setIconSize(QtCore.QSize(40, 40))
        self.onearm_proportion_Button.setCheckable(True)
        self.onearm_proportion_Button.setChecked(False)
        self.onearm_proportion_Button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.onearm_proportion_Button.setObjectName(_fromUtf8("onearm_proportion_Button"))
        self.buttonGroup.addButton(self.onearm_proportion_Button)
        self.gridLayout.addWidget(self.onearm_proportion_Button, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 3)
        self.twoarm_proportions_Button = QtGui.QToolButton(self.groupBox)
        self.twoarm_proportions_Button.setMinimumSize(QtCore.QSize(90, 65))
        self.twoarm_proportions_Button.setMaximumSize(QtCore.QSize(90, 65))
        self.twoarm_proportions_Button.setBaseSize(QtCore.QSize(10, 10))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/new_dataset/startscreens/proportions.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.twoarm_proportions_Button.setIcon(icon5)
        self.twoarm_proportions_Button.setIconSize(QtCore.QSize(72, 44))
        self.twoarm_proportions_Button.setCheckable(True)
        self.twoarm_proportions_Button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.twoarm_proportions_Button.setObjectName(_fromUtf8("twoarm_proportions_Button"))
        self.buttonGroup.addButton(self.twoarm_proportions_Button)
        self.gridLayout.addWidget(self.twoarm_proportions_Button, 5, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 2)
        self.diagnostic_Button = QtGui.QToolButton(self.groupBox)
        self.diagnostic_Button.setMinimumSize(QtCore.QSize(90, 65))
        self.diagnostic_Button.setMaximumSize(QtCore.QSize(90, 65))
        self.diagnostic_Button.setBaseSize(QtCore.QSize(10, 10))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/new_dataset/startscreens/diagnostic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.diagnostic_Button.setIcon(icon6)
        self.diagnostic_Button.setIconSize(QtCore.QSize(85, 44))
        self.diagnostic_Button.setCheckable(True)
        self.diagnostic_Button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.diagnostic_Button.setObjectName(_fromUtf8("diagnostic_Button"))
        self.buttonGroup.addButton(self.diagnostic_Button)
        self.gridLayout.addWidget(self.diagnostic_Button, 8, 0, 1, 1)
        self.line_4 = QtGui.QFrame(self.groupBox)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 6, 0, 1, 6)
        self.line_2 = QtGui.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 6)
        self.twoarm_means_Button = QtGui.QToolButton(self.groupBox)
        self.twoarm_means_Button.setMinimumSize(QtCore.QSize(90, 65))
        self.twoarm_means_Button.setMaximumSize(QtCore.QSize(90, 65))
        self.twoarm_means_Button.setBaseSize(QtCore.QSize(10, 10))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/new_dataset/startscreens/means.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.twoarm_means_Button.setIcon(icon7)
        self.twoarm_means_Button.setIconSize(QtCore.QSize(54, 40))
        self.twoarm_means_Button.setCheckable(True)
        self.twoarm_means_Button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.twoarm_means_Button.setObjectName(_fromUtf8("twoarm_means_Button"))
        self.buttonGroup.addButton(self.twoarm_means_Button)
        self.gridLayout.addWidget(self.twoarm_means_Button, 5, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 5)
        self.verticalLayout.addWidget(self.groupBox)
        self.outcome_name_Frame = QtGui.QFrame(newprojectdialog)
        self.outcome_name_Frame.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.outcome_name_Frame.setPalette(palette)
        self.outcome_name_Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.outcome_name_Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.outcome_name_Frame.setObjectName(_fromUtf8("outcome_name_Frame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.outcome_name_Frame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.outcome_name_Frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.outcome_name_LineEdit = QtGui.QLineEdit(self.outcome_name_Frame)
        self.outcome_name_LineEdit.setEnabled(False)
        self.outcome_name_LineEdit.setText(_fromUtf8(""))
        self.outcome_name_LineEdit.setObjectName(_fromUtf8("outcome_name_LineEdit"))
        self.horizontalLayout_2.addWidget(self.outcome_name_LineEdit)
        self.verticalLayout.addWidget(self.outcome_name_Frame)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel_Button = QtGui.QPushButton(newprojectdialog)
        self.cancel_Button.setAutoDefault(False)
        self.cancel_Button.setObjectName(_fromUtf8("cancel_Button"))
        self.horizontalLayout.addWidget(self.cancel_Button)
        self.ok_Button = QtGui.QPushButton(newprojectdialog)
        self.ok_Button.setEnabled(False)
        self.ok_Button.setAutoDefault(False)
        self.ok_Button.setDefault(False)
        self.ok_Button.setObjectName(_fromUtf8("ok_Button"))
        self.horizontalLayout.addWidget(self.ok_Button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.helpLabel = QtGui.QLabel(newprojectdialog)
        self.helpLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.helpLabel.setOpenExternalLinks(True)
        self.helpLabel.setObjectName(_fromUtf8("helpLabel"))
        self.verticalLayout.addWidget(self.helpLabel)
        self.label.setBuddy(self.outcome_name_LineEdit)

        self.retranslateUi(newprojectdialog)
        QtCore.QObject.connect(self.cancel_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), newprojectdialog.reject)
        QtCore.QObject.connect(self.ok_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), newprojectdialog.accept)
        QtCore.QMetaObject.connectSlotsByName(newprojectdialog)

    def retranslateUi(self, newprojectdialog):
        newprojectdialog.setWindowTitle(_translate("newprojectdialog", "Dialog", None))
        self.what_type_of_data_Label.setText(_translate("newprojectdialog", "WHAT TYPE OF DATA DO YOU HAVE?", None))
        self.onearm_single_reg_coef_Button.setText(_translate("newprojectdialog", "regression coefficient", None))
        self.twoarm_smds_Button.setText(_translate("newprojectdialog", "SMD", None))
        self.onearm_generic_effect_size_Button.setText(_translate("newprojectdialog", "generic\n"
"effect size", None))
        self.onearm_mean_Button.setText(_translate("newprojectdialog", "mean", None))
        self.onearm_proportion_Button.setText(_translate("newprojectdialog", "proportion", None))
        self.label_4.setText(_translate("newprojectdialog", "Data on two or more groups per study", None))
        self.twoarm_proportions_Button.setText(_translate("newprojectdialog", "proportions", None))
        self.label_5.setText(_translate("newprojectdialog", "Data on test performance", None))
        self.diagnostic_Button.setText(_translate("newprojectdialog", "diagnostic", None))
        self.twoarm_means_Button.setText(_translate("newprojectdialog", "means", None))
        self.label_2.setText(_translate("newprojectdialog", "One piece of data from each study or studies with one group", None))
        self.label.setText(_translate("newprojectdialog", "What is the name of your outcome?", None))
        self.cancel_Button.setText(_translate("newprojectdialog", "Cancel", None))
        self.ok_Button.setText(_translate("newprojectdialog", "OK", None))
        self.helpLabel.setText(_translate("newprojectdialog", "<a href=\"http://tuftscaes.org/open_meta/help/openMA_help.html\">help</a>", None))

import icons_rc

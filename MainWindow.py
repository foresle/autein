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
        MainWindow.resize(308, 432)
        MainWindow.setMinimumSize(QtCore.QSize(308, 432))
        MainWindow.setMaximumSize(QtCore.QSize(450, 537))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.mainLayout.addItem(spacerItem)
        self.logo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMaximumSize(QtCore.QSize(10000000, 10000000))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.logo.setFont(font)
        self.logo.setAutoFillBackground(False)
        self.logo.setTextFormat(QtCore.Qt.MarkdownText)
        self.logo.setScaledContents(False)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.mainLayout.addWidget(self.logo)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.mainLayout.addItem(spacerItem1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 286, 269))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.templatesLayout = QtWidgets.QVBoxLayout()
        self.templatesLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.templatesLayout.setObjectName("templatesLayout")
        self.verticalLayout_3.addLayout(self.templatesLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.mainLayout.addWidget(self.scrollArea)
        self.verticalLayout.addLayout(self.mainLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCancel.sizePolicy().hasHeightForWidth())
        self.btnCancel.setSizePolicy(sizePolicy)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        self.btnAbout = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAbout.sizePolicy().hasHeightForWidth())
        self.btnAbout.setSizePolicy(sizePolicy)
        self.btnAbout.setObjectName("btnAbout")
        self.horizontalLayout.addWidget(self.btnAbout)
        self.btnInstall = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnInstall.sizePolicy().hasHeightForWidth())
        self.btnInstall.setSizePolicy(sizePolicy)
        self.btnInstall.setObjectName("btnInstall")
        self.horizontalLayout.addWidget(self.btnInstall)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AuTeIn Beta 0.8"))
        self.logo.setText(_translate("MainWindow", "AuTeIn Beta 0.8"))
        self.btnCancel.setText(_translate("MainWindow", "Cancel"))
        self.btnAbout.setText(_translate("MainWindow", "About"))
        self.btnInstall.setText(_translate("MainWindow", "Install"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

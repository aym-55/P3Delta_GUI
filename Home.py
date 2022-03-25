import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QLabel):
    
    def setupUi(self, MainWindow):
        super().__init__()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(934, 493)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:white;")
        self.centralwidget.setObjectName("centralwidget")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.label_P3delta_website = QtWidgets.QLabel(self.frame)
        self.label_P3delta_website.setObjectName("P3delta_website")
        self.label_P3delta_website.setOpenExternalLinks(True)
        self.label_P3delta_website.resize(0,0)
        self.gridLayout_2.addWidget(self.label_P3delta_website, 2, 1, 1, 9)
        
        self.label_Welcome = QtWidgets.QLabel(self.frame)
        self.label_Welcome.setObjectName("Welcome")
        self.gridLayout_2.addWidget(self.label_Welcome, 1, 0, 1, 9)
        
        self.label_User = QtWidgets.QLabel(self.frame)
        self.label_User.setObjectName("label_Admin")
        self.gridLayout_2.addWidget(self.label_User, 6, 3, 1, 1)
        
        self.label_Linkedin = QtWidgets.QLabel(self.frame)
        self.label_Linkedin.setObjectName("label_Linkedin")
        self.label_Linkedin.setOpenExternalLinks(True)
        self.gridLayout_2.addWidget(self.label_Linkedin, 3, 1, 1, 9)
        
        self.label_Settings = QtWidgets.QLabel(self.frame)
        self.label_Settings.setObjectName("label_Settings")
        self.gridLayout_2.addWidget(self.label_Settings, 4, 0, 1, 11)
        
        spacerItem = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 5, 5, 1, 1)
        
        self.label_P3delta = QtWidgets.QLabel(self.frame)
        self.label_P3delta.setObjectName("label_P3delta")
        self.gridLayout_2.addWidget(self.label_P3delta, 0, 0, 1, 11)
        
        spacerItem1 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 5, 8, 1, 1)
        
        self.label_Notification = QtWidgets.QLabel(self.frame)
        self.label_Notification.setObjectName("label_Notification")
        self.gridLayout_2.addWidget(self.label_Notification, 5, 0, 1, 1)
        
        slider_user = """QSlider::groove:horizontal { 
	background-color: grey;
	border: 0px solid #424242; 
	height: 10px; 
	border-radius: 4px;
}

QSlider::handle:horizontal { 
	background-color: white; 
	border: 2px solid; 
	width: 16px; 
	height: 20px; 
	line-height: 20px; 
	margin-top: -5px; 
	margin-bottom: -5px; 
	border-radius: 10px; 
}

QSlider::handle:horizontal:hover { 
	border-radius: 10px;
}"""


        
        self.horizontalSlider_2 = QtWidgets.QSlider(self.frame)
        self.horizontalSlider_2.setStyleSheet(slider_user)
        self.horizontalSlider_2.setMaximum(1)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.gridLayout_2.addWidget(self.horizontalSlider_2, 5, 1, 1, 1)
        self.horizontalSlider_2.valueChanged.connect(self.Slider_On)
        
        spacerItem2 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 5, 7, 1, 1)
        
        self.horizontalSlider_3 = QtWidgets.QSlider(self.frame)
        self.horizontalSlider_3.setStyleSheet(slider_user)
        self.horizontalSlider_3.setMaximum(1)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.gridLayout_2.addWidget(self.horizontalSlider_3, 6, 1, 1, 1)
        self.horizontalSlider_3.valueChanged.connect(self.Slider_User)
        
        self.label_Mode = QtWidgets.QLabel(self.frame)
        self.label_Mode.setObjectName("label_Mode")
        self.gridLayout_2.addWidget(self.label_Mode, 6, 0, 1, 1)
        
        self.label_On = QtWidgets.QLabel(self.frame)
        self.label_On.setObjectName("label_On")
        self.gridLayout_2.addWidget(self.label_On, 5, 3, 1, 1)
        
        spacerItem3 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 5, 6, 1, 1)
        
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 5, 2, 1, 1)
        
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 934, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_P3delta_website.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline; color:#0009be;\"><a href=\"https://iboussaa.gitlabpages.inria.fr/partial-pole-placement-via-delay-action/P3d-Home.html\">P3delta Website</a></span></p></body></html>"))
        self.label_Welcome.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt\">Welcome to P3delta Online ! A software for delayed control design. For more information, consult :</span></p></body></html>"))
        self.label_User.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt\">User</span></p></body></html>"))
        self.label_Linkedin.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline; color:#0009be;\"><a href=\"https://www.linkedin.com/company/p3delta\">P3delta Linkedin page</a></span></p></body></html>"))
        self.label_Settings.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#8e2042;\">Settings</span></p></body></html>"))
        self.label_P3delta.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#8e2042;\">P3delta Online</span></p></body></html>"))
        self.label_Notification.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt\">Notification :</span></p></body></html>"))
        self.label_Mode.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt\">Mode :</span></p></body></html>"))
        self.label_On.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt\">On</span></p></body></html>"))

    def Slider_On(self):
        _translate = QtCore.QCoreApplication.translate
        if self.horizontalSlider_2.value() == 1:
            self.label_On.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt\">Off</span></p></body></html>"))
        elif self.horizontalSlider_2.value() == 0:
            self.label_On.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt\">On</span></p></body></html>"))

    def Slider_User(self):
        _translate = QtCore.QCoreApplication.translate
        if self.horizontalSlider_2.value() == 1:
            self.label_User.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt\">User</span></p></body></html>"))
        elif self.horizontalSlider_2.value() == 0:
            self.label_User.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt\">Admin</span></p></body></html>"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

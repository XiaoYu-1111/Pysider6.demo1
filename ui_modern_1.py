# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modern_1.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 400)
        font = QFont()
        font.setFamilies([u"Arial Narrow"])
        font.setPointSize(15)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(600, 400))
        self.centralwidget.setStyleSheet(u"")
        self.drap_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drap_shadow_layout.setSpacing(0)
        self.drap_shadow_layout.setObjectName(u"drap_shadow_layout")
        self.drap_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drap_shadow_frame = QFrame(self.centralwidget)
        self.drap_shadow_frame.setObjectName(u"drap_shadow_frame")
        self.drap_shadow_frame.setStyleSheet(u"background-color: rgb(103, 104, 99);\n"
"border-radius:8px;")
        self.drap_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drap_shadow_frame.setFrameShadow(QFrame.Raised)
        self.drap_shadow_frame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.drap_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drap_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setAutoFillBackground(False)
        self.title_bar.setStyleSheet(u"")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        font1 = QFont()
        font1.setFamilies([u"Agency FB"])
        font1.setPointSize(17)
        self.frame_title.setFont(font1)
        self.frame_title.setStyleSheet(u"")
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.label_title.setFont(font2)
        self.label_title.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_title.setFrameShape(QFrame.Box)
        self.label_title.setLineWidth(0)

        self.verticalLayout_2.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        self.frame_btns.setStyleSheet(u"")
        self.frame_btns.setFrameShape(QFrame.NoFrame)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_maximize = QPushButton(self.frame_btns)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(17, 17))
        self.btn_maximize.setStyleSheet(u"#btn_maximize{border-radius:8px;background-color: rgb(0, 255, 0);}\n"
"#btn_maximize:hover{background-color: rgba(0, 255, 0, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_maximize)

        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"#btn_minimize{border-radius:8px;background-color: rgb(255, 170, 0);\n"
"}\n"
"#btn_minimize:hover{background-color: rgba(255, 170, 0, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_minimize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"#btn_close{border-radius:8px;background-color: rgb(255, 0, 0);\n"
"}\n"
"#btn_close:hover{background-color: rgba(255, 0, 0, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drap_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.content_bar.setFont(font3)
        self.content_bar.setStyleSheet(u"")
        self.content_bar.setFrameShape(QFrame.NoFrame)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.content_bar.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.content_bar)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget = QWidget(self.content_bar)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(100, 0))
        self.widget.setMaximumSize(QSize(200, 16777215))
        self.widget.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.Page1_button = QPushButton(self.widget)
        self.Page1_button.setObjectName(u"Page1_button")
        self.Page1_button.setMinimumSize(QSize(0, 40))
        self.Page1_button.setMaximumSize(QSize(100, 16777215))
        self.Page1_button.setStyleSheet(u"#Page1_button{color: rgb(153, 113, 113);background-color: rgb(237, 236, 208);}\n"
"#Page1_button:hover{background-color: rgb(220, 227, 235);}\n"
"#Page1_button:pressed{padding-top:5px;padding-left:5px;}")

        self.verticalLayout_7.addWidget(self.Page1_button)

        self.Page2_button = QPushButton(self.widget)
        self.Page2_button.setObjectName(u"Page2_button")
        self.Page2_button.setMinimumSize(QSize(0, 40))
        self.Page2_button.setMaximumSize(QSize(100, 16777215))
        self.Page2_button.setStyleSheet(u"#Page2_button{color: rgb(153, 113, 113);background-color: rgb(237, 236, 208);}\n"
"#Page2_button:hover{background-color: rgb(220, 227, 235);}\n"
"#Page2_button:pressed{padding-top:5px;padding-left:5px;}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_7.addWidget(self.Page2_button)

        self.Page3_button = QPushButton(self.widget)
        self.Page3_button.setObjectName(u"Page3_button")
        self.Page3_button.setMinimumSize(QSize(0, 40))
        self.Page3_button.setMaximumSize(QSize(100, 16777215))
        self.Page3_button.setStyleSheet(u"#Page3_button{color: rgb(153, 113, 113);background-color: rgb(237, 236, 208);}\n"
"#Page3_button:hover{background-color: rgb(220, 227, 235);}\n"
"#Page3_button:pressed{padding-top:5px;padding-left:5px;}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_7.addWidget(self.Page3_button)


        self.horizontalLayout_4.addWidget(self.widget)

        self.widget_2 = QWidget(self.content_bar)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_6 = QVBoxLayout(self.page_1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.page_1)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color: rgb(237, 236, 208);")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(50, -1, 50, -1)
        self.Search_con = QLineEdit(self.widget_3)
        self.Search_con.setObjectName(u"Search_con")
        self.Search_con.setMinimumSize(QSize(0, 40))
        self.Search_con.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Yu Gothic UI Semilight"])
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setUnderline(False)
        self.Search_con.setFont(font4)
        self.Search_con.setStyleSheet(u"background-color: rgb(103, 104, 99);\n"
"border-radius:20px;\n"
"color: rgb(237, 237, 239);")

        self.horizontalLayout_6.addWidget(self.Search_con)

        self.Search_but = QPushButton(self.widget_3)
        self.Search_but.setObjectName(u"Search_but")
        self.Search_but.setMinimumSize(QSize(100, 40))
        self.Search_but.setStyleSheet(u"#Search_but{color: rgb(237, 237, 239);background-color: rgb(103, 104, 99);}\n"
"#Search_but:hover{color: rgb(103, 104, 99);background-color: rgb(214, 182, 171);}\n"
"\n"
"\n"
"#Search_but:pressed{padding-top:5px;padding-left:5px;}")

        self.horizontalLayout_6.addWidget(self.Search_but)


        self.verticalLayout_6.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.page_1)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 0))
        self.widget_4.setMaximumSize(QSize(16777215, 60))
        self.widget_4.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(20, -1, 20, -1)
        self.Page1_but1 = QPushButton(self.widget_4)
        self.Page1_but1.setObjectName(u"Page1_but1")
        self.Page1_but1.setMaximumSize(QSize(300, 30))
        self.Page1_but1.setStyleSheet(u"#Page1_but1{color: rgb(153, 113, 113);background-color: rgb(237, 236, 208);}\n"
"#Page1_but1:hover{background-color: rgb(220, 227, 235);}\n"
"#Page1_but1:pressed{padding-top:5px;padding-left:5px;}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.Page1_but1)

        self.Page1_but2 = QPushButton(self.widget_4)
        self.Page1_but2.setObjectName(u"Page1_but2")
        self.Page1_but2.setMaximumSize(QSize(300, 30))
        self.Page1_but2.setStyleSheet(u"#Page1_but2{color: rgb(153, 113, 113);background-color: rgb(237, 236, 208);}\n"
"#Page1_but2:hover{background-color: rgb(220, 227, 235);}\n"
"#Page1_but2:pressed{padding-top:5px;padding-left:5px;}\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.Page1_but2)

        self.Page1_but3 = QPushButton(self.widget_4)
        self.Page1_but3.setObjectName(u"Page1_but3")
        self.Page1_but3.setMaximumSize(QSize(300, 30))
        self.Page1_but3.setStyleSheet(u"#Page1_but3{color: rgb(153, 113, 113);background-color: rgb(237, 236, 208);}\n"
"#Page1_but3:hover{background-color: rgb(220, 227, 235);}\n"
"#Page1_but3:pressed{padding-top:5px;padding-left:5px;}\n"
"")

        self.horizontalLayout_5.addWidget(self.Page1_but3)


        self.verticalLayout_6.addWidget(self.widget_4)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 10, 111, 51))
        font5 = QFont()
        font5.setPointSize(13)
        self.label.setFont(font5)
        self.label.setStyleSheet(u"color: rgb(153, 113, 113);background-color: rgb(237, 236, 208);")
        self.label.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 10, 111, 51))
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"color: rgb(153, 113, 113);background-color: rgb(237, 236, 208);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.widget_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.drap_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMinimumSize(QSize(0, 30))
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"")
        self.credits_bar.setFrameShape(QFrame.StyledPanel)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_label_credits = QFrame(self.credits_bar)
        self.frame_label_credits.setObjectName(u"frame_label_credits")
        self.frame_label_credits.setMaximumSize(QSize(16777215, 50))
        self.frame_label_credits.setStyleSheet(u"")
        self.frame_label_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_label_credits)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 0, 0, 0)
        self.label_credits = QLabel(self.frame_label_credits)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.label_credits)


        self.horizontalLayout_3.addWidget(self.frame_label_credits)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 30))
        self.frame_grip.setMaximumSize(QSize(60, 30))
        self.frame_grip.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_grip)


        self.verticalLayout.addWidget(self.credits_bar)


        self.drap_shadow_layout.addWidget(self.drap_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_close.clicked.connect(MainWindow.close)
        self.btn_minimize.clicked.connect(MainWindow.showMinimized)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"This is a Title !", None))
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize.setText("")
        self.btn_minimize.setText("")
        self.btn_close.setText("")
        self.Page1_button.setText(QCoreApplication.translate("MainWindow", u"Page1", None))
        self.Page2_button.setText(QCoreApplication.translate("MainWindow", u"Page2", None))
        self.Page3_button.setText(QCoreApplication.translate("MainWindow", u"Page3", None))
        self.Search_con.setText(QCoreApplication.translate("MainWindow", u"The rose", None))
        self.Search_but.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.Page1_but1.setText(QCoreApplication.translate("MainWindow", u"One", None))
        self.Page1_but2.setText(QCoreApplication.translate("MainWindow", u"Two", None))
        self.Page1_but3.setText(QCoreApplication.translate("MainWindow", u"Three", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Page2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Page3", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Designed by Xiao Yu !", None))
    # retranslateUi


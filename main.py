import sys
from PySide6  import QtCore,QtGui,QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *#导入库
import webbrowser

from ui_modern_1 import *#导入ui

from ui_functions import *#导入自定义函数

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)#隐藏原始系统边框
        
        UIFunctions.uiDefinitions(self)
        
        self.ui.Page1_button.clicked.connect(self.displaystack0)#链接不同页面
        self.ui.Page2_button.clicked.connect(self.displaystack1)
        self.ui.Page3_button.clicked.connect(self.displaystack2)
        self.ui.Search_but.clicked.connect(self.search)
    
        self.show()
        
    def displaystack0(self):#链接不同页面
            self.ui.stackedWidget.setCurrentIndex(0)
    def displaystack1(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def displaystack2(self):
        self.ui.stackedWidget.setCurrentIndex(2)   
    #search
    def search(self):
        query=self.ui.Search_con.text()
        webbrowser.open(f"https://www.baidu.com/s?wd={query}")
        
    
    #鼠标拖动
    def mousePressEvent(self,event):
        if event.button()==Qt.LeftButton and self.isMaximized() ==False:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos()#获取鼠标相对窗口位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))#更改鼠标图标
    def mouseMoveEvent(self,mouse_event):
        
        if UIFunctions.returnStatus()==1:
            UIFunctions.maximize_restore(self)#return窗口状态
    
        if Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos()-self.m_Position)#更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self,mouse_event):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
        
    

if __name__=='__main__':
    app=QApplication(sys.argv)
    windows=MainWindow()
    
    sys.exit(app.exec())

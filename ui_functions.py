from main import *

GLOBAL_STATE=0#全局状态
class UIFunctions(MainWindow):
    def maximize_restore(self):#定义最大化
        global  GLOBAL_STATE
        status=GLOBAL_STATE
        if status ==0:
            self.showMaximized()
            
            GLOBAL_STATE=1
            
            self.ui.drap_shadow_layout.setContentsMargins(0,0,0,0)
            #self.ui.drap_shadow_layout.setStyleSheet('background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(50, 50, 50, 255), stop:0.5 rgba(99, 99, 99, 255), stop:0.9801 rgba(50, 50, 50, 255));border-radius:0px;')
            self.ui.btn_maximize.setToolTip('Restore')
        else:
            GLOBAL_STATE=0
            self.showNormal()
            self.resize(self.width()+1,self.height()+1)
            self.ui.drap_shadow_layout.setContentsMargins(10,10,10,10)
            #self.ui.drap_shadow_layout.setStyleSheet('background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(50, 50, 50, 255), stop:0.5 rgba(99, 99, 99, 255), stop:0.9801 rgba(50, 50, 50, 255))')
            self.ui.btn_maximize.setToolTip('Maximize')
    def uiDefinitions(self):
        
        self.shadow=QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(237, 236, 208))
        
        self.ui.drap_shadow_frame.setGraphicsEffect(self.shadow)
        
        self.ui.btn_maximize.clicked.connect(lambda:UIFunctions.maximize_restore(self))
        
        #调整窗口大小
        self.sizegrip=QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet('QSizeGrip{width:50px;height:20px;margin:5px} QSizeGrip:hover{backgroup-color:rgb(0,0,0)}')
        self.sizegrip.setToolTip('Resize Window')

    def returnStatus():
        return GLOBAL_STATE
    
    
        
        

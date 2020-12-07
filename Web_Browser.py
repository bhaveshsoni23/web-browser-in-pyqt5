from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
import os
from PyQt5 import  QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


import sys

class MainWindow(QMainWindow):
    def __init__(self,*args,**Kwargs):
        super(MainWindow,self).__init__(*args,**Kwargs)
        self.setWindowTitle('Web Browser')
        self.setWindowIcon(QIcon(os.path.join('icons','Browser_Icon_24px.png')))
        self.browser = QWebView()
        self.browser.setUrl(QUrl('https://www.google.com/'))
        self.setCentralWidget(self.browser)
        
        navtb = QToolBar('Navigation')
        navtb.setIconSize(QSize(21,21))
        self.addToolBar(navtb)
        
        back_btn = QAction(QIcon(os.path.join('icons','Back_icon_24px.png')),"Back",self)
        back_btn.setStatusTip('Back to privious page')
        back_btn.triggered.connect( self.browser.back )
        navtb.addAction(back_btn)
        
        next_btn = QAction(QIcon(os.path.join('icons','Forword_icon_24px.png')),"Next",self)
        next_btn.setStatusTip('Next page')
        next_btn.triggered.connect( self.browser.forward )
        navtb.addAction(next_btn)
        
        reload_btn = QAction(QIcon(os.path.join('icons','UndoIcon-20px.png')),"Reload",self)
        reload_btn.setStatusTip('Reload')
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)
        
        home_btn = QAction( QIcon(os.path.join('icons','Home_icon_24px.png')), "Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect( self.navigate_home )
        navtb.addAction(home_btn)
        
        navtb.addSeparator()
        
        self.httpsicon = QLabel()
        self.httpsicon.setPixmap(QPixmap(os.path.join('icons','openlock_icon_24.png')))
        navtb.addWidget(self.httpsicon)
        
        
        
        self.urlbar=QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)
        
        
        stop_btn = QAction(QIcon(os.path.join('icons','xIcon_24px.png')),"stop",self)
        stop_btn.setStatusTip('stop')
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)
        
        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)
        
    def navigate_home(self):
        self.browser.setUrl(QUrl('http://www.google.com'))
        
        
        
    def navigate_to_url(self):
        q=QUrl(self.urlbar.text())
        if q.scheme()=="":
            q.setScheme('http')
        self.browser.setUrl()
        
    def update_urlbar(self,q):
        if q.scheme() == 'https':
            self.httpsicon.setPixmap(QPixmap(os.path.join('icons','openlock_icon_24.png')))
        else:
            self.httpsicon.setPixmap(QPixmap(os.path.join('icons','Lock_Icon_24px.png')))
            
            
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)
    
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("%s - Web Browser" % title)
        
        
        
        
        

                            








app = QApplication(sys.argv)
app.setApplicationName('Web Browser')
app.setOrganizationName('Browser')
app.setOrganizationDomain('WebBrowser.org')
window = MainWindow()
window.show()
app.exec_()



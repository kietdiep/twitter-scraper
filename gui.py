import sqlite3
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QWidget
from PyQt5 import QtCore
import scraperDB as sb
import os 

# --------------------------------- Welcome Screen --------------------------------------------------#

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        loadUi("welcomescreen.ui",self)
        self.keyword.stateChanged.connect(self.uncheck)
        self.username.stateChanged.connect(self.uncheck)
        self.location.stateChanged.connect(self.uncheck)
        self.hashtag.stateChanged.connect(self.uncheck)
        
        self.keyword.stateChanged.connect(self.is_checked)
        self.username.stateChanged.connect(self.is_checked)
        self.location.stateChanged.connect(self.is_checked)
        self.hashtag.stateChanged.connect(self.is_checked)
               
        #takes in input variables
        
        self.search.clicked.connect(self.get_search_input)
        
        self.search.clicked.connect(self.completeSearch)

    def completeSearch(self):
        com_search = SearchScreen(self.filterCrit,self.userInput)
        widget.addWidget(com_search)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        


    #Problems with this code is that it takes two clicks to clear a checkbox
    #causes more problems with the is_checked function... will look into in future
    def uncheck(self):
        if self.sender() == self.keyword:
            self.username.setChecked(False)
            self.location.setChecked(False)
            self.hashtag.setChecked(False)
        elif self.sender() == self.username:
            self.keyword.setChecked(False)
            self.location.setChecked(False)
            self.hashtag.setChecked(False)
        elif self.sender() == self.location:
            self.keyword.setChecked(False)
            self.username.setChecked(False)
            self.hashtag.setChecked(False)
        elif self.sender() == self.hashtag:
            self.keyword.setChecked(False)
            self.username.setChecked(False)
            self.location.setChecked(False)

    #works first try but if you try to change your filter it will bug out
    def is_checked(self):
        if self.keyword.isChecked():
            self.filterCrit = 'k'
        elif self.username.isChecked():
            self.filterCrit = 'u'
        elif self.location.isChecked():
            self.filterCrit = 'c'
        elif self.hashtag.isChecked():
            self.filterCrit = '#'
        else:
            #default will be keyword
            self.filterCrit = 'not working'
        
    def get_search_input(self):
        self.userInput = self.inputField.text()
        

# --------------------------------- Search Screen --------------------------------------------------#

class SearchScreen(QDialog):
    def __init__(self, filterCrit, userInput):
        super(SearchScreen,self).__init__()
        loadUi("output.ui",self) 
        scraped = sb.Scraper(filterCrit,userInput)
        # scraper class obsolete here, could have just used a python file of just functions to create the database but will keep it as mental note for how i came to my solution
        self.loaddata()
        


    def loaddata(self):
        conn = sqlite3.connect("twitterInfo.db")
        cur = conn.cursor()
        sqlquery = "SELECT * FROM Tweet LIMIT 100"

        self.tableWidget.setRowCount(100)
        tablerow = 0
        for row in cur.execute(sqlquery):
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.tableWidget.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(row[8]))
            tablerow+=1







# --------------------------------- Main --------------------------------------------------#

#main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(731)
widget.setFixedWidth(941)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting")


import sqlite3
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QButtonGroup, QDialog, QApplication, QStackedWidget, QWidget
from PyQt5 import QtCore
import scraperDB as sb
import os

# --------------------------------- Welcome Screen --------------------------------------------------#


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("../ui/welcomescreen.ui", self)
        self.bg = QButtonGroup()
        self.bg.addButton(self.keyword, 1)
        self.bg.addButton(self.username, 2)
        self.bg.addButton(self.hashtag, 3)

        self.keyword.stateChanged.connect(self.is_checked)
        self.username.stateChanged.connect(self.is_checked)
        self.hashtag.stateChanged.connect(self.is_checked)

        self.search.clicked.connect(self.get_search_input)

        self.search.clicked.connect(self.completeSearch)

    def completeSearch(self):
        com_search = SearchScreen(self.filterCrit, self.userInput)
        widget.addWidget(com_search)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def is_checked(self):
        if self.keyword.isChecked():
            self.filterCrit = 'k'
        elif self.username.isChecked():
            self.filterCrit = 'u'
        elif self.hashtag.isChecked():
            self.filterCrit = '#'
        else:
            self.filterCrit = 'not working'

    def get_search_input(self):
        self.userInput = self.inputField.text()


# --------------------------------- Search Screen --------------------------------------------------#

class SearchScreen(QDialog):
    def __init__(self, filterCrit, userInput):
        super(SearchScreen, self).__init__()
        loadUi("../ui/output.ui", self)
        self.tableWidget.setColumnWidth(2, 350)
        scraped = sb.Scraper(filterCrit, userInput)
        # scraper class obsolete here, could have just used a python file of just functions to create the database but will keep it as mental note for how i came to my solution
        self.loaddata()
        self.search2.clicked.connect(self.goPrev)
        self.closebutton.clicked.connect(self.exit)

    def goPrev(self):
        if os.path.exists("twitterInfo.db"):
            os.remove("twitterInfo.db")
        else:
            print("The file does not exist")
        os.execl(sys.executable, sys.executable, *sys.argv)

    def exit(self):
        exit()

    def loaddata(self):
        conn = sqlite3.connect("twitterInfo.db")
        cur = conn.cursor()
        sqlquery = "SELECT * FROM Tweet LIMIT 100"

        self.tableWidget.setRowCount(100)
        tablerow = 0
        for row in cur.execute(sqlquery):
            self.tableWidget.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(
                tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(
                tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(
                tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(
                tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(
                tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.tableWidget.setItem(
                tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.tableWidget.setItem(
                tablerow, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.tableWidget.setItem(
                tablerow, 8, QtWidgets.QTableWidgetItem(row[8]))
            tablerow += 1


# --------------------------------- Main --------------------------------------------------#
if __name__ == "__main__":
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

from functools import partial
import random
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

#For loading QT design = pyside6-designer

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('form.ui',None)
        self.ui.show()
        self.game = [[self.ui.btn_1 , self.ui.btn_2 , self.ui.btn_3],
                    [self.ui.btn_4 , self.ui.btn_5 , self.ui.btn_6],
                    [self.ui.btn_7 , self.ui.btn_8 , self.ui.btn_9]]

        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('color: black ; background-color : skyblue')
                self.game[i][j].clicked.connect(partial(self.play, i , j))


        self.player = 'x'

        self.ui.btn_restart.clicked.connect(self.restart)
        self.ui.btn_about.clicked.connect(self.about)

        self.playerOne_score = 0
        self.playerTWo_score = 0
        self.draw = 0

    def play(self, i , j):
        if self.game[i][j].text()=='': #player Human
            if self.ui.btn_OneVsOne.isChecked():
                if self.player == 'X':
                    self.game[i][j].setText('X')
                    self.game[i][j].setStyleSheet('color : green ; background-color : lightgreen')
                    self.player = 'O'
                else:
                    self.player == 'O'
                    self.game[i][j].setText('O')
                    self.game[i][j].setStyleSheet('color : red ; background-color : pink')
                    self.player = 'X'

            if self.ui.btn_OneVsAI.isChecked(): #player AI     
                if self.player == "X":
                    self.game[i][j].setText("X")
                    self.game[i][j].setStyleSheet('color : green ; background-color : lightgreen')
                    self.player = "O"
                    
                elif self.player == "O":
                    while True:
                        i = random.randint(0, 2)
                        j = random.randint(0, 2)
                        if self.game[i][j].text() == "":
                            self.game[i][j].setText("O")
                            self.game[i][j].setStyleSheet('color : red ; background-color : pink')
                            self.player = "X"
                            break
                                               
        self.check()        
    #-----------------------------------------------------------------------------------------------#
    def check(self):
        
        if ((self.game[0][0].text()=='X' and self.game[0][1].text()=='X' and self.game[0][2].text()=='X') or 
            (self.game[1][0].text()=='X' and self.game[1][1].text()=='X' and self.game[1][2].text()=='X') or
            (self.game[2][0].text()=='X' and self.game[2][1].text()=='X' and self.game[2][2].text()=='X') or
            (self.game[0][0].text()=='X' and self.game[1][0].text()=='X' and self.game[2][0].text()=='X') or
            (self.game[0][1].text()=='X' and self.game[1][1].text()=='X' and self.game[2][1].text()=='X') or
            (self.game[0][2].text()=='X' and self.game[1][2].text()=='X' and self.game[2][2].text()=='X') or 
            (self.game[0][0].text()=='X' and self.game[1][1].text()=='X' and self.game[2][2].text()=='X')):
            self.playerOne_score += 1
            msgBox = QMessageBox()
            msgBox.setText('Player 1 wins')
            msgBox.exec()
            self.restart()
        elif ((self.game[0][0].text()=='O' and self.game[0][1].text()=='O' and self.game[0][2].text()=='O') or 
            (self.game[1][0].text()=='O' and self.game[1][1].text()=='O' and self.game[1][2].text()=='O') or
            (self.game[2][0].text()=='O' and self.game[2][1].text()=='O' and self.game[2][2].text()=='O') or
            (self.game[0][0].text()=='O' and self.game[1][0].text()=='O' and self.game[2][0].text()=='O') or
            (self.game[0][1].text()=='O' and self.game[1][1].text()=='O' and self.game[2][1].text()=='O') or
            (self.game[0][2].text()=='O' and self.game[1][2].text()=='O' and self.game[2][2].text()=='O') or 
            (self.game[0][0].text()=='O' and self.game[1][1].text()=='O' and self.game[2][2].text()=='O')):
            self.playerTWo_score += 1 
            msgBox = QMessageBox()
            msgBox.setText('Player 2 wins')
            msgBox.exec()
            self.restart()

        elif (self.game[0][0].text() != "" and self.game[0][1].text() != "" and self.game[0][2].text() != "" and 
            self.game[1][0].text() != "" and self.game[1][1].text() != "" and self.game[1][2].text() != "" and 
            self.game[2][0].text() != "" and self.game[2][1].text() != "" and self.game[2][2].text() != ""):
            self.draw += 1 
            msgBox = QMessageBox()
            msgBox.setText('draw')
            msgBox.exec()
            self.restart()

        self.ui.btn_score_1.setText(f' player one score \n{self.playerOne_score}')
        self.ui.btn_score_2.setText(f' player two score \n{self.playerTWo_score}')
        #-----------------------------------------------------------------------------------------------#
    def restart(self):
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('color: black ; background-color : skyblue')
                self.game[i][j].clicked.connect(partial(self.play, i , j))


    def about(self):
        msgBox = QMessageBox()
        msgBox.setText('made by arash at 2022')
        msgBox.exec()

app = QApplication([])
window = TicTacToe()
app.exec()
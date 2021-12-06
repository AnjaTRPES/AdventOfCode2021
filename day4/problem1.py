# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

class pos:
    def __init__(self, pos):
        self.values = [pos, False]
    
    def mark(self):
        self.values[1] = True
    
    def isMarked(self):
        return self.values[1]
    
    def getValue(self):
        return self.values[0]

class Board:
    def __init__(self, listNumbers):
        self.bingoBoard = []
        for boardLine in listNumbers:
            b = [pos(i) for i in boardLine]
            self.bingoBoard.append(b)
            
    def mark(self, value):
        for boardLine in self.bingoBoard:
            for boardPos in boardLine:
                if boardPos.getValue() == value:
                    boardPos.mark()
                    
    def isWinner(self):
        posit = [0, 1, 2, 3, 4]
        # check the horizontal winners
        for b in self.bingoBoard:
            if (all([b[pos].isMarked() for pos in posit]) == True):
                return True
        # check the columns
        for b in posit:
            if (all([self.bingoBoard[pos][b].isMarked() for pos in posit]) == True):
                return True
        return False
    
    def sumUnmarked(self):
        sumUnmarked = 0
        for b in self.bingoBoard:
            for val in b:
                if (val.isMarked() == False):
                    sumUnmarked += val.getValue()
        return sumUnmarked
    
    def __str__(self):
        returnStr = "["
        for b in self.bingoBoard:
            returnStr += "["
            for pos in b:
                if pos.isMarked():
                    returnStr += "*" + str(pos.getValue()) +" "
                else:
                    returnStr += " " + str(pos.getValue()) +" "
            returnStr += "]\n"
        returnStr += "]\n"
        return returnStr


def loadFile(filename):
    # load the random numbers
    f = open(filename)
    lines = f.readlines()
    f.close()
    random_numbers = [int(i) for i in lines[0].split(',')]
    # get the boards
    boards = []
    tempBoardInput = []
    for line in lines[2:]:
        #print(line)
        if line != '\n':
            tempBoardInput.append([int(i) for i in line.split(' ') if i != ''])
        else:
            boards.append(Board(tempBoardInput))
            tempBoardInput = []
    boards.append(Board(tempBoardInput))
    return random_numbers , boards

def playBingo(randomNumbers, boards):
    winner = False
    winningBoard = None
    posRandom = -1
    
    while (winner == False) and (posRandom < len(randomNumbers)):
        print('first round!', posRandom)
        # draw a number!
        posRandom += 1
        number = randomNumbers[posRandom]
        # mark and check if there is a winner
        for board in boards:
            board.mark(number)
            if (board.isWinner() == True):
                print('foundWinner???')
                winningBoard = board
                winner = True
                break
    return randomNumbers[posRandom], winningBoard

def getWinningScore(finalNumber, winningBoard):
    # Sum of all unmarked numbers
    sumUnmarked = winningBoard.sumUnmarked()
    return finalNumber * sumUnmarked

randomNumbers, boards = loadFile('input.txt')
finalNumber, winningBoard = playBingo(randomNumbers, boards)
print('final score: ', getWinningScore(finalNumber, winningBoard))



















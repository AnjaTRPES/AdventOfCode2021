# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 22:33:37 2021

@author: Anja
"""
from collections import Counter


class Player:
    def __init__(self, pos, score=0):
        self.score = score
        self.pos = pos
        
    def move(self, dieAmount):
        newPos = (self.pos + dieAmount)%10
        self.pos = newPos
        if newPos == 0:
            self.score += 10
        else:
            self.score += self.pos

def getNewPosScore(dieAmount, pos, score):
    newPos = (pos + dieAmount)%10
    if newPos == 0:
        return newPos, score+10
    else:
        return newPos, score+newPos

diracRollSums = []
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            diracRollSums.append(i+j+k)

diracDies = Counter(diracRollSums)

start = (6, 0, 1, 0) #player1pos, player1score, player2pos, player2score
playC = Counter([start])
player1WonC = Counter()
player2WonC = Counter()

sumPlayer1Won = 0
sumPlayer2Won = 0

endScore = 21
player1Turn = True

allFinished = False
while len(playC) != 0:
    intermC = Counter()
    for key in playC:
        if playC[key] != 0:
            for dieAm in diracDies.keys():
                if player1Turn:
                    p1pos, p1score = getNewPosScore(dieAm, key[0], key[1])
                    if p1score >= endScore:
                        player1WonC[(p1pos, p1score, key[2], key[3])] += playC[key]*diracDies[dieAm]
                        sumPlayer1Won += playC[key]*diracDies[dieAm]
                    else:
                        intermC[(p1pos, p1score, key[2], key[3])] += playC[key]*diracDies[dieAm]
                else:
                    p2pos, p2score = getNewPosScore(dieAm, key[2], key[3])
                    if p2score >= endScore:
                        player2WonC[(key[0], key[1], p2pos, p2score)] += playC[key]*diracDies[dieAm]
                        sumPlayer2Won += playC[key]*diracDies[dieAm]
                    else:
                        intermC[(key[0], key[1], p2pos, p2score)] += playC[key]*diracDies[dieAm]
    if player1Turn == True:
        player1Turn = False
    else:
        player1Turn = True
    playC = intermC

#Count how many games each
print('player1 won in ', sumPlayer1Won, ' player 2 in ', sumPlayer2Won)
print('player1 won more?')

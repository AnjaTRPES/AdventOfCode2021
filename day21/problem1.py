# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 22:33:37 2021

@author: Anja
"""

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

        
player1 = Player(6)
player2 = Player(1)

player1Turn = True
gameEnd = False
endScore = 1000
threeDie = []

dierolled = 0
    
while gameEnd is False:
    #print('Player1: ', player1.score, 'Player2', player2.score)
    for i in range(1,101):
        threeDie.append(i)
        dierolled += 1
        if len(threeDie) == 3:
            dieSum = sum(threeDie)
            threeDie = []
            if player1Turn:
                player1.move(dieSum)
                player1Turn = False
            else:
                player2.move(dieSum)
                player1Turn = True
            if player1.score >= 1000:
                gameEnd = True
                print('player1 won!')
                break
            if player2.score >= 1000:
                gameEnd = True
                print('player2 won!')
                break
def finalScore(player, dieRolled):
    print(dieRolled*player.score)

print('player 1  ')
finalScore(player1, dierolled)
print('player 2  ')
finalScore(player2, dierolled)


tPlayer = Player(7)
tPlayer.move(5)
#print(tPlayer.score, tPlayer.pos)
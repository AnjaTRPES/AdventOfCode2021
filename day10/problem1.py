# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 09:45:01 2021

@author: Anja
"""


def loadLines(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    return lines


def isValid(line):
    openers = '([{<'
    closers = ')]}>'
    
    charStack = []
    for char in line:
        if char in openers:
            charStack.append(closers[openers.find(char)])
        if char in closers:
            if len(charStack) == 0:
                print('weird, weird.. whats the score?')
            else:
                lastChar = charStack.pop()
                if lastChar != char:
                    print('corrupted line!')
                    if (char == ')'):
                        return 3
                    elif (char == ']'):
                        return 57
                    elif (char == '}'):
                        return 1197
                    elif (char == '>'):
                        return 25137
                    break
    return 0
    
def getSyntaxScore(lines):
    score = 0
    for line in lines:
        score += isValid(line)
    return score


def getIncompleteLines(lines):
    for n in range(len(lines)-1, -1, -1):
        if isValid(lines[n]) != 0:
            lines.pop(n)
    return lines

def getCompletionScoreLine(line):
    openers = '([{<'
    closers = ')]}>'
    
    charStack = []
    for char in line:
        if char in openers:
            charStack.append(closers[openers.find(char)])
        if char in closers:
            if len(charStack) == 0:
                print('weird, weird.. whats the score?')
            else:
                lastChar = charStack.pop()
    score = 0
    scoreDict = {')': 1, ']': 2, '}': 3, '>': 4}
    #print(charStack)
    for char in charStack[::-1]:
        score *= 5
        score += scoreDict[char]
        #print('after ', char, ' score ', score)
    return score

def getCompletionScore(lines):
    totalScore = []
    for line in lines:
        totalScore.append(getCompletionScoreLine(line))
    totalScore.sort()
    return totalScore[int(len(totalScore)/2)]

lines = loadLines('input.txt')
print(len(lines))
#print(getSyntaxScore(lines))
getIncompleteLines(lines)
print(getCompletionScore(lines))
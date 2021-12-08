# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 12:58:29 2021

@author: Anja
"""

class entry:
    def __init__(self, segments, output):
        self.segments = segments
        self.output = output
        
        
        self.oDigits = {'abcefg': 0, 'cf': 1 , 'acdeg': 2, 'acdfg': 3, 
                        'bcdf': 4, 'abdfg': 5, 'abdefg': 6, 'acf': 7,
                        'abcdefg': 8, 'abcdfg': 9}
        
        self.decoderDict, self.encoderDict = self.decodeDicts()
        
        self.decodedOutput = int(self.decodeOutput())
        
    def decodeOutput(self):
        decodedOutput = ''
        for o in self.output:
            decoded = ''
            for s in o:
                decoded += self.decoderDict[s]
            sortedList = sorted(decoded)
            
            decodedOutput += str(self.oDigits["".join(sortedList)])
        return decodedOutput
        
    def getLenArrays(self):
        h = self.segments[:]
        h.extend(self.output)
        twoLen = [s for s in h if len(s)==2]
        threeLen = [s for s in h if len(s)==3]
        fourLen = [s for s in h if len(s)==4]
        fiveLen = [s for s in h if len(s)==5]
        sixLen = [s for s in h if len(s)==6]
        sevenLen = [s for s in h if len(s)==7]
        return twoLen, threeLen, fourLen, fiveLen, sixLen, sevenLen
        
        
    def decodeDicts(self):
        #for decoding use both the segments and the final numbers!
        twoLen, threeLen, fourLen, fiveLen, sixLen, sevenLen = self.getLenArrays()
        
        decoderDict = {}
        encoderDict = {}
        
        decoderDict[self.getStringDiff(twoLen[0], threeLen[0])] = 'a' #only possibility for a
        encoderDict['a'] = self.getStringDiff(twoLen[0], threeLen[0])
        #print('what is the encoderDict now', encoderDict, twoLen, threeLen)
        #now for g -> there is one 6len-4len with 2 letters of difference, a and g:
        for six in sixLen:
            diff = self.getStringDiff(six, fourLen[0])
            if len(diff) == 2:
                #print('found G')
                gCode = self.getStringDiff(diff, encoderDict['a'])
                decoderDict[gCode] = 'g'
                encoderDict['g'] = gCode
        # now I can get e from the difference of 8(len 7) and 4(len 4)
        diff = self.getStringDiff(sevenLen[0], fourLen[0])
        eCode = self.getStringDiff(diff, encoderDict['a']+encoderDict['g'])
        decoderDict[eCode] = 'e'
        encoderDict['e'] = eCode
        #now for d -> there is one 5len-3len difference with 2 letters, d and g
        for five in fiveLen:
            diff = self.getStringDiff(five, threeLen[0])
            if len(diff) == 2:
                #print('found D!')
                dCode = self.getStringDiff(diff, encoderDict['g'])
                decoderDict[dCode] = 'd'
                encoderDict['d'] = dCode
        #Now that I know a, d, e G, One of the fiveLetters (acdeg) is only one difference!
        for five in fiveLen:
            diff = self.getStringDiff(five, encoderDict['a']+encoderDict['d']+encoderDict['e']+encoderDict['g'])
            if len(diff) == 1:
                #print('found C!')
                decoderDict[diff] = 'c'
                encoderDict['c'] = diff
        #Knowing c, I can get f from the number 1
        fCode = self.getStringDiff(twoLen[0], encoderDict['c'])
        decoderDict[fCode] = 'f'
        encoderDict['f'] = fCode
        #and now the last one is easypeasy:
        bCode = self.getStringDiff(sevenLen[0], 
                                   encoderDict['a']+encoderDict['c']+encoderDict['d']+encoderDict['e']+encoderDict['f']+encoderDict['g'])
        decoderDict[bCode] = 'b'
        encoderDict['b'] = bCode
        return decoderDict, encoderDict
        
    def getStringDiff(self, string1, string2):
        diffChar = ''
        for s in string1:
            if s not in string2:
                diffChar += s
        for s in string2:
            if s not in string1:
                diffChar += s
        return diffChar
        
        
     
    def __str__(self):
        return str(self.segments) + '|' + str(self.output)


def loadFile(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    entries =  []
    for line in lines:
        splitted = line[:-1].split(' | ')
        entries.append(entry(splitted[0].split(' '), splitted[1].split(' ')))
    return entries

def getEasyDigits(entries):
    Neasy = 0
    for entry in entries:
        #print(entry)
        for o in entry.output:
            if len(o) in [2, 3, 4, 7]:
                #print(o)
                Neasy += 1
    return Neasy


def getOutputSum(entries):
    outpSum = 0
    for entry in entries:
        outpSum += entry.decodedOutput
    return outpSum        

entries = loadFile('input.txt')
print(getOutputSum(entries))




#print('Neasy', getEasyDigits(entries))

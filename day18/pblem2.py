# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 18:06:24 2021

@author: Anja
"""

from collections import deque

class SnailNumber:
    
    def __init__(self, sNString, parent = None):
        self.parent = parent
        # three limiting cases: [a, b], [[a,b], a], [a, [a,b]]
        if sNString.count(',') == 1:
            sNList = sNString.split(',')
            self.left = int(sNList[0][1:])
            self.right = int(sNList[1][:-1])
        else:
            leftD = deque()
            leftStr = []
            for i, h in enumerate(sNString[1:]):
                if h == '[':
                    leftD.append(h)
                elif h == ',':
                    if len(leftD) == 0:
                        break
                elif h == ']':
                    leftD.pop()
                leftStr.append(h)
            left = ''.join(leftStr)
            right = sNString[i+2:-1]
        
            if left.isnumeric():
                self.left = int(left)
            else:
                self.left = SnailNumber(left, parent=self)
            if right.isnumeric():
                self.right = int(right)
            else:
                self.right = SnailNumber(right, parent = self)
        
    def __repr__(self):
        return '['+str(self.left)+','+str(self.right)+']'
    
    def add2Right(self, number):
        if type(self.right) == int:
            self.right += number
        else:
            self.right.add2Right(number)
    
    def __add__(self, other):
        newNumber = SnailNumber('[1,1]', parent=None)
        newNumber.left = self
        self.parent = newNumber
        newNumber.right = other
        other.parent = newNumber
        #print('before reducing: ', newNumber)
        newNumber.reduce()
        #print('after reducing:  ', newNumber)
        return newNumber
    
    def reduce(self):
        reducingPossible = True
        while reducingPossible:
            explodedOnce = False
            splittedOnce = False
            exploded = True
            while exploded:
                exploded = self.explode()
                #print('exploded?', exploded)
                if exploded is True:
                    #print('exploded!!')
                    explodedOnce = True
            splittedOnce = self.split()
            #if splittedOnce:
            #    print('splitted!')
            if (splittedOnce is False) and (explodedOnce is False):
                reducingPossible = False
            
    def magnitude(self):
        if type(self.left) == int:
            magLeft = 3*self.left
        else:
            magLeft = 3*self.left.magnitude()
        if type(self.right) == int:
            magRight = 2*self.right
        else:
            magRight = 2*self.right.magnitude()
        return magLeft+magRight
    
    def goUpLeft(self, number):
        if self.parent == None:
            pass # can't add
        elif self.parent.left != self:
            #aha, I can go down!!
            if type(self.parent.left) == int:
                self.parent.left += number
            else:
                self.parent.left.add2Right(number)
        else:
            self.parent.goUpLeft(number)
    
    def add2Left(self, number):
        if type(self.left) == int:
            self.left += number
        else:
            self.left.add2Left(number)
    
    def goUpRight(self, number):
        if self.parent == None:
            pass #nope, can't add
        elif self.parent.right != self:
            #aha, can go dwon!
            if type(self.parent.right) == int:
                self.parent.right += number
            else:
                self.parent.right.add2Left(number)
        else:
            self.parent.goUpRight(number)
    
    def replaceWith0(self):
        if self.parent.left == self:
            self.parent.left = 0
        if self.parent.right == self:
            self.parent.right = 0
    
    def explode(self, depth = 0, exploded = False):
        if depth == 4:
            #time to explode!
            #print('boooom!')
            self.goUpLeft(self.left)
            self.goUpRight(self.right)
            self.replaceWith0()
            return True
        
        if type(self.left) != int:
            exploded = self.left.explode(depth+1)
            if exploded is False:
                if type(self.right) != int:
                    exploded = self.right.explode(depth+1)
        elif type(self.right) != int:
            exploded = self.right.explode(depth+1)
        return exploded

    def newPair(self, number):
        newPair = SnailNumber('[1,1]', parent=self)
        newPair.left = int(number/2)
        newPair.right = number - newPair.left
        return newPair
            
    def split(self):
        #traverse the tree from left to right
        if type(self.left) == int:
            #print('checking left: ', self.left)
            if self.left >= 10:
                self.left = self.newPair(self.left)
                return True
            elif type(self.right) == int:
                if self.right >= 10:
                    self.right = self.newPair(self.right)
                    return True
                else:
                    return False
            else:
                return self.right.split()
        else:
            #print('left', self.left)
            splitted = self.left.split()
            if splitted == False:
                #print('right!', self.right)
                if type(self.right) == int:
                    #print('checking right: ', self.right)
                    if self.right >= 10:
                        self.right = self.newPair(self.right)
                        return True
                    else:
                        return False
                else:
                    splitted = self.right.split()
            return splitted
        

sNumberEx = ['[1,2]', 
             '[[1,2],3]',
             '[9,[8,7]]',
             '[[1,9],[8,5]]',
             '[[[[1,2],[3,4]],[[5,6],[7,8]]],9]',
             '[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]',
             '[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]']

for n in sNumberEx:
    snailNumber = SnailNumber(n)
    #print(snailNumber, n)
    assert str(snailNumber) == n
print('can load snail Numbers')

explodeEx = [
    ('[[[[[9,8],1],2],3],4]', '[[[[0,9],2],3],4]'),
    ('[7,[6,[5,[4,[3,2]]]]]', '[7,[6,[5,[7,0]]]]'),
    ('[[6,[5,[4,[3,2]]]],1]', '[[6,[5,[7,0]]],3]'),
    ('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]', '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'),
    ('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]', '[[3,[2,[8,0]]],[9,[5,[7,0]]]]')
    #('[[[[4,0],[5,0]],[[[4,5],[2,6]],1]],1]', '[1,1]')
    ]

for n in explodeEx:
    snailNumber = SnailNumber(n[0])
    #print('\n\nbe', snailNumber)
    snailNumber.explode()
    #print('  ', snailNumber)
    #print('? ', str(SnailNumber(n[1])))
    #print('??', n)
    assert str(SnailNumber(n[1])) == str(snailNumber) 
print('explosions seem to work fine')

splitEx = [('[[[[0,7],4],[15,[0,13]]],[1,1]]', '[[[[0,7],4],[[7,8],[0,13]]],[1,1]]'),
           ('[[[[0,7],4],[[7,8],[0,13]]],[1,1]]', '[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]')
    ]
for n in splitEx:
    snailNumber = SnailNumber(n[0])
    #print('\n\nbe', snailNumber)
    snailNumber.split()
    #print('  ', snailNumber)
    #print('? ', str(SnailNumber(n[1])))
    #print('??', n)
    assert str(SnailNumber(n[1])) == str(snailNumber) 
print('splitting seem to work fine')


print("Checking the sums now!")
finalSumEx = [
    ('[[[[4,3],4],4],[7,[[8,4],9]]]\n[1,1]', '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'),
    ('[1,1]\n[2,2]\n[3,3]\n[4,4]', '[[[[1,1],[2,2]],[3,3]],[4,4]]'),
    ('[1,1]\n[2,2]\n[3,3]\n[4,4]\n[5,5]', '[[[[3,0],[5,3]],[4,4]],[5,5]]'),
    ('[1,1]\n[2,2]\n[3,3]\n[4,4]\n[5,5]\n[6,6]', '[[[[5,0],[7,4]],[5,5]],[6,6]]'),
    ('[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]\n[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]',
     '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]')
    ]

for ex in finalSumEx:
    numbers = [SnailNumber(e) for e in ex[0].split('\n')]
    
    startNumber = numbers[0]
    
    #print('\n\nstart         ', startNumber)
    startNumber.reduce()
    #print('startReduced: ', startNumber)

    if len(numbers) > 2:
        for number in numbers[1:]:
            number.reduce()
            startNumber = startNumber + number
    else:
        startNumber = startNumber + numbers[1]
    #print('end ', startNumber)
    #print('??  ', str(SnailNumber(ex[1])))
    assert str(startNumber) == str(SnailNumber(ex[1]))

print('successfully checked the sums')

print('######## Checking the sample')
def loadNumbers(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    numbers = []
    for line in lines:
        line = line.rstrip()
        numbers.append(SnailNumber(line))
    return numbers
numbers = loadNumbers('sample.txt')
exp_result = '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'
starting_number = numbers[0]
#print('  ', starting_number)
for number in numbers[1:]:
    #print('+  ', number)
    starting_number = starting_number + number
    #print('= ', starting_number)

assert str(starting_number) == str(SnailNumber(exp_result))
print('sample worked!')

print('magnitude?')

magnitudeEx = [
    ('[9,1]', 29),
    ('[1,9]', 21),
    ('[[9,1],[1,9]]', 129),
    ('[[1,2],[[3,4],5]]', 143),
    ('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]', 1384),
    ('[[[[1,1],[2,2]],[3,3]],[4,4]]', 445),
    ('[[[[3,0],[5,3]],[4,4]],[5,5]]', 791),
    ('[[[[5,0],[7,4]],[5,5]],[6,6]]', 1137),
    ('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]', 3488)
    ]

for ex in magnitudeEx:
    sNumber = SnailNumber(ex[0])
    assert sNumber.magnitude() == ex[1]
    
print('######## Checking the sample 2')
def loadNumbers(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    numbers = []
    for line in lines:
        line = line.rstrip()
        numbers.append(SnailNumber(line))
    return numbers
numbers = loadNumbers('sample2.txt')

magNumber = 0
n1 = None
n2 = None
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j:
            newNumber = SnailNumber(str(numbers[i])) + SnailNumber(str(numbers[j]))
            mag = newNumber.magnitude()
            if mag > magNumber:
                n1 = i
                n2 = j
                magNumber = mag

print('sample worked!', magNumber)


print('input!')
def loadNumbers(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    numbers = []
    for line in lines:
        line = line.rstrip()
        numbers.append(SnailNumber(line))
    return numbers
numbers = loadNumbers('input.txt')

magNumber = 0
n1 = None
n2 = None
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j:
            newNumber = SnailNumber(str(numbers[i])) + SnailNumber(str(numbers[j]))
            mag = newNumber.magnitude()
            if mag > magNumber:
                n1 = i
                n2 = j
                magNumber = mag
print('input largest mag', magNumber)
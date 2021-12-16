# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 07:15:17 2021

@author: Anja
"""

Hex2Bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
    }

def convertHex2Bin(packet, Hex2Bin):
    binary = []
    for p in packet:
        binary.append(Hex2Bin[p])
    return ''.join(binary)


class Packet:
    def __init__(self, version, typeId, content):
        self.version = version 
        self.typeId = typeId
        self.content = content
    
    def __repr__(self):
        return 'Packet[v'+str(self.version)+', t'+str(self.typeId)+', c='+str(self.content)+']'
    
    def getVersionSum(self):
        return self.version
    
    def getValue(self):
        return self.content

class OperatorPacket:
    def __init__(self, version, typeId, lengthId, length, content):
        self.version = version
        self.typeId = typeId
        self.lengthId = lengthId
        self.length = length
        self.content = content
    
    def __repr__(self):
        rS = 'OPacket{v'+str(self.version)+', t'+str(self.typeId)
        rS = rS + ', Li'+str(self.lengthId)+', l'+str(self.length)
        return rS + 'c='+ str(self.content) + '}'
    
    def getVersionSum(self):
        sumV = self.version
        for c in self.content:
            sumV += c.getVersionSum()
        return sumV
    
    def getValue(self):
        
        if self.typeId == 0:
            return sum([c.getValue() for c in self.content])
        elif self.typeId == 1:
            val = 1
            for c in self.content:
                val *= c.getValue()
            return val
        elif self.typeId == 2:
            return min([c.getValue() for c in self.content])
        elif self.typeId == 3:
            return max([c.getValue() for c in self.content])
        elif self.typeId == 5:
            valPacket1 = self.content[0].getValue()
            valPacket2 = self.content[1].getValue()
            if valPacket1 > valPacket2:
                return 1
            else:
                return 0
        elif self.typeId == 6:
            valPacket1 = self.content[0].getValue()
            valPacket2 = self.content[1].getValue()
            if valPacket1 < valPacket2:
                return 1
            else:
                return 0
        elif self.typeId == 7:
            valPacket1 = self.content[0].getValue()
            valPacket2 = self.content[1].getValue()
            if valPacket1 == valPacket2:
                return 1
            else:
                return 0

def decodeSinglePacket(binaryPacket):
    version = int(binaryPacket[:3], 2)
    typeId = int(binaryPacket[3:6], 2) # int(number, 2)
    #print('version: ', version, 'typeId: ', typeId)
    binaryPacket = binaryPacket[6:]
    if typeId == 4: #literal value
        groups4bits = []
        while True:
            if len(binaryPacket) < 5:
                print('len of packet reached')
                break
            groups4bits.append(binaryPacket[1:5])
            if binaryPacket[0] == '0':
                binaryPacket = binaryPacket[5:]
                break
            binaryPacket = binaryPacket[5:]
        litValue = ''.join(groups4bits)
        return Packet(version, typeId, int(litValue, 2)), binaryPacket 

    else: #operator!
        #print('its an operator')
        lengthTypeId = binaryPacket[0]
        if lengthTypeId == '0':
            totalLengthOfBites = int(binaryPacket[1:16], 2)
            #print('LenBites: ', totalLengthOfBites)
            binaryPacket = binaryPacket[16:]
            subpackets = []
            subpacketBinaries = binaryPacket[:totalLengthOfBites]
            while (len(subpacketBinaries) > 5): #for it to be a valid packet?
                #print('new packet!')
                newPacket, newBinary = decodeSinglePacket(subpacketBinaries)
                subpackets.append(newPacket)
                subpacketBinaries = newBinary
            binaryPacket = binaryPacket[totalLengthOfBites:]
            #print('version here', version)
            return OperatorPacket(version, typeId, lengthTypeId, totalLengthOfBites, subpackets), binaryPacket
            
            #go in chuncks of 15 if you can, otherwise take the rest
            
        else:
            NsubPackets = int(binaryPacket[1:12], 2)
            #print('NsubPackets: ', NsubPackets)
            binaryPacket = binaryPacket[12:]
            subpackets = []
            for n in range(NsubPackets):
                newPacket, newBinary = decodeSinglePacket(binaryPacket)
                subpackets.append(newPacket)
                binaryPacket = newBinary
            return OperatorPacket(version, typeId, lengthTypeId, NsubPackets, subpackets), binaryPacket


def ShowExample(packet, Hex2Bin):
    samplePacket1Binary = convertHex2Bin(packet, Hex2Bin)
    #print(samplePacket1Binary)
    packetSample, remainingBinary = decodeSinglePacket(samplePacket1Binary)
    #print(packetSample)
    #print('---versionSum: ', packetSample.getVersionSum())
    print('---value: ', packetSample.getValue())
    

examples = ['C200B40A82',
            '04005AC33890',
            '880086C3E88112',
            'CE00C43D881120',
            'D8005AC2A8F0',
            'F600BC2D8F',
            '9C005AC2F8F0',
            '9C0141080250320F1802104A08'
            ]

for i, ex in enumerate(examples):
    print('\n#######   example ', i+1)
    ShowExample(ex, Hex2Bin)


print('for the input')
f = open('input.txt')
lines = f.readlines()
f.close()
packet = lines[0].rstrip()
ShowExample(packet, Hex2Bin)

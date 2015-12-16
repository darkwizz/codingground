import polynomDivider as div
import math

#isn't used now
_simplePolynomsTable = {
    2: { 1: '111' },
    3: { 1: '1011', 3: '1101' },
    4: { 1: '10011', 3: '11111', 5: '111', 7: '11001' },
    5: { 1: '100101', 3: '111101', 5: '110111', 7: '101111', 9: '110111', 11: '111011' },
    6: { 1: '1000011', 3: '1010111', 5: '1100111', 7: '1001001', 9: '1101', 11: '1101101' },
    7: { 1: '10001001', 3: '10001111', 5: '10011101', 7: '11110111', 9: '10111111', 11: '11010101', 13: '10000011' },
    8: { 1: '100011101', 3: '101110111', 5: '111110011', 7: '101101001', 9: '110111101', 11: '111100011', 13: '100101011' }
}

def isPrime(number):
    i = 2
    while i * i < number:
        if number % i == 0:
            return False
        i += 1
    return True

def isAllowed(length):
    sLength = bin(length + 1)[2:]
    return sLength.count('1') == 1 and length != 1

def multiplyPolynoms(left, right):
    bRight = bin(right)[2:]
    parts = []
    for i in range(len(bRight), 0, -1):
        if bRight[i - 1] == 0:
            parts.append(0)
            continue
        part = left << (i - 1)
        parts.append(part)
    res = 0
    for part in parts:
        res ^= part
    return res

def getCreatingPolynom(polynoms):
    count = len(polynoms)
    resPolynom = polynoms[0]
    for i in range(1, count):
        iResPolynom = int(resPolynom, 2)
        iRight = int(polynoms[i], 2)
        resPolynom = multiplyPolynoms(iResPolynom, iRight)
    return resPolynom

def getMinimalPolynoms(fullCodeLength, mistakesCount):
    polynoms = []
    highestDegree = math.log(fullCodeLength + 1, 2)
    for i in range(mistakesCount):
        lastPolynom = 2 << int(highestDegree)
        lastPolynom -= 1
        highestDegree -= 1
        for j in range(lastPolynom, 0, -1):
            if isPrime(j):
                polynom = j
                polynoms.append(bin(polynom)[2:])
                break
    return polynoms

def getBitsList(polynom):
    bits = bin(polynom)[2:]
    res = [int(x) for x in bits]
    return res

def addBits(left, right):
    temp = left
    if len(left) < len(right):
        left = right
        right = temp
    res = left[:]
    for i in range(-1, -len(right), -1):
        res[i] = int(res[i]) ^ int(right[i])
    return res

def getB4HCode(inputBits, fullCodeLength, mistakesCount):
    controlBitsCount = fullCodeLength - len(inputBits)
    minimalPolynoms = getMinimalPolynoms(fullCodeLength, mistakesCount)
    creatingPolynom = getCreatingPolynom(minimalPolynoms)
    if type(inputBits) == type(''):
        inputBits += ('0' * controlBitsCount)
    else:
        inputBits.extend([0] * controlBitsCount)
    rest = div.getRest(inputBits, getBitsList(creatingPolynom))
    result = addBits(inputBits, rest)
    return result

if __name__ == "__main__":
    inputBits = [1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,0,1]
    codeLength = 31
    mistakesCount = 2
    print getB4HCode(inputBits, codeLength, mistakesCount)
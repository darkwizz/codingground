import polynomDivider as div
import math

def isPrime(number):
    i = 2
    while i * i < number:
        if number % i == 0:
            return False
        i += 1
    return True

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

def getCreatingPolynom(*polynoms):
    count = len(polynoms)
    resPolynom = polynoms[0]
    for i in range(1, count):
        resPolynom = multiplyPolynoms(resPolynom, polynoms[i])
    return resPolynom

def getMinimalPolynoms(fullCodeLength, mistakesCount):
    polynoms = []
    highestDegree = math.log(fullCodeLength + 1.0, 2)
    if highestDegree > int(highestDegree):
        highestDegree = int(highestDegree) + 1
    lastPolynom = 2 ** highestDegree
    for i in range(mistakesCount):
        polynom = 0
        for j in range(lastPolynom, 0, -1):
            if isPrime(j):
                polynom = j
                lastPolynom = polynom
                polynoms.append(bin(polynom)[2:])
                break
    return polynoms

def getBitsList(polynom):
    bits = bin(polynom)[2:]
    res = [x for x in bits]
    return res

def addBits(left, right):
    temp = left
    if len(left) < len(right):
        left = right
        right = temp
    res = left[:]
    for i in range(-1, -len(right), -1):
        res[i] = (int)res[i] ^ (int)right[i]
    return res

def getB4HCode(inputBits, fullCodeLength, mistakesCount):
    controlBitsCount = fullCodeLength - len(inputBits)
    minimalPolynoms = getMinimalPolynoms(fullCodeLength, mistakesCount)
    creatingPolynom = getCreatingPolynom(minimalPolynoms)
    if type(inputBits) == type(''):
        inputBits += ('0' * controlBitsCount)
    else:
        inputBits.extend([0] * controlBitsCount)
    rest = getRest(inputBits, getBitsList(creatingPolynom)
    result = addBits(inputBits, rest)
    return result

if __name__ == "__main__":
    inputBits = []
    codeLength = 31
    mistakesCount = 2

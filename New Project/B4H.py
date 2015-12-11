import polynomDivider as div
import math

def isPrime(number):
    end = int(number ** 0.5)
    for i in range(end):
        if number % i == 0:
            return True
    return False

def getPrime(lastPrime = 2):
    if lastPrime < 2:
        return 2
    for i in range(lastPrime ** 2):
        if isPrime(lastPrime):
            return i
    return None

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

def getCreatingPolynom(fullCodeLength, mistakesCount):
    h = math.log(fullCodeLength + 1.0, 2)
    if h > int(h):
        h = int(h) + 1
    codeLength = 2 * mistakesCount + 1
    polynomDegree = 2 * mistakesCount - 1
    polynom = 0
    

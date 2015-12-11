import polynomDivider as div
import math

def isPrime(number):
    end = int(number ** 0.5)
    for i in range(2, end + 1):
        if number % i == 0:
            return True
    return False

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
    lastPolynom = 2 ** (mistakesCount * 2 - 1)
    for i in range(mistakesCount):
        polynom = 0
        for j in range(lastPolynom, 0, -1):
            if isPrime(j):
                polynom = j
                lastPolynom = polynom
                polynoms.append(bin(polynom)[2:])
                break
    return polynoms

__author__ = 'artur'

_systems = [
    [4, 2, 2, 1], [6, 4, 2, 1], [7, 3, 2, 1], [6, 2, 2, 1]
]

def toDecimal(inputBits):
    res = ''
    for bit in inputBits:
        res += str(bit)
    return int(res, 2)

def encode(inputBits, binaryDecimalSystemIndex):
    if binaryDecimalSystemIndex < 0 or binaryDecimalSystemIndex >= len(_systems):
        return 'out of binary decimal systems range'
    res = []
    decNum = str(toDecimal(inputBits))
    for num in decNum:
        temp = int(num)
        log = str(temp) + ' = '
        for system in _systems[binaryDecimalSystemIndex]:
            div = temp / system
            if div > 1:
                div = 1
            log += (str(system) + '*' + str(div) + ' ')
            temp -= (system * div)
            res.append(div)
        print log
    return res

def decode(inputCode, binaryDecimalSystemIndex):
    if binaryDecimalSystemIndex < 0 or binaryDecimalSystemIndex >= len(_systems):
        return 'out of binary decimal systems range'
    tetradeSize = 4
    if len(inputCode) % tetradeSize:
        return 'incorrect length of code. Must be dividable by 4'
    strRes = ''
    startIndex = 0
    system = _systems[binaryDecimalSystemIndex]
    for i in range(1, len(inputCode) + 1):
        if i % tetradeSize == 0:
            ls = [str(x) for x in inputCode[startIndex : i]]
            log = ''
            for bit in ls:
                log += bit
            log += ' = '
            tempSum = 0
            for (x, y) in zip(system, inputCode[startIndex : i]):
                log += (str(x) + '*' + str(y) + ' ')
                tempSum += (x * y)
            log += ('= ' + str(tempSum))
            print log
            startIndex = i
            strRes += str(tempSum)
    return int(strRes)

if __name__ == '__main__':
    bits = [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
    print encode(bits, 3)
    print
    code = [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
    print decode(code, 3)

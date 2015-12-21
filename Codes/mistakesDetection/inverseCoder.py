__author__ = 'artur'

def encode(inputBits):
    counter = 0
    for bit in inputBits:
        counter += int(bit)
    res = inputBits[:]
    counter &= 1
    res.extend([x ^ counter for x in inputBits]) # if counter == 0 then no changes otherwise it'll be an inversion
    return res

def bitsEqual(left, right):
    if len(left) != len(right):
        return False
    for (lItem, rItem) in zip(left, right):
        if lItem != rItem:
            return False
    return True

def hasOneMistake(code):
    infoBitsLen = len(code) / 2
    infoBits = code[:infoBitsLen]
    return not bitsEqual(encode(infoBits), code)

if __name__ == '__main__':
    pass
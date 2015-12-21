__author__ = 'artur'

def encode(inputBits):
    counter = 0
    for bit in inputBits:
        counter += int(bit)
    res = inputBits[:]
    res.extend([int(x) for x in bin(counter)[2:]])
    return res

if __name__ == '__main__':
    pass
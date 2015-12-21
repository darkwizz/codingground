__author__ = 'artur'

def encode(inputBits):
    counter = 0
    for bit in inputBits:
        counter += int(bit)
    res = inputBits[:]
    res.append(~(counter & 1))
    return res

def hasOneMistake(code):
    counter = 0
    for i in code:
        counter += int(code[i])
    return code[-1] != counter & 1

if __name__ == '__main__':
    pass
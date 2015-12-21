__author__ = 'artur'

def encode(inputBits):
    res = []
    for item in inputBits:
        if item:
            res.append('10')
        else:
            res.append('01')
    return res

def hasMistakes(code):
    if not len(code) & 1:
        return True
    for i in range(0, len(code), 2):
        if code[i:i + 1] == '00' or code[i:i + 1] == '11':
            return True
    return False

def decode(code):
    if not len(code) & 1:
        return False
    res = []
    for i in range(0, len(code), 2):
        coded = code[i:i + 1]
        if coded == '01':
            res.append(0)
        elif coded == '10':
            res.append(1)
        else:
            return False
    return res

if __name__ == '__main__':
    pass
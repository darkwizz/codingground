# Hello World program in Python

def divide(left, right):
    res = []
    isFirstOne = False
    for i in range(len(left)):
        xorRes = left[i] ^ right[i]
        if not isFirstOne and xorRes == 0:
            print 'No any first 1'
            continue
        elif not isFirstOne and xorRes == 1:
            isFirstOne = True
        res.append(xorRes)
    return res

def getRest(inputBits, polynom):
    pollen = len(polynom)
    index = 0
    rest = []
    while index < len(inputBits):
        print 'Index =', index
        rightBoard = index + pollen
        print 'Right board =', rightBoard
        if rightBoard > len(inputBits):
            print 'In if part'
            break
        rest.extend(inputBits[index + len(rest) : rightBoard])
        print 'After extending:', rest
        rest = divide(rest, polynom)
        print 'The rest =', rest
        index = index + pollen - len(rest)
    print 'In end of getRest'
    return rest

inputBits = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1]
polynom = [1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1]

print '\n\n'
print getRest(inputBits, polynom)

offsetNum = 0
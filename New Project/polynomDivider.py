def divide(left, right):
    res = []
    isFirstOne = False
    for i in range(len(left)):
        xorRes = left[i] ^ right[i]
        if not isFirstOne and xorRes == 0:
            #print 'No any first 1'
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
        #print 'Index =', index
        rightBoard = index + pollen
        #print 'Right board =', rightBoard
        if rightBoard > len(inputBits):
            #print 'In if part'
            rest.extend(inputBits[index + len(rest) : len(inputBits)])
            break
        rest.extend(inputBits[index + len(rest) : rightBoard])
        #print 'After extending:', rest
        rest = divide(rest, polynom)
        #print 'The rest =', rest
        index = index + pollen - len(rest)
    #print 'In end of getRest'
    return rest
 
def isNormal(rest):
    onesCount = 0
    for i in rest:
        if i:
            onesCount += 1
    return onesCount <= 2
 
initBits = [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
inputBits = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1]
polynom = [1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1]
 
print '\n\n'
print getRest(initBits, polynom)
 
rest = getRest(inputBits, polynom)
leftBoard = 0
while not isNormal(rest) and leftBoard < len(inputBits):
    leftBoard += 1
    temp = inputBits[leftBoard % len(inputBits) : len(inputBits)]
    temp.extend(inputBits[0 : leftBoard % len(inputBits)])
    rest = getRest(temp, polynom)
    print 'Current offset =', leftBoard, '\tCurrent rest =', rest
print 'Needed offset:', leftBoard
print rest

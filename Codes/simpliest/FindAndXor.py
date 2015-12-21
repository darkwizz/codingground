__author__ = 'artur'

def findAdnXor(first, second, addit):
    res = addit
    for (i, j) in zip(first, second):
        res = (int(i) & int(j)) ^ res
    return res

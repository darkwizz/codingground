__author__ = 'artur'

def goDecodeGray(number):
    y = []
    y.append(int(number[0]))
    for i in range(1, len(number)):
        res = y[i - 1] ^ int(number[i])
        y.append(res)
        print y[i - 1], '+', number[i], '=', res
    return y

def goGray(number):
    y = []
    y.append(int(number[0]))
    for i in range(1, len(number)):
        res = int(number[i - 1]) ^ int(number[i])
        y.append(res)
        print number[i - 1], '+', number[i], '=', res
    return y


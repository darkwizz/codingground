__author__ = 'artur'


def divideOnEqual(probabilities):
    index = 1
    if len(probabilities) == 2 or len(probabilities) == 3:
        return index
    while abs(sum(probabilities[:index]) - sum(probabilities[index:])) > 0.058 and index < len(probabilities):
        index += 1
    return index

def buildShennonFanoTable(probabilities):
    probabilities.sort(reverse=True)
    codes = []
    probsTuples = []
    index = 0
    for prob in probabilities:
        codes.append([prob, ''])
        probsTuples.append((prob, index))
        index += 1
    probsGroups = []
    probsGroups.append(probsTuples)
    probsCopy = probsGroups[:]
    while len(probsGroups) != len(probabilities):
        for group in probsCopy:
            if not probsGroups.__contains__(group):
                continue
            if len(group) <= 1:
                continue
            plainProbs = [x for (x, y) in group]
            middleIndex = divideOnEqual(plainProbs)
            offset = group[0][1]
            i = offset
            for item in plainProbs:
                if i < middleIndex + offset:
                    codes[i][1] += '0'
                else:
                    codes[i][1] += '1'
                i += 1
            probsGroups.remove(group)
            probsGroups.append(group[:middleIndex])
            probsGroups.append(group[middleIndex:])

            probsCopy.append(group[:middleIndex])
            probsCopy.append(group[middleIndex:])
            print codes[offset:offset + len(group)], '\n'
    return codes

if __name__ == '__main__':
    probs = [0.2239, 0.1194, 0.1045, 0.0746, 0.0746, 0.0746, 0.0597, 0.0597, 0.0299, 0.0299, 0.0299, 0.0149, 0.0149]
    print buildShennonFanoTable(probs)
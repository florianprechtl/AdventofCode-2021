import os

def findMostCommonBit(bitArray, index):
    numOneBits = 0
    for bitRow in bitArray:
        numOneBits += int(bitRow[index])

    if (numOneBits / len(bitArray)) >= 0.5:
        return 1
    else:
        return 0

def findLeastCommonBit(bitArray, index):
    numOneBits = 0
    for bitRow in bitArray:
        numOneBits += int(bitRow[index])

    if (numOneBits / len(bitArray)) < 0.5:
        return 1
    else:
        return 0

def calcOGRating(lines):
    maxBitPosition = len(lines[0]) - 1
    bitPosition = 0

    while (len(lines) > 1 or bitPosition < maxBitPosition):
        remainingLines = []
        mostCommonBit = findMostCommonBit(lines, bitPosition)
        for line in lines:
            if int(line[bitPosition]) == mostCommonBit:
                remainingLines.append(line)

        lines = remainingLines
        bitPosition += 1

    og_rating = lines[0]
    og_rating = int(og_rating, 2)
    return og_rating

def calcCO2Rating(lines):
    maxBitPosition = len(lines[0]) - 1
    bitPosition = 0

    while (len(lines) > 1 and bitPosition < maxBitPosition):
        remainingLines = []
        leastCommonBit = findLeastCommonBit(lines, bitPosition)
        for line in lines:
            if int(line[bitPosition]) == leastCommonBit:
                remainingLines.append(line)

        lines = remainingLines
        bitPosition += 1

    co2_rating = lines[0]
    co2_rating = int(co2_rating, 2)
    return co2_rating


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, '../input.txt'), 'r')
text = f.read()
lines = text.split("\n")

co2_rating = calcCO2Rating(lines)
og_rating = calcOGRating(lines)
result = og_rating * co2_rating
print(co2_rating, " * ", og_rating, " = ", result)

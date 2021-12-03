import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, '../input.txt'), 'r')

text = f.read()
lines = text.split("\n")

lenBinary = len(lines[0])

resultGamma = ""
resultEpsilon = ""

for i in range(0, lenBinary):

    oneCounter = 0

    for line in lines:
        oneCounter += int(line[i])

    if (oneCounter > (len(lines) / 2)):
        resultGamma += str(1)
        resultEpsilon += str(0)
    else:
        resultGamma += str(0)
        resultEpsilon += str(1)

result = int(resultGamma, 2) * int(resultEpsilon, 2)

print(int(resultGamma, 2), " * ", int(resultEpsilon, 2), " = ", result)
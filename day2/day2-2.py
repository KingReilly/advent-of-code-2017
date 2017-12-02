# Advent Of Code 2017
# Day 2, Part 2
# KingReilly

input = open('input.txt')
result = 0

for line in iter(input):
    stringLine = line.rsplit()
    numLine = [int(x) for x in stringLine]
    numLine.sort(reverse=True)
    for i in range(0, len(numLine) - 1):
        for y in range(i + 1, len(numLine) - 1):
            if numLine[i] % numLine[y] == 0:
                result += numLine[i] / numLine[y]

input.close()
print('The checksum is {}'.format(str(int(result))))

# Advent Of Code 2017
# Day 2, Part 1
# KingReilly

input = open('input.txt')
result = 0

for line in iter(input):
    stringLine = line.rsplit()
    numLine = [int(x) for x in stringLine]
    numLine.sort()
    result += numLine[-1] - numLine[0]

input.close()
print('The checksum is {}'.format(str(result)))

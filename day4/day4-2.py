# Advent Of Code 2017
# Day 4, Part 2
# KingReilly

input = open('input.txt')
result = 0

for line in iter(input):
    wordList = line.rsplit()
    sortedWordList = []
    for word in wordList:
        sortedWordList.append(''.join(sorted(word)))
    if len(sortedWordList) == len(set(sortedWordList)):
        result += 1

print('There are {} valid passphrases'.format(result))

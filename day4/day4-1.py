# Advent Of Code 2017
# Day 4, Part 1
# KingReilly

input = open('input.txt')
result = 0

for line in iter(input):
    wordList = line.rsplit()
    if len(wordList) == len(set(wordList)):
        result += 1

print('There are {} valid passphrases'.format(result))

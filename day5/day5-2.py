# Advent Of Code 2017
# Day 5, Part 2
# KingReilly

input = open('input.txt')
numbers = []

for line in iter(input):
    numbers.append(int(line.strip()))

steps = 0
i = 0
while i >= 0 and i < len(numbers):
    steps += 1
    newIndex = i + numbers[i]

    if numbers[i] >= 3:
        numbers[i] -= 1
    else:
        numbers[i] += 1

    i = newIndex

print('It took {} steps to reach the exit'.format(steps))

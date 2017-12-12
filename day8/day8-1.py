# Advent Of Code 2017
# Day 8, Part 1
# KingReilly

instructions = open('input.txt')
variables = {}

for line in instructions:
    a, operation, amount, _, b, conditional, conditionalAmount = line.rsplit()
    amount = int(amount)
    conditionalAmount = int(conditionalAmount)

    # Init variables
    if a not in variables:
        variables[a] = 0
    if b not in variables:
        variables[b] = 0

    if operation == 'inc':
        operator = 1
    else:
        operator = -1

    if conditional == '==':
        if variables[b] == conditionalAmount:
            variables[a] += operator * amount
    elif conditional == '<':
        if variables[b] < conditionalAmount:
            variables[a] += operator * amount
    elif conditional == '>':
        if variables[b] > conditionalAmount:
            variables[a] += operator * amount
    elif conditional == '<=':
        if variables[b] <= conditionalAmount:
            variables[a] += operator * amount
    elif conditional == '>=':
        if variables[b] >= conditionalAmount:
            variables[a] += operator * amount
    else:
        if variables[b] != conditionalAmount:
            variables[a] += operator * amount

print('The highest value is {}'.format(max(variables.values())))

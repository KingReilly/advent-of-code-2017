# Advent Of Code 2017
# Day 6, Part 2
# KingReilly

with open('input.txt') as file:
    memory = [int(x) for x in file.readline().rsplit()]


def cycle():
    history = []
    history.append(memory.copy())
    cycles = 0

    while True:
        # Determine index and value of highest number
        highestIndex = memory.index(max(memory))
        highestNumber = memory[highestIndex]

        # Set the highest value to 0
        memory[highestIndex] = 0

        # Distribute highest number sequentially across memory blocks
        nextIndex = highestIndex + 1
        for i in range(highestNumber):
            if nextIndex >= len(memory):
                nextIndex = 0
            memory[nextIndex] += 1
            nextIndex += 1

        cycles += 1
        if memory in history:
            break
        history.append(memory.copy())
    return cycles


print('It took {} cycles to encounter a repeated pattern'.format(str(cycle())))
print('It took a further {} cycles to encounter this repeated pattern again'.format(str(cycle())))

file = open('day02/input.txt', 'r')
lines = file.readlines()

# part 1
total = 0
for line in lines: 
    opponent = line[0]
    you = line[2]
    if opponent == 'A' and you == 'X':
        total += 4
    elif opponent == 'B' and you == 'Y':
        total += 5
    elif opponent == 'C' and you == 'Z':
        total += 6
    elif opponent == 'A' and you == 'Y':
        total += 8
    elif opponent == 'A' and you == 'Z':
        total += 3
    elif opponent == 'B' and you == 'X':
        total += 1
    elif opponent == 'B' and you == 'Z':
        total += 9
    elif opponent == 'C' and you == 'X':
        total += 7
    elif opponent == 'C' and you == 'Y':
        total += 2

print(total)

# part 2
total = 0
for line in lines: 
    opponent = line[0]
    you = line[2]
    if opponent == 'A' and you == 'X':
        total += 3
    elif opponent == 'B' and you == 'Y':
        total += 5
    elif opponent == 'C' and you == 'Z':
        total += 7
    elif opponent == 'A' and you == 'Y':
        total += 4
    elif opponent == 'A' and you == 'Z':
        total += 8
    elif opponent == 'B' and you == 'X':
        total += 1
    elif opponent == 'B' and you == 'Z':
        total += 9
    elif opponent == 'C' and you == 'X':
        total += 2
    elif opponent == 'C' and you == 'Y':
        total += 6

print(total)
file = open('day01/input.txt', 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

elves = []
elf = []
for line in lines:
    if line == '':
        elves.append(elf)
        elf = []
    else:
        elf.append(line)
elves.append(elf)

final = []
for i in elves:
    i = sum([int(j) for j in i])
    final.append(i)

# part 1
print(max(final))

# part 2
final.sort()
print(sum(final[-3:]))









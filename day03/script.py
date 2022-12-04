file = open('day03/input.txt', 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# part 1
total = 0 
for line in lines:
    firstHalf = line[:len(line)//2]
    secondHalf = line[len(line)//2:]
    for i in alphabet: 
        if i in firstHalf and i in secondHalf:
            total += alphabet.index(i)+1
print(total)

# part 2
pos = 0
total = 0
while pos < len(lines):
    elf1 = lines[pos]
    elf2 = lines[pos+1]
    elf3 = lines[pos+2]

    for i in elf1:
        if i in elf2 and i in elf3:
            total += alphabet.index(i)+1
            break

    pos += 3
print(total)


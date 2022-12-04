file = open('day04/input.txt', 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

#part 1
total = 0
for line in lines: 
    line = line.split(',')
    elf1 = line[0].split('-')
    elf2 = line[1].split('-')
    if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
        total += 1
    elif int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1]):
        total += 1
print(total)

#part 2
total = 0
for line in lines: 
    line = line.split(',')
    elf1 = line[0].split('-')
    elf2 = line[1].split('-')
    if (int(elf1[0]) <= int(elf2[0]) <= int(elf1[1])) or (int(elf2[0]) <= int(elf1[0]) <= int(elf2[1])):
        total += 1
print(total)


    


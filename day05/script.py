file = open('day05/input.txt', 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

# Unfortunately, in the short time I had, I could not do this without hardcoding the values
# so input.txt is missing some lines at the start which are represented below and in crates.txt instead 
stacks = { 
"1": ["J", "F", "C", "N", "D", "B", "W"],
"2": ["T", "S", "L", "Q", "V", "Z", "P"],
"3": ["T", "J", "G", "B", "Z", "P"],
"4": ["C", "H", "B", "Z", "J", "L", "T", "D"],
"5": ["S", "J", "B", "V", "G"],
"6": ["Q", "S", "P"],
"7": ["N", "P", "M", "L", "F", "D", "V", "B"],
"8": ["R", "L", "D", "B", "F", "M", "S", "P"],
"9": ["R", "T", "D", "V"],
}

## Part 1
for line in lines:
    a = line.split(' ')

    chosen = int(a[1])
    initial = stacks[a[3]]
    final = stacks[a[5]]

    for i in range(0,chosen):
        value = initial.pop(0)
        final.insert(0, value)

for key, value in stacks.items():
    print(value[0])

## Part 2
for line in lines:
    a = line.split(' ')

    chosen = int(a[1])
    initial = stacks[a[3]]
    final = stacks[a[5]]

    lift = []
    for i in range(0,chosen):
        if len(initial) != 0:
            value = initial.pop(0)
            lift.append(value)
        else:
            pass

    #iterates backwards to keep order
    for i in range(len(lift)-1, -1, -1):
        final.insert(0, lift[i])

for key, value in stacks.items():
    print(value[0])




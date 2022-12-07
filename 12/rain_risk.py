import math

rotation = 0
posx = 0
posy = 0
wayx = 10
wayy = 1
p1 = 0
p2 = 0

with open('12.in', 'r') as reader:
    lines = reader.readlines()

    for line in lines:
        instruction = line[:1]
        val = int(line[1:])
        if instruction == 'N':
            wayy += val
        if instruction == 'S':
            wayy -= val
        if instruction == 'E':
            wayx += val
        if instruction == 'W':
            wayx -= val
        if instruction == 'L':
            for _ in range(val//90):
                wayx, wayy = -wayy, wayx
        if instruction == 'R':
            for _ in range(val//90):
                wayx, wayy = wayy, -wayx
        if instruction == 'F':
            posx += val * wayx
            posy += val * wayy
        print(instruction,val)
        print('posx', posx)
        print('posy', posy)
        print('wayx', wayx)
        print('wayy', wayy)

    print(abs(posx) + abs(posy))

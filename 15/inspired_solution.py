from math import sqrt

data = None
with open("testinput.txt", "r", encoding="utf8") as reader:
    data = [x.strip() for x in reader.readlines()]

beacons = set()
sensors = set()


def mdist(point1, point2):
    xdiff = abs(point2[0] - point1[0])
    ydiff = abs(point2[1] - point1[1])
    return xdiff + ydiff


def possible(x, y):
    point = (x, y)
    for sx, sy, dist in sensors:
        sensor_point = (sx, sy)
        if point not in beacons and mdist(point, sensor_point) <= dist:
            return False
    return True


def p1(y):
    count = 0
    left = min(x - dist for x, _, dist in sensors)
    right = max(x + dist + 1 for x, _, dist in sensors)
    for x in range(left, right + 1):
        if not possible(x, y):
            count += 1
    return count


def p2():
    possiblex = None
    possibley = None
    # max_check = 4000000 + 1
    max_check = 20 + 1
    for sx, sy, dist in sensors:
        tempx = set()
        tempy = set()
        for i in range(0, sx - dist):
            tempx.add(i)
        for i in range(sx + dist + 1, max_check):
            tempx.add(i)
        for i in range(0, sy - dist):
            tempy.add(i)
        for i in range(sy + dist + 1, max_check):
            tempy.add(i)
        if possiblex is None:
            possiblex = tempx
        else:
            possiblex = possiblex.intersection(tempx)
        if possibley is None:
            possibley = tempy
        else:
            possibley = possibley.intersection(tempy)
    return list(possiblex)[0] * 4000000 + list(possibley)[0]


for line in data:
    dasplit = line.split(" ")
    sx, sy = int(dasplit[2][2:-1]), int(dasplit[3][2:-1])
    bx, by = int(dasplit[8][2:-1]), int(dasplit[9][2:])
    spos = (sx, sy)
    bpos = (bx, by)
    beacons.add(bpos)
    sensors.add((sx, sy, mdist(spos, bpos)))

# print(p1(2000000))
print(p2())

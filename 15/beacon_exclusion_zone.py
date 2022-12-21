from math import sqrt

data = None
p1 = 0
p2 = 0
with open("testinput.txt", "r", encoding="utf8") as reader:
    data = [x.strip() for x in reader.readlines()]


covered_points = {}
bposes = {}


def apply(a, b, operation):
    return tuple(operation(x[0], x[1]) for x in zip(a, b))


def mdist(point1, point2):
    xdiff = abs(point2[0] - point1[0])
    ydiff = abs(point2[1] - point1[1])
    return xdiff + ydiff


def add_bpos(x, y):
    if y not in bposes:
        bposes[y] = set()
    bposes[y].add(x)


def get_invalid(y):
    return sum([len(x) for x in covered_points[y]]) - len(bposes[y])


def add_range(y, xstart, xend):
    if y not in covered_points:
        covered_points[y] = set()
    for ran in covered_points[y]:
        if xstart in ran:
            xstart = ran.stop
        if xend in ran:
            xend = ran.start

    if xend > xstart:
        covered_points[y].add(range(xstart, xend))


for line in data:
    dasplit = line.split(" ")
    sx, sy = int(dasplit[2][2:-1]), int(dasplit[3][2:-1])
    bx, by = int(dasplit[8][2:-1]), int(dasplit[9][2:])
    spos = (sx, sy)
    bpos = (bx, by)
    add_bpos(bx, by)

    dist = mdist(spos, bpos)
    for index, y in enumerate(range(sy - dist, sy)):
        xstart, xend = sx - index, sx + index + 1
        add_range(y, xstart, xend)
    for index, y in enumerate(range(sy, sy + dist + 1)):
        xstart, xend = sx - dist + index, sx + dist - index + 1
        add_range(y, xstart, xend)

points = []

for ran in covered_points[10]:
    for element in ran:
        points.append(element)

temp = []
for ran in covered_points[10]:
    for x in ran:
        temp.append(x)
print(sorted(temp))
print(get_invalid(10))

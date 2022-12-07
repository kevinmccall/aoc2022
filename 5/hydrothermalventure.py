q1 = None
q2 = None

def get_sign(num):
    if num >= 0:
        return 1
    else:
        return -1

data = []
with open('input', 'r') as reader:
    lines = reader.readlines()
    for line in lines:
        start, end = line.strip().split(" -> ")
        startx, starty = start.split(',')
        endx, endy = end.split(',')
        
        data.append(((int(startx), int(starty)), (int(endx), int(endy))))

paths = []
for endpoints in data:
    (startx, starty), (endx, endy) = endpoints
    if startx == endx:
        sign = get_sign(endy - starty)
        for y in range(starty, endy + sign, sign):
            paths.append( (startx, y) )
    elif starty == endy:
        sign = get_sign(endx - startx)
        for x in range(startx, endx + sign, sign):
            paths.append( (x, starty) )
    elif abs(endy - starty) == abs(endx - startx):
        ydiff = endy - starty
        xdiff = endx - startx
        xsign = get_sign(xdiff)
        ysign = get_sign(ydiff)
        xvals = range(startx, endx + xsign, xsign)
        yvals = range(starty, endy + ysign, ysign)
        for i in range(abs(ydiff) + 1):
            paths.append((xvals[i], yvals[i]))


overlapping_points = []
for coordinate in paths:
    if paths.count(coordinate) > 1:
        overlapping_points.append(coordinate)
q1 = len(set(overlapping_points))

print(q1)


def print_coords():
    result = ''
    maxx = max([x[0] for x in paths])
    maxy = max([x[1] for x in paths])
    for y in range(maxy + 1):
        for x in range(maxx + 1):

            count = paths.count((x,y))
            if count > 0:
                result += str(count)
            else:
                result += '.'
        result += "\n"
    print(result)    

# print_coords()
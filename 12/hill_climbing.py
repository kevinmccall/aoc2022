from string import ascii_lowercase

data = None
p1 = 0
p2 = 0
with open("testinput.txt", "r", encoding="utf8") as reader:
    data = [x.strip() for x in reader.readlines()]


class Point:
    def __init__(self, point, elevation, came_from, distance) -> None:
        self.elevation = elevation
        self.came_from = came_from
        self.distance = distance
        self.point = point
        self.row = point[0]
        self.col = point[1]


start = None
end = None

for i, line in enumerate(data):
    a = line.find("S")
    if a != -1:
        start = (i, a)
    b = line.find("E")
    if b != -1:
        end = (i, b)
    if start is not None and end is not None:
        break

checked = set()
to_check = set()
num_rows = len(data)
num_cols = len(data[0])
row_length = num_cols
col_length = num_rows
points = []

for i in range(len(data)):
    for j in range(len(data[i])):
        points.append(None)


def get_point(row, col) -> Point:
    return points[row * row_length + col]


def set_point(row, col, point: Point):
    points[row * row_length + col] = point


def get_neighbors(point: Point):
    for adj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        arow, acol = point.row + adj[0], point.col + adj[1]
        if arow < 0 or arow >= num_rows or acol < 0 or acol >= num_cols:
            continue
        elif (arow, acol) in checked:
            continue
        distance = point.distance + 1
        point_in_spot = get_point(arow, acol)
        if point_in_spot is not None:
            if distance >= point_in_spot.distance:
                continue
        elevation = -1
        if data[arow][acol] == "E":
            elevation = 25
        else:
            elevation = ascii_lowercase.index(data[arow][acol])
        if elevation > point.elevation + 1:
            continue
        yield Point(
            point=(arow, acol), elevation=elevation, came_from=point, distance=distance
        )


def get_path_after_complete():
    path = []
    c = get_point(*end)
    while c is not None:
        path.insert(0, c.point)
        c = c.came_from
    return path


to_check.add(Point(start, 0, None, 0))
while len(to_check) > 0:
    current = to_check.pop()
    set_point(current.row, current.col, current)
    for neighbor in get_neighbors(current):
        to_check.add(neighbor)
    checked.add(current.point)

p = get_path_after_complete()


def print_board():
    message = ""
    for i in range(num_rows):
        for j in range(num_cols):
            point = get_point(i, j)
            direction = "."
            if point.point == start:
                direction = "S"
            elif point.point == end:
                direction = "E"
            elif point.row - point.came_from.row == 1:
                direction = "^"
            elif point.row - point.came_from.row == -1:
                direction = "v"
            elif point.col - point.came_from.col == 1:
                direction = "<"
            elif point.col - point.came_from.col == -1:
                direction = ">"
            else:
                breakpoint()
            message += direction
        message += "\n"
    print(message, end="")


def print_path():
    message = ""
    for i in range(num_rows):
        for j in range(num_cols):
            point = get_point(i, j)
            direction = "."
            if point.point not in p:
                pass
            elif point.point == start:
                direction = "S"
            elif point.point == end:
                direction = "E"
            elif point.row - point.came_from.row == 1:
                direction = "^"
            elif point.row - point.came_from.row == -1:
                direction = "v"
            elif point.col - point.came_from.col == 1:
                direction = "<"
            elif point.col - point.came_from.col == -1:
                direction = ">"
            else:
                breakpoint()
            message += direction
        message += "\n"
    print(message, end="")


def print_points():
    for i in range(num_rows):
        for j in range(num_cols):
            print(get_point(i, j).point, end=", ")
        print("\n")


print_board()
print(p)
print_path()

from string import ascii_lowercase

data = None
p1 = 0
p2 = 0
with open("input.txt", "r", encoding="utf8") as reader:
    data = [x.strip() for x in reader.readlines()]


class Point:
    def __init__(self, point, elevation, came_from, distance) -> None:
        self.elevation = elevation
        self.came_from = came_from
        self.distance = distance
        self.point = point
        self.row = point[0]
        self.col = point[1]


class Pathfinder:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.checked = set()
        self.to_check = set()
        self.num_rows = len(data)
        self.num_cols = len(data[0])
        self.row_length = self.num_cols
        self.col_length = self.num_rows
        self.points = []
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.points.append(None)
        start_point = Point(start, 0, None, 0)
        self.to_check.add(start_point)
        self.set_point(start_point.row, start_point.col, start_point)

    def get_point(self, row, col) -> Point:
        return self.points[row * self.row_length + col]

    def set_point(self, row, col, point: Point):
        self.points[row * self.row_length + col] = point

    def get_path_after_complete(self):
        path = []
        c = self.get_point(*self.end)
        while c is not None:
            path.insert(0, c.point)
            c = c.came_from
        return path

    def get_neighbors(self, point: Point):
        for adj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            arow, acol = point.row + adj[0], point.col + adj[1]
            if arow < 0 or arow >= self.num_rows or acol < 0 or acol >= self.num_cols:
                continue
            if (arow, acol) in self.checked:
                continue
            distance = point.distance + 1
            point_in_spot = self.get_point(arow, acol)
            if point_in_spot is not None:
                if distance >= point_in_spot.distance:
                    continue
                point_in_spot.distance = distance
                point_in_spot.came_from = point
                yield point_in_spot
            elevation = -1
            if data[arow][acol] == "E":
                elevation = 25
            elif data[arow][acol] == "S":
                elevation = 0
            else:
                elevation = ascii_lowercase.index(data[arow][acol])
            if elevation > point.elevation + 1:
                continue
            yield Point(
                point=(arow, acol),
                elevation=elevation,
                came_from=point,
                distance=distance,
            )

    def find_path(self):
        while len(self.to_check) > 0:
            current = self.to_check.pop()
            for neighbor in self.get_neighbors(current):
                self.set_point(neighbor.row, neighbor.col, neighbor)
                self.to_check.add(neighbor)
            self.checked.add(current.point)

        return self.get_path_after_complete()

    def get_path_length(self, path):
        return len(path) - 1

    def print_board(self):
        message = ""
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                point = self.get_point(i, j)
                direction = "."
                if point is None:
                    pass
                elif point.point == self.start:
                    direction = "S"
                elif point.point == self.end:
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

    def print_path(self, path):
        message = ""
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                point = self.get_point(i, j)
                direction = "."
                if point is None:
                    pass
                elif point.point not in path:
                    pass
                elif point.point == self.start:
                    direction = "S"
                elif point.point == self.end:
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

    def print_points(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                print(self.get_point(i, j).point, end=", ")
            print("\n")


def find_start_and_end():
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
            return start, end


# p1
start, end = find_start_and_end()
pathfinder = Pathfinder(start, end)
path = pathfinder.find_path()
print(pathfinder.get_path_length(path))

start_points = {}
for i, line in enumerate(data):
    for j, elevation in enumerate(line):
        if elevation == "a":
            start = (i, j)
            pathfinder = Pathfinder(start, end)
            path = pathfinder.find_path()
            start_points[start] = pathfinder.get_path_length(path)

distances = start_points.values()
valid_starts = filter(lambda x: x != -1, distances)
# valid_starts = filter(lambda x: x != -1, distances)
# valid_starts = list(valid_starts) #??????? you can't convert it to a list on the same line??????? what ???!??!?!? I literally don't get this this would have made my correct code not work!?
print(min(valid_starts))

# ???? it doesn't work anymore but it did in interactive mode
# actual valid things?:
# [459, 463, 456, 469, 464, 457, 460, 456, 457, 464, 463, 460, 465, 464, 455, 455, 461, 462, 463, 462, 465, 458, 460, 461, 453, 464, 463, 462, 453, 458, 452, 453, 455, 454, 460, 453, 451, 455, 446, 448, 460, 451, 453, 452, 453, 452, 458, 453, 453, 453, 450, 450, 448, 459, 451, 451, 446, 452, 451, 450, 451, 467, 480, 454, 462, 461, 464, 469, 470, 459, 461, 462, 465, 470, 467, 464, 469, 458, 461, 464, 461, 464, 463, 480, 455, 457, 458, 457, 462, 459, 470, 463, 466, 462, 460, 463, 462, 459, 462, 461, 462, 469, 464, 457, 461, 458, 461, 462, 465, 464, 469, 464, 469, 468, 462, 462, 463, 461, 464, 463, 472, 465, 472, 481, 469, 459, 470, 461, 460, 463, 466, 464, 464, 459, 464, 463, 468, 463, 461, 452, 463, 472, 465, 460, 462, 463, 468, 471, 473, 467, 456, 465, 454, 468, 473, 457, 463, 468, 463, 462, 459]
#
# I fixed it, the code that didn't work for some reason:
# valid_starts = list(filter(lambda x: x != -1, distances))
#
# now they both work... I'm gonna have a blood vessel in my brain pop
# I just got rid of the list conversion all together - freak that

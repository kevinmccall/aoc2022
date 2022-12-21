data = None
p1 = 0
p2 = 0
with open("testinput.txt", "r", encoding="utf8") as reader:
    data = [x.strip() for x in reader.readlines()]

# USE SETS -- lol
walls = set()
sand_point = (500, 0)
lowest_point = 0
for line in data:
    splits = line.split(" -> ")
    for i in range(len(splits) - 1):
        x1, y1 = [int(x) for x in splits[i].split(",")]
        x2, y2 = [int(x) for x in splits[i + 1].split(",")]
        lowest_point = max(lowest_point, y1, y2)
        if x2 == x1:
            darange = range(min(y1, y2), max(y1, y2) + 1)
            for y in darange:
                walls.add((x1, y))
        else:
            darange = range(min(x1, x2), max(x1, x2) + 1)
            for x in darange:
                walls.add((x, y1))


sand = set()

# 0 -> move down
# 1 -> move left
# 2 -> move right


def apply(a, b, operation):
    return tuple(operation(x[0], x[1]) for x in zip(a, b))


def occupied(coord):
    return coord in walls or coord in sand


def check_move(coord, move_pos):
    new_pos = coord[0] + move_pos[0], coord[1] + move_pos[1]
    return not occupied(new_pos)


# def simulate_sand():
#     sand_coord = sand_point
#     moving = True
#     while moving:
#         if sand_coord[1] > lowest_point:
#             return False
#         moving = False
#         for coord in [(0, 1), (-1, 1), (1, 1)]:
#             if check_move(sand_coord, coord):
#                 moving = True
#                 sand_coord = apply(sand_coord, coord, lambda x, y: x + y)
#                 break
#     sand.append(sand_coord)
#     return True


lowest_point += 2


def simulate_sand():
    sand_coord = sand_point
    moving = True
    while moving:
        if sand_coord[1] > lowest_point:
            return False
        moving = False
        for coord in [(0, 1), (-1, 1), (1, 1)]:
            if check_move(sand_coord, coord):
                moving = True
                sand_coord = apply(sand_coord, coord, lambda x, y: x + y)
                if sand_coord[1] + 1 >= lowest_point:
                    moving = False
                break

    sand.add(sand_coord)
    return True


# print(walls)


def debug_print():
    message = ""
    for y in range(0, 11 + 1):
        for x in range(494 - 5, 503 + 1 + 5):
            if (x, y) in walls:
                message += "#"
            elif (x, y) == sand_point:
                message += "+"
            elif (x, y) in sand:
                message += "o"
            else:
                message += "."
            message += " "
        message += "\n"
    print(message, end="")


while simulate_sand():
    if sand_point in sand:
        break
    debug_print()
    print()

print(len(sand))

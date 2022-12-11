data = None
p1 = 0
p2 = 0
with open("input.txt", "r", encoding="utf8") as reader:
    data = [x.strip() for x in reader.readlines()]

for i, line in enumerate(data):
    for j, height in enumerate(line):
        height = int(height)
        # top
        visible_top = True
        for y in range(i):
            if int(data[y][j]) >= height:
                visible_top = False
        # bottom
        visible_bottom = True
        for y in range(i + 1, len(data)):
            if int(data[y][j]) >= height:
                visible_bottom = False
        # left
        visible_left = True
        for x in range(j):
            if int(data[i][x]) >= height:
                visible_left = False
        # right
        visible_right = True
        for x in range(j + 1, len(line)):
            if int(data[i][x]) >= height:
                visible_right = False

        if visible_top or visible_bottom or visible_left or visible_right:
            p1 += 1

print(p1)

for i, line in enumerate(data):
    for j, height in enumerate(line):
        height = int(height)
        # top
        top_score = 0
        for y in range(i - 1, -1, -1):
            top_score += 1
            if int(data[y][j]) >= height:
                break
        # bottom
        bottom_score = 0
        for y in range(i + 1, len(data)):
            bottom_score += 1
            if int(data[y][j]) >= height:
                break
        # left
        left_score = 0
        for x in range(j - 1, -1, -1):
            left_score += 1
            if int(data[i][x]) >= height:
                break
        # right
        right_score = 0
        for x in range(j + 1, len(line)):
            right_score += 1
            if int(data[i][x]) >= height:
                break
        p2 = max(p2, top_score * bottom_score * left_score * right_score)

print(p2)

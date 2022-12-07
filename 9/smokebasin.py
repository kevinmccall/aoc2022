data = []
q1 = 0
q2 = None

with open('input', 'r') as reader:
    lines = reader.readlines()
    for line in lines:
        row = []
        for digit in line.strip():
            row.append(int(digit))
        data.append(row)

basins = []

def get_point(data, x, y):
    if x < 0 or y < 0:
        return None
    try:
        return data[y][x]
    except IndexError:
        return None

for xindex, row_val in enumerate(data):
    for yindex, column_val in enumerate(row_val):
        is_low_point = True
        current_basin = {}
        try:
            if row_val[yindex - 1] <= column_val:
                is_low_point = False
        except IndexError:
            pass
        try:
            if row_val[yindex + 1] <= column_val:
                is_low_point = False
        except IndexError:
            pass
        try:
            if data[xindex + 1][yindex] <= column_val:
                is_low_point = False
        except IndexError:
            pass
        try:
            if data[xindex - 1][yindex] <= column_val:
                is_low_point = False
        except IndexError:
            pass
        if is_low_point == True:
            q1 += column_val + 1
            current_basin[(yindex, xindex)] = column_val
            basins.append(current_basin)

for basin_group in basins:
    need_to_check = list(basin_group.keys())
    while len(need_to_check) > 0:
        current_pos = need_to_check[0]
        current_val = basin_group[current_pos]
        for neighbor_offset in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor_x = current_pos[0] + neighbor_offset[0]
            neighbor_y = current_pos[1] + neighbor_offset[1]
            neighbor_val = get_point(data, neighbor_x, neighbor_y)
            if neighbor_val != None and neighbor_val != 9 and neighbor_val > current_val:
                need_to_check.append((neighbor_x, neighbor_y))
                basin_group[(neighbor_x, neighbor_y)] = neighbor_val
        need_to_check.remove(current_pos)

basins.sort(key=lambda x : len(x))
q2 = 1
for top_3 in basins[-3:]:
    q2 *= len(top_3)


print(q1)
print(q2)
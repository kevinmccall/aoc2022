data = None
p1 = 0
p2 = 0
with open("input.txt", "r", encoding="utf8") as reader:
    data = [x.strip() for x in reader.readlines()]


def parse_range(string_data: str):
    start, end = string_data.split("-")
    return range(int(start), int(end) + 1)


for line in data:
    one, two = line.split(",")
    shiftone = set(parse_range(one))
    shifttwo = set(parse_range(two))
    if shiftone.issubset(shifttwo) or shifttwo.issubset(shiftone):
        p1 += 1
    if len(shiftone.intersection(shifttwo)) > 0:
        p2 += 1

print(p1)
print(p2)

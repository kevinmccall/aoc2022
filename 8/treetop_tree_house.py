data = None
p1 = 0
p2 = 0
with open("8/input.txt", "r", encoding="utf8") as reader:
    data = [x.strip() for x in reader.readlines()]

visible = [0] * len(data) ** 2

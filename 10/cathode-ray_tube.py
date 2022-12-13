data = None
p1 = 0
p2 = 0
with open("10/input.txt", "r", encoding="utf8") as reader:
    data = [x.strip() for x in reader.readlines()]

x = 1
commands = []


def noop():
    commands.append(None)


def addx(amount):
    noop()
    commands.append(amount)


for line in data:
    split = line.split(" ")
    command = split[0]
    if command == "noop":
        noop()
    else:
        addx(int(split[1]))

cycle = 0
message = ""
screen_width = 40
while len(commands) > 0:
    if cycle % screen_width in range(x - 1, x + 2):
        message += "#"
    else:
        message += "."
    cycle += 1
    if cycle in [20, 60, 100, 140, 180, 220]:
        p1 += cycle * x
    if cycle % screen_width == 0:
        message += "\n"
    current = commands.pop(0)
    if current is None:
        pass
    elif isinstance(current, int):
        x += current

print(p1)
print(message, end="")

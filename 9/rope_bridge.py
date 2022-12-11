data = None
p1 = 0
p2 = 0
with open("input.txt", "r", encoding="utf8") as reader:
    data = [x.strip() for x in reader.readlines()]


def get_sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0


class Pos:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def get_pos(self):
        return (self.x, self.y)

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


rope = [Pos(0, 0) for x in range(10)]

visited_pos = set()
head = rope[0]
tail = rope[-1]
visited_pos.add(tail.get_pos())


def update_previous(leader, follower):
    xdiff = leader.x - follower.x
    ydiff = leader.y - follower.y
    if (abs(xdiff) >= 2 and abs(ydiff) >= 1) or (abs(xdiff) >= 1 and abs(ydiff) >= 2):
        ydir = get_sign(ydiff)
        xdir = get_sign(xdiff)
        follower.x += xdir
        follower.y += ydir
    elif abs(xdiff) >= 2:
        xdir = get_sign(xdiff)
        follower.x += xdir
    elif abs(ydiff) >= 2:
        ydir = get_sign(ydiff)
        follower.y += ydir


for command in data:
    direc, times = command.split(" ")
    times = int(times)

    for i in range(times):
        if direc == "U":
            head.y += 1
        elif direc == "D":
            head.y -= 1
        elif direc == "L":
            head.x -= 1
        elif direc == "R":
            head.x += 1

        lead = head
        for segment in rope[1:]:
            update_previous(lead, segment)
            lead = segment
        visited_pos.add(tail.get_pos())

print(len(visited_pos))
print(head.get_pos())

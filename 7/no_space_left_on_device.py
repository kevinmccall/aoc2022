data = None
p1 = 0
p2 = 0
with open("7/input.txt", "r", encoding="utf8") as reader:
    data = [x.strip() for x in reader.readlines()]

size_under_100_000 = 0


class Node:
    def __init__(self, name) -> None:
        self.children = {}
        self.file_size = 0
        self.name = name
        self.parent = None
        self.is_dir = False
        self.total_size = None

    def add_child(self, name, size, is_dir):
        child = Node(name)
        child.file_size = size
        child.parent = self
        child.is_dir = is_dir
        self.children[name] = child

    def get_child(self, name):
        return self.children[name]

    def get_parent(self):
        return self.parent

    def get_size(self):
        if self.total_size is None:
            size = self.file_size
            for child in self.children.values():
                size += child.get_size()

            if size <= 100_000 and self.is_dir:
                global size_under_100_000
                size_under_100_000 += size
            self.total_size = size
            return size
        else:
            return self.total_size


current_dir: Node = None
head = None

for line in data:
    split = line.split(" ")
    if split[0] == "$":
        if split[1] == "cd":
            if split[2] == "..":
                current_dir = current_dir.get_parent()
            else:
                if current_dir is None:
                    current_dir = Node(split[2])
                    current_dir.is_dir = True
                    head = current_dir
                else:
                    current_dir = current_dir.get_child(split[2])
    elif split[0] == "dir":
        current_dir.add_child(split[1], 0, True)
    elif split[0].isnumeric():
        current_dir.add_child(split[1], int(split[0]), False)

head.get_size()


print(size_under_100_000)

all_n = []


def all_nodes(node):
    required_size = min(30000000, 70000000 - head.total_size)
    if not node.is_dir or node.total_size < required_size:
        return
    for child in node.children.values():
        all_nodes(child)
    all_n.append(node)


all_nodes(head)
all_n.sort(key=lambda x: x.total_size)
print(all_n[0].total_size)

# 6483416 too high

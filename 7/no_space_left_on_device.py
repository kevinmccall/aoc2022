data = None
p1 = 0
p2 = 0
with open("input.txt", "r", encoding="utf8") as reader:
    data = [x.strip() for x in reader.readlines()]


P1_TARGET = 100_000
P2_TOTAL_SIZE = 70_000_000
P2_SIZE_NEEDED = 30_000_000

free_size = 0
size_under_target = 0
min_file = float("inf")


class Node:
    def __init__(self, name) -> None:
        self.dirs = {}
        self.files = []
        self.name = name
        self.parent = None
        self.cached_size = None

    def add_file(self, size):
        self.files.append(size)

    def add_dir(self, name):
        child = Node(name)
        child.parent = self
        self.dirs[name] = child

    def get_dir(self, dirname):
        return self.dirs[dirname]

    def get_parent(self):
        return self.parent

    def get_size(self):
        if self.cached_size is None:
            size = 0
            for child in self.dirs.values():
                size += child.get_size()
            for filesize in self.files:
                size += filesize

            if size <= P1_TARGET:
                global size_under_target
                size_under_target += size
            self.cached_size = size
            return size
        else:
            return self.cached_size

    def p2(self):
        space_over = P2_SIZE_NEEDED - free_size
        print("hit")
        if self.get_size() < space_over:
            return None
        for subdir in self.dirs.values():
            val = subdir.p2()
            if val is not None:
                global min_file
                min_file = min(min_file, val)
        return self.get_size()


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
                    head = current_dir
                else:
                    current_dir = current_dir.get_dir(split[2])
    elif split[0] == "dir":
        current_dir.add_dir(split[1])
    elif split[0].isnumeric():
        current_dir.add_file(int(split[0]))

free_size = P2_TOTAL_SIZE - head.get_size()
head.p2()
print(min_file)

get_child_sizes = lambda dir: [subdir.get_size() for subdir in dir.dirs.values()]

# p2 not 1148106
# idk where this came from -> 24933642

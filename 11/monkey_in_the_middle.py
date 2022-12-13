from functools import reduce

data = None
p1 = 0
p2 = 0
with open("11/testinput.txt", "r", encoding="utf8") as reader:
    data = [x.strip() for x in reader.readlines()]


def parse_operation(text):
    left, operation, right = [
        x.strip() for x in text.split("=")[1].split(" ") if x != ""
    ]
    operator = None
    if operation == "*":
        operator = lambda x, y: x * y
    if operation == "/":
        operator = lambda x, y: x / y
    if operation == "+":
        operator = lambda x, y: x + y
    if operation == "-":
        operator = lambda x, y: x - y

    def final_operation(x):
        l = int(left) if left.isnumeric() else x
        r = int(right) if right.isnumeric() else x

        return operator(l, r)

    return final_operation


class Monkey:
    monkeys = []
    inspected_count = []

    def __init__(
        self, mid, starting_items, operation, test_val, true_monkey, false_monkey
    ) -> None:
        self.id = mid
        self.items = starting_items
        self.operation = operation
        self.test_val = test_val
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        Monkey.monkeys.append(self)
        Monkey.inspected_count.append(0)

    @staticmethod
    def from_input(info):
        starting_items = [
            int(x.strip()) for x in info[1].split(":")[1].split(",") if x != ""
        ]
        # TODO: Fix this so it works with higher ids of monkeys
        mid = int(info[0][7])
        operation = parse_operation(info[2])
        test_val = int(info[3].split(" ")[-1])
        true_monkey = int(info[4].split(" ")[-1])
        false_monkey = int(info[5].split(" ")[-1])
        m = Monkey(mid, starting_items, operation, test_val, true_monkey, false_monkey)
        return m

    def pass_item(self, val):
        if val % self.test_val == 0:
            Monkey.monkeys[self.true_monkey].items.append(val)
        else:
            Monkey.monkeys[self.false_monkey].items.append(val)

    def run(self):
        while len(self.items) > 0:
            current = self.items.pop(0)
            # new = self.operation(current) // 3
            new = self.operation(current)
            Monkey.inspected_count[self.id] += 1
            self.pass_item(new)


_ = []
for line in data:
    if line == "":
        Monkey.from_input(_)
        _ = []
    else:
        _.append(line)

for mround in range(10000):
    print(f"Round: {mround}")
    for monkey in Monkey.monkeys:
        monkey.run()

print(reduce(lambda x, y: x * y, sorted(Monkey.inspected_count, reverse=True)[:2]))
for index, datapoint in enumerate(Monkey.inspected_count):
    print(f"Monkey {index} inspected {datapoint} items")
for monkey in Monkey.monkeys:
    print(f"{monkey.id}: {monkey.items}")

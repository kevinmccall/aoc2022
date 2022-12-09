import os
from copy import deepcopy

stacks = []
stacks2 = []
instructions = None

for i in range(9):
    stacks.append([])

with open("5/input.txt", "r", encoding="utf8") as reader:
    for i in range(8):
        line = reader.readline()
        for index, j in enumerate(range(1, 36, 4)):
            if line[j] != " ":
                stacks[index].insert(0, line[j])

    for i in range(2):
        reader.readline()

    instructions = [x.strip() for x in reader.readlines()]
    stacks2 = deepcopy(stacks)


for message in instructions:
    m = message.split(" ")
    times, from_stack, to_stack = int(m[1]), int(m[3]), int(m[5])
    holding_stack = []
    for i in range(times):
        stacks[to_stack - 1].append(stacks[from_stack - 1].pop())
        stacks2[to_stack - 1].append(stacks2[from_stack - 1].pop(i - times))

message = ""
message2 = ""

for stack in stacks:
    if len(stack) == 0:
        print("investigate")
    else:
        message += stack[-1]

for stack in stacks2:
    if len(stack) == 0:
        print("investigate")
    else:
        message2 += stack[-1]

print(message)
print(message2)

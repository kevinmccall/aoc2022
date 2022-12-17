data = None
p1 = 0
p2 = 0
with open("input.txt", "r", encoding="utf8") as reader:
    data = [x.strip() for x in reader.readlines()]


def get_pairs():
    temp = []
    pairs = []
    for line in data:
        if line == "":
            pairs.append(temp)
            temp = []
        else:
            temp.append(line.strip())
    return pairs


def iterative_list_builder(strlist):
    list_stack = []
    current_num = ""
    for char in strlist:
        if char == "[":
            list_stack.append([])
        elif char.isnumeric():
            current_num += char
        else:
            if current_num != "":
                list_stack[-1].append(int(current_num))
                current_num = ""
            if char == "]" and len(list_stack) > 1:
                last = list_stack.pop()
                list_stack[-1].append(last)

    return list_stack[0]


def compare(left, right, init_call=True):
    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            return False
        if right > left:
            return True
    else:
        if not hasattr(left, "__iter__"):
            left = [left]
        if not hasattr(right, "__iter__"):
            right = [right]

        for i in range(max(len(left), len(right))):
            if i >= len(left):
                return True
            if i >= len(right):
                return False
            l = left[i]
            r = right[i]
            res = compare(l, r, init_call=False)
            if res is not None:
                return res
        if init_call:
            return True


correct_signals = []
for index, pair in enumerate(get_pairs(), start=1):
    left = iterative_list_builder(pair[0])
    right = iterative_list_builder(pair[1])

    if compare(left, right):
        correct_signals.append(index)

all_signals = [iterative_list_builder(x) for x in data if x != ""]
all_signals.append([[2]])
all_signals.append([[6]])


def bubble_sort(li, comparator):
    for i in range(len(li)):
        for j in range(len(li) - i - 1):
            if not comparator(li[j], li[j + 1]):
                li[j], li[j + 1] = li[j + 1], li[j]


bubble_sort(all_signals, comparator=compare)
for x in all_signals:
    print(x)
print((all_signals.index([[2]]) + 1) * (1 + all_signals.index([[6]])))

# rand_list = [6, 1, 3, 5, 4, 8, 10, 9, 7, 2]
# bubble_sort(rand_list, lambda x, y: x < y)
# print(rand_list)

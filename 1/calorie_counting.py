with open("input.txt", "r") as reader:
    calories = []
    cum = 0
    for line in reader:
        if line == "\n":
            calories.append(cum)
            cum = 0
        else:
            cum += int(line.strip())

    # part 1
    print(max(calories))

    # part 2
    calories.sort()
    print(sum(calories[-3:]))

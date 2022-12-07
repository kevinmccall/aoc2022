from string import ascii_letters


with open("input.txt", "r", encoding="utf8") as reader:
    data = [x.strip() for x in reader.readlines()]
    score = 0

    for line in data:
        first = line[: len(line) // 2]
        second = line[len(line) // 2 :]
        both = set(first).intersection(set(second))
        (letter,) = both  # get the only element of the set
        score += ascii_letters.index(letter) + 1
    print(score)

    # bad solution
    # score2 = 0
    # current = set()
    # for index, content in enumerate(data):
    #     if (index % 3) == 0 and index != 0:
    #         (letter,) = current  # get the only element of the set
    #         score2 += ascii_letters.index(letter) + 1
    #         current = set()
    #     if len(current) == 0:
    #         current.update(set(content))
    #     else:
    #         current = current.intersection(set(content))
    # print(score2 + 26) # last one is z

    # better solution?
    score2 = 0
    current = set()
    for index, content in enumerate(data):
        if len(current) == 0:
            current.update(set(content))
        else:
            current = current.intersection(set(content))
        if (index + 1) % 3 == 0:
            (letter,) = current  # get the only element of the set
            score2 += ascii_letters.index(letter) + 1
            current = set()
    print(score2)  # last one is z

with open('input', 'r') as reader:
    lines = reader.readlines()
    rand_nums = [int(x.strip()) for x in lines[0].split(',')]

    boards = []

    current_board = []
    for count, line in enumerate(lines[2:]):
        if len(current_board) < 5:
            line_nums = [int(x) for x in line.strip().split()]
            if line_nums:
                current_board.append(line_nums)
        else:
            boards.append(current_board)
            current_board = []
    if current_board != []:
        boards.append(current_board)



    def search_for_board():
        for current_number in range(len(rand_nums)):
            current_pool = set(rand_nums[:current_number + 1])
            for board in boards:
                columns = [[] for i in range(5)]
                for row in board:
                    if set(row).issubset(current_pool):
                        return (board, current_number)
                    for index, element in enumerate(row):
                        columns[index].append(element)
                for column in columns:
                    if set(column).issubset(current_pool):
                        return (board, current_number)
        print("L")
        return (None, None)
    
    def search_for_worst_board():
        winning_boards = []
        current_pool = set()
        for current_number in range(len(rand_nums)):
            current_pool.add(rand_nums[current_number])
            for board in boards:
                if board in winning_boards:
                    continue
                columns = [[] for i in range(5)]
                for row in board:
                    if set(row).issubset(current_pool):
                        if board not in winning_boards:
                            winning_boards.append(board)
                    for index, element in enumerate(row):
                        columns[index].append(element)
                for column in columns:
                    if set(column).issubset(current_pool):
                        if board not in winning_boards:
                            winning_boards.append(board)
                if len(winning_boards) == len(boards):
                    return (board, current_number)
        print("L")
        return (None, None)

    
    target_board, count = search_for_worst_board()
    if target_board != None:
        sum = 0
        searched_numbers = set(rand_nums[:count+1])
        last_number = rand_nums[count]
        for row in target_board:
            for number in set(row).difference(searched_numbers):
                sum += number
        print(sum * last_number)
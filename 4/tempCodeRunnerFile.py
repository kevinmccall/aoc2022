    if len(winning_boards) == len(boards) - 1:
                    for board in boards:
                        if board not in winning_boards:
                            return (board, current_number)
                    print("didn't work")
ties = {"A": "X", "B": "Y", "C": "Z"}
wins = {"A": "Y", "B": "Z", "C": "X"}


with open("input.txt", "r", encoding="utf8") as reader:

    opponent_moves = []
    our_moves = []
    for line in reader:
        opp, our = line.strip().split(" ")
        opponent_moves.append(opp)
        our_moves.append(our)

    score = 0
    for opp, our in zip(opponent_moves, our_moves):
        if our == "X":
            score += 1
        elif our == "Y":
            score += 2
        elif our == "Z":
            score += 3

        if wins[opp] == our:
            score += 6
        elif ties[opp] == our:
            score += 3

    print(score)

    score2 = 0
    for opp, our in zip(opponent_moves, our_moves):
        if our == "X":
            score2 += 0
            if opp == "A":
                score2 += 3
            elif opp == "B":
                score2 += 1
            elif opp == "C":
                score2 += 2
        elif our == "Y":
            score2 += 3
            if opp == "A":
                score2 += 1
            elif opp == "B":
                score2 += 2
            elif opp == "C":
                score2 += 3
        elif our == "Z":
            score2 += 6
            if opp == "A":
                score2 += 2
            elif opp == "B":
                score2 += 3
            elif opp == "C":
                score2 += 1
    print(score2)


#             rock  paper scissors
# opp_moves = ["a", "b", "c"]
# our_moves = ["x", "y", "z"]

# if opp_moves.index(a) == (our_moves.index(b) + 1) % len(our_moves):
#   we win
# elif if opp_moves.index(a) == opp_moves.index(b):
#   tie
# else:
#   we lose

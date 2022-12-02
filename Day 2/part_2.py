
ROUND_SCORE = {
    "X" : 0 ,
    "Y" : 3,
    "Z" : 6
}

WIN_MAP = {
    "A" : 2,
    "B" : 3,
    "C" : 1
}

LOSS_MAP = {
    "A" : 3,
    "B" : 1,
    "C" : 2
}

DRAW_MAP = {
    "A" : 1,
    "B" : 2,
    "C" : 3
}



with open("input.txt") as f:
    score = 0
    for round in f:
        
        opp, result = round.strip().split(" ")
        score += ROUND_SCORE[result]
        if result == "X":
            score += LOSS_MAP[opp]
        elif result == "Y":
            score += DRAW_MAP[opp]
        else:
            score += WIN_MAP[opp]

    print(score)

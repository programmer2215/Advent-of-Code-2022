
SHAPE_SCORE = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

SHAPE_MAP = {
    "X" : "A",
    "Y" : "B",
    "Z" : "C"
}

ROUND_POINTS = {
    "win" : 6,
    "draw" : 3,
    "loss" : 0
}

with open("input.txt") as f:
    score = 0
    for round in f:
        
        opp, me = round.strip().split(" ")
        score += SHAPE_SCORE[me]
        if me == "X" and opp == "C":
            result = "win"
        elif me == "Y" and opp == "A":
            result = "win"
        elif me == "Z" and opp == "B":
            result = "win"
        elif opp == SHAPE_MAP[me]:
            result = "draw"
        else:
            result = "loss"
        
        score += ROUND_POINTS[result]

    print(score)

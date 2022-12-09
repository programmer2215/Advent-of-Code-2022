with open('input.txt') as f:
    forrest = [list(x.strip()) for x in f.readlines()]
    col_forrest = [[] for x in range(len(forrest))]
    for i in range(len(forrest)):
        for j in range(len(forrest)):
            col_forrest[i].append(forrest[j][i])
    

    visible = (len(forrest[0]) * 4) - 4 #outer trees

    for row in range(1, len(forrest) - 1):
        for column in range(1, len(forrest) - 1):
            tree = forrest[row][column]
            r = tree > max(forrest[row][column + 1:])
            l = tree > max(forrest[row][:column])
            b = tree > max(col_forrest[column][row + 1:])
            t = tree > max(col_forrest[column][:row])
            if r or l or t or b:
                visible += 1 

    print(f"Visible: {visible}")
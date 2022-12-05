

with open("input.txt") as f:
    lines = f.readlines()
    stacks = {}
    for i in lines:
        index_row = i
        i = i.strip()
        if i.startswith("1"):

            for x in range(int(i[0]) , int(i[-1]) + 1):
                stacks[str(x)] = []
            break
    for line in lines:
        if not line.strip().startswith("1"):
            for j in stacks:
                if line[index_row.index(j)] != ' ':
                    stacks[j].append(line[index_row.index(j)])
        else:
            break
    for stack in stacks:
        stacks[stack].reverse()
    # Part 1
    for move in lines[lines.index("\n") + 1 :]:
        temp = []
        move = move.split()
        amt, from_i, to_i = int(move[1]), move[3], move[5]
        for i in range(amt):
            temp.append(stacks[from_i].pop())
        stacks[to_i].extend(temp)
    
    ans = ''
    for i in stacks:
        ans = ans + stacks[i][-1]
    print(ans)



def find_dist(tree, direc: list):
    dist = 0
    
    for _tree in direc:
        dist += 1
        if _tree >= tree  :  
            break
    
    return dist

with open('input.txt') as f:
    forrest = [[int(x) for x in list(x.strip())] for x in f.readlines()]
    col_forrest = [[] for x in range(len(forrest))]
    for i in range(len(forrest)):
        for j in range(len(forrest)):
            col_forrest[i].append(forrest[j][i])
    

    scenic_score = []

    for row in range(0, len(forrest)):
        for column in range(0, len(forrest)):
            tree = forrest[row][column]
            r = find_dist(tree, forrest[row][column + 1:])
            l = find_dist(tree, list(reversed(forrest[row][:column])))
            b = find_dist(tree, col_forrest[column][row + 1:])
            t = find_dist(tree, list(reversed(col_forrest[column][:row])))
            
            
            scenic_score.append(r * l * t * b)
            

    print(f"Max Scenic Score: {max(scenic_score)}")
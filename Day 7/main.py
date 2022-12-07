

with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]
    data = {}
    cur_path = []

    # Part 1
    for line in lines:
        if line.startswith("$"):
            if "cd" in line:
                if '..' not in line:
                    cur_path.append(line.split()[-1])
                else:
                    cur_path.pop()
            else:
                path = "/".join(cur_path)
                data[path] = 0
        else:
            path = "/".join(cur_path)
            if line[0].isnumeric():
                data[path] += int(line.split()[0])
                
    for path1 in data:
        for path2 in data:
            if path1 in path2 and path1 != path2:
                data[path1] += data[path2]
    dir_sizes = sorted([x for x in list(data.values()) if x <= 100000])
    print(sum(dir_sizes))
    
    
    #Part 2
    required_space = 30000000 - (70000000 - data['/'])
    data = sorted(list(data.values()))
    

    for i in range(len(data)):
        if data[i] >= required_space:
            print(data[i])
            break


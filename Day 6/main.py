

with open('input.txt') as f:
    buffer = f.read().strip()
    
    #Part 1
    for i in range(len(buffer)):
        marker = buffer[i : i+4]
        if len(marker) == len(set(marker)):
            print(i+4)
            break
    #Part 2
    for i in range(len(buffer)):
        marker = buffer[i : i+14]
        if len(marker) == len(set(marker)):
            print(i+14)
            break


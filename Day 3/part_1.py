import string

with open('input.txt') as f:
    sum_priorities = 0
    alpha = string.ascii_letters
    for rucksack in f:
        rucksack = rucksack.strip()
        mid = (len(rucksack) // 2)
        compart_1 = [] 
        for x in rucksack[:mid]:
            if x not in compart_1:
                compart_1.append(x)
        
        compart_2 = rucksack[mid:]
        for item in compart_1:
            if item in compart_2:
                sum_priorities += alpha.index(item) + 1
    print(sum_priorities)
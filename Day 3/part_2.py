import string

with open('input.txt') as f:
    sum_priorities = 0
    alpha = string.ascii_letters
    
    rucksacks = [x.strip() for x in f.readlines()]
    
    index = 0
    for i in range(len(rucksacks) // 3):
        group = rucksacks[index:index+3]
        elf_1 = []
        for item in group[0]:
            if item not in elf_1:
                elf_1.append(item)
        for item in elf_1:
            if item in group[1] and item in group[2]:
                sum_priorities += alpha.index(item) + 1
        
        index += 3

        
    print(sum_priorities)
    
    
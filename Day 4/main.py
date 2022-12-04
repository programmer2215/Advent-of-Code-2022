

with open('input.txt') as f:
    
    subset_count = 0
    intersection_count = 0
    
    # Part - 1
    for pair in f.readlines():
        elf_1, elf_2 = pair.strip().split(',')
        elf_1, elf_2 = elf_1.split('-'), elf_2.split('-')
        elf_1, elf_2 = set(range(int(elf_1[0]), int(elf_1[1]) +1)), set(range(int(elf_2[0]), int(elf_2[1]) +1))
        if elf_1.issubset(elf_2) or elf_2.issubset(elf_1):
            subset_count += 1

        # Part 2
        if len(elf_1.intersection(elf_2)) > 0:
            intersection_count += 1
    print(subset_count)
    print(intersection_count)
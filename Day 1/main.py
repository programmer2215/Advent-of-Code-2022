with open('input.txt') as f:
    # Part 1
    data = f.readlines()
    total_calories = []
    total_calories_per_elf = 0
    for snack in data:
        if not snack == '\n':
            total_calories_per_elf += int(snack.strip())
        else:
            total_calories.append(total_calories_per_elf)
            total_calories_per_elf = 0
    print(max(total_calories))
    # Part 2
    sum_top_3 =  0
    for i in range(3):
        sum_top_3 += total_calories.pop(total_calories.index(max(total_calories)))

    print(sum_top_3)
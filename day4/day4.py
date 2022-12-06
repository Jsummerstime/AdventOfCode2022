# part 1
'''
total = 0
with open("day4.txt") as file:
    for line in file:
        convert_0 = line.strip('\n').split(",")
        convert_1 = convert_0[0].split('-')
        convert_2 = convert_0[1].split('-')

        elf1 = (int(convert_1[0]),int(convert_1[1]))
        elf2 = (int(convert_2[0]),int(convert_2[1]))

        if elf2[0] >= elf1[0] and elf2[-1] <= elf1[-1]:
            total +=1
        elif elf1[0] >= elf2[0] and elf1[-1] <= elf2[-1]:
            total +=1
print(total)
'''

# part 2

total = 0
with open("day4.txt") as file:
    for line in file:
        convert_0 = line.strip('\n').split(",")
        convert_1 = convert_0[0].split('-')
        convert_2 = convert_0[1].split('-')

        elf1 = (int(convert_1[0]),int(convert_1[1]))
        elf2 = (int(convert_2[0]),int(convert_2[1]))

        if elf2[0] >= elf1[0] and elf2[-1] <= elf1[-1]:
            total +=1
        elif elf1[0] >= elf2[0] and elf1[-1] <= elf2[-1]:
            total +=1
        elif elf1[-1] <= elf2[-1] and elf1[-1] >= elf2[0]:
            total += 1
        elif elf2[-1] <= elf1[-1] and elf2[-1] >= elf1[0]:
            total += 1
print(total)  
#part 1
'''
with open("day2.txt") as file:
    total = 0
    for line in file:
        items = line.split()
        oppoent = items[0]
        play = items[1]

        if play == 'X':
            total +=1
        elif play == 'Y':
            total +=2
        elif play == 'Z':
            total += 3

        if oppoent == 'A' and play == 'X':
            total += 3
        elif oppoent == 'A' and play == 'Y':
            total += 6
        elif oppoent == 'A' and play == 'Z':
            total += 0
        elif oppoent == 'B' and play == 'X':
            total += 0
        elif oppoent == 'B' and play == 'Y':
            total += 3
        elif oppoent == 'B' and play == 'Z':
            total += 6
        elif oppoent == 'C' and play == 'X':
            total += 6
        elif oppoent == 'C' and play == 'Y':
            total += 0
        elif oppoent == 'C' and play == 'Z':
            total += 3

    print(total)
'''
#part 2
with open("day2.txt") as file:
    total = 0
    for line in file:
        items = line.split()
        oppoent = items[0]
        play = items[1]

        if play == 'X':
            total += 0 # lose
            if oppoent == 'A':
                total += 3
            elif oppoent == 'B':
                total += 1
            elif oppoent == 'C':
                total += 2
        elif play == 'Y':
            total += 3 # draw
            if oppoent == 'A':
                total += 1
            elif oppoent == 'B':
                total += 2
            elif oppoent == 'C':
                total += 3
        elif play == 'Z':
            total += 6 #win
            if oppoent == 'A':
                total += 2
            elif oppoent == 'B':
                total += 3
            elif oppoent == 'C':
                total +=1
            

    print(total)



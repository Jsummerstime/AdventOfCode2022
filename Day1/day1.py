# part 1
'''
max = 0
current = 0
with open('day1.txt') as file:
    for line in file:

        if line == '\n':
            if current > max:
                max = current
                current = 0
            else:
                current = 0
        else:
            current += int(line)

    print(max)
'''      
# part 2

max1 = 0
max2 = 0
max3 = 0
current = 0
with open('param.txt') as file:
    for line in file:

        if line == '\n':
            p1 = max1
            p2 = max2
            p3 = max3
            if current > max1:
                max1 = current
                max2 = p1
                max3 = p2
                current = 0
            elif current > max2:
                max2 = current
                max3 = p2
                current = 0
            elif current > max3:
                max3 = current
                current = 0
            else:
                current = 0
        else:
            current += int(line)

    print(max1+max2+max3)


# part 1
'''
def conv(c): # convert char to priority a - z = 1-26, A - Z = 27 - 52
    n = ord(c)
    if n >= 97:
        return (n - 96)
    else:
        return (n - 38)

total = 0

with open("day3.txt") as file:
    for line in file:
        l = int(len(line)/2)
        firstHalf = line[0:l]
        secondHalf = line[l:-1]
        
        
        for i in firstHalf: # find match char
            for j in secondHalf:
                if i == j: # break out of inner loop
                    print(i, conv(i))
                    total += conv(i)
                    break
            if i == j: # break out of outer loop
                break
       
print(total)
'''
def conv(c): # convert char to priority a - z = 1-26, A - Z = 27 - 52
    n = ord(c)
    if n >= 97:
        return (n - 96)
    else:
        return (n - 38)

total = 0

with open("day3.txt") as file:
    track = 0 #keep track of line number, loop 0,1,2
    l0 = "" # save three lines 
    l1 = ""
    l2 = ""
    for line in file:
        
        if track <=2:
            if track == 0:
                l0 = line
                track += 1
            elif track == 1:
                l1 = line
                track += 1
            else: #brute force all three lines
                l2 = line
                track += 1
                for h in l0:
                    for i in l1:
                        for j in l2:
                            if h == i == j:
                                total += conv(h) #convert and add to total
                                break
                        if h == i == j: #break out of outer loops
                            break  
                    if h == i == j:
                        break  
                track = 0 # reset
                l0 = ""
                l1 = ""
                l2 = ""
        
print(total)


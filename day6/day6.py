# part 1
'''
last_four = ['', '', '', '']
count = 0
with open("day6.txt") as file:
    for line in file:
        line.strip('\n')
        for item in line: # super nasty code, but tests for uniqueness of each item
            if last_four[0] not in last_four[1:-1] and last_four[1] not in last_four[2:-1] and last_four[1] != last_four[0] and last_four[2] not in last_four[0:1] and last_four[2] != last_four[3] and last_four[3] not in last_four[0:2] and  '' not in last_four:
                print(count)
                print(last_four)
                break
       
            else: # if previous four items not unique, add to count, and update list
                count +=1
                last_four.insert(0,item)
                last_four.pop()
        if last_four[0] != last_four[1] != last_four[2] != last_four[3] and '' not in last_four: # not needed?
            break
'''

# part 2
def counter(lst, x): # looks for repeat chars
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

last_fourteen =  ['', '', '', '', '', '', '', '', '', '', '', '', '', ''] # keep track of last fourteen chars
count = 0
status = False # see loop starting on line 37
with open("day6.txt") as file:
    for line in file:
        line.strip('\n')
        for item in line:
            for i in last_fourteen: # look for repeat chars for each item
                if counter(last_fourteen, i) > 1:
                    
                    status = False
                    break
                else: # if the entire list is unique, true
                    status = True
                    
            if '' not in last_fourteen and status == True:
                print(count)
                print(last_fourteen)
                break
       
            else: # if previous four items not unique, add to count, and update list
                count +=1
                last_fourteen.append(item) # queue
                last_fourteen.pop(0)

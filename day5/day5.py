# part 1
'''
from collections import defaultdict
dict = defaultdict(list) # initialize empty dictonary with empyth lists as vals
count = 0
dict_count = 1

with open("day5_crates.txt") as file:
    for line in file:
        line = "  " + line.strip('\n') # make the lines even, so that on index 3 there is a crate ID
        count = 0
        dict_count = 1

        for item in line.strip('\n'): # populate dictionary with crate IDs
            
            if count == 3:
                count = 0 # reset count every 3 (0,1,2,3,0,1,2,3...)
                if item != ' ' and item.isdigit() == False:
                    dict[dict_count].insert(0,item) 
                    dict_count +=1 # keep track of stack number
                else:
                    dict_count +=1
                
            else:
                count +=1

il = []
ol = []

with open("day5.txt") as file: # reformat move instructions to a matrix of lists. [n, from, to]
    for line in file:
        items = line.strip('\n').split(' ')
        
        for i in items:
            if i.isdigit():
                il.append(int(i))        
        ol.append(il)
        il = []

for item in ol: # execute crate movements
    
    for i in range(int(item[0])):
        try:
            c = dict[item[1]].pop() # stack: first in, first out
            dict[item[2]].append(c)
        except:
            pass
           
        

for key, val in dict.items():

    try:
        print(key, val.pop()) # return top of each stack
    except: 
        pass
'''

from collections import defaultdict
dict = defaultdict(list)
count = 0
dict_count = 1

with open("day5_crates.txt") as file:
    for line in file:
        line = "  " + line.strip('\n')
        count = 0
        dict_count = 1

        for item in line.strip('\n'):
            
            if count == 3:
                count = 0
                if item != ' ' and item.isdigit() == False:
                    dict[dict_count].insert(0,item)
                    dict_count +=1
                else:
                    dict_count +=1
                
            else:
                count +=1

il = []
ol = []

with open("day5.txt") as file:
    for line in file:
        items = line.strip('\n').split(' ')
        
        for i in items:
            if i.isdigit():
                il.append(int(i))
                
        ol.append(il)
        il = []
cra = [] # keep track of crates to be moved.
for item in ol:
    
    for i in range(int(item[0])):
        try:
            c = dict[item[1]].pop() # only change, instead of first in first out, take of top n in order, then append to target stack
            cra.insert(0,c)

        except:
            pass
  
    dict[item[2]] += cra  
    cra = []      

for key, val in dict.items():

    try:
        print(key, val.pop())
    except:
        pass





           

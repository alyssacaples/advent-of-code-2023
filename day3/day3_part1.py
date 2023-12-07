import re

with open("day3/test.txt") as f:
    lines = f.readlines()
    
    ign = '.'
    
    #how to handle middle cases
    for x in range(1, len(lines) - 1):# goes through each row
        line = lines[x].strip()
        print("line " + str(x) + " " + line)
        
        #go through each line and find number
        # x & y grid 
        sum = 0
        phrase = ""
        for y in line:
            
            if y.isdigit():
                print(y)
                phrase = phrase + y

                #symbol
            else:
                #check grid
                if y != "."
                    #symbol
                    
                
                if phrase != "":
                    print(phrase)
                phrase = ""
                
        
        # for y in line:
        #     print(y)
            
            
        #break
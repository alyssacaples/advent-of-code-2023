

with open("input.txt") as f:
    lines = f.readlines()
    
    limits = {"red": 12, "green": 13, "blue": 14}

    possible_games = [] #holds int values
    game_sum = 0
    cnt = 1
    for line in lines:
        impossible = False
        # each line is a game
        line = line.strip()
        print(line)
        
        #each line is game
        #semi colon splits ; 
        handful = line.split(':')[1]
        #print(handful)
        
        sets = handful.split(';')
        #print(sets)
        
        for set in sets:
            if impossible == True:
                break
            
            set = set.strip() # clear white space
            colors = set.split(',')
            
            for c in colors:
                c = c.strip()
                num = int(c.split()[0])
                color = c.split()[1]
                
                if num > limits[color]:
                    impossible = True
                    print("game " + str(cnt) + " is impossible!")
                    break

        if impossible == False:
            game_sum = game_sum + cnt
        cnt = cnt + 1
        
    print(game_sum)
        #break
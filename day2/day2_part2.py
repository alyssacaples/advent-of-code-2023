
def power_function(a, b, c):
    tmp = a * b
    return tmp * c

with open("input.txt") as f:
    lines = f.readlines()
    
    #limits = {"red": float('inf'), "green": float('inf'), "blue": float('inf')}

    possible_games = [] #holds int values
    game_sum = 0
    cnt = 1
    for line in lines:
        limits = {"red": float('-inf'), "green": float('-inf'), "blue": float('-inf')}
        # each line is a game
        line = line.strip()
        print(line)
        
        #each line is game
        #semi colon splits ; 
        handful = line.split(':')[1]
        sets = handful.split(';')
        
        for set in sets:
            set = set.strip() # clear white space
            colors = set.split(',')
            
            for c in colors:
                c = c.strip()
                num = int(c.split()[0])
                color = c.split()[1]
                
                if num > limits[color]:
                    limits[color] = num
                    print(color, num)
                    

        pwr = power_function(limits["red"], limits["blue"], limits["green"])
        print(limits)
        print(pwr)
        game_sum = game_sum + pwr
        cnt = cnt + 1
        # if cnt == 5:
        #     break
        
    print("sum: ", game_sum)
        #break

test_cases = { (7, 9), (15, 40), (30, 200)}
input_cases = {(38, 234), (67, 1027), (76,1157), (73,1236)}
part3 = {(38677673, 234102711571236)}


current_case = part3

total_wins = []
for i in current_case:
    time = i[0]
    distance_to_beat = i[1]
    
    print(time, distance_to_beat)
    
    cnt = 0
    for j in range(time):
        distance = (1*j) * (time-j)
        
        if distance > distance_to_beat:
            #print(j, distance)
            cnt = cnt + 1

    
    total_wins.append(cnt)
    #break
    
print("Total wins: ", total_wins)    

product = 1
for i in total_wins:
    product = i*product
    
print(product)
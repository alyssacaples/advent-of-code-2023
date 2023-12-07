import re

number_translation = { "one" : '1', "two" : '2', "three" : '3', "four": '4', "five" : '5', "six": '6', "seven": '7', "eight": '8', "nine":'9'}

with open("input.txt") as f:
    lines = f.readlines()

    total_sum = 0
    count = 0
    for line in lines:
        # identify all numbers in the line
        #res = [i for i in line if i.isdigit()]
        line = line.strip()
        # check a phrase in python string
        digits = []
        phrase = ""
        for i in line:

            if i.isdigit():
                digits.append(i)
                phrase = ""
            else:
                
                phrase = phrase + i
                for j in number_translation.keys():
                    if j in phrase:
                        digits.append(number_translation[j])
                        phrase = i # just leave the last letter in
        
        print(line.strip())
        print(digits)
        num = int(digits[0] + digits[-1])
        total_sum = total_sum + num
        
        print(num)
        count = count + 1
        # temp = re.findall(r'\d+', line)
        # print(line, temp)

        
    
    print(total_sum)    

        # determine first and last numbers
        
        
        #create a map
        

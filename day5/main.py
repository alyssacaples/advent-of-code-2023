import time
        
tic = time.perf_counter()


def range_changer(number, dest_start, source_start, range_length):
        if number in range(source_start, source_start+range_length):
            return (number - source_start) + dest_start
        else:
            return number

def create_number_dict(mappings):
    output_range_dict = {}

    for map in mappings:
        dest_start = map[0]
        source_start = map[1]
        range_length = map[2]

        for i in range(range_length):
            output_range_dict[source_start+i] = dest_start + i

    return output_range_dict


seeds = []
seed2soil_map = []
soil2fert_map = []
fert2water_map = []
water2light_map = []
light2temp_map = []
temp2humidity_map = []
humidity2location_map = []

with open("input.txt") as lines:

    parsing_dict = {"seed2soil": [], "fert2water":[], "humidity2location":[], "light2temp":[], "water2light":[], "soil2fert":[], "temp2humidity":[]}
    map_dict={"seed2soil": {}, "fert2water":{}, "humidity2location":{}, "light2temp":{}, "water2light":{}, "soil2fert":{}, "temp2humidity":{}}
    map_name = ""
    map_active = False
    for line in lines:

        if map_active == True:
            if line[0].isdigit():
                parsing_dict[map_name].append([int(i) for i in line.strip().split()]) 
            else:
                #could try converting here
                map_active = False
                map_dict[map_name] = create_number_dict(parsing_dict[map_name])

        if "seeds" in line:
            seeds = [int(i) for i in line.split(":")[1].strip().split()]
            #print(seeds)
            
        if "seed-to-soil map" in line:
            map_name = "seed2soil"
            map_active = True

        if "soil-to-fertilizer" in line:
            map_name = "soil2fert"
            map_active = True

        if "fertilizer-to-water" in line:
            map_name = "fert2water"
            map_active = True

        if "water-to-light" in line:
            map_name = "water2light"
            map_active = True   

        if "light-to-temperature" in line:
            map_name = "light2temp"
            map_active = True  

        if "humidity-to-location" in line:
            map_name = "humidity2location"
            map_active = True

        if "temperature-to-humidity" in line:
            map_name = "temp2humidity"
            map_active = True    

    map_dict[map_name] = create_number_dict(parsing_dict[map_name])  

    # #print(parsing_dict)

    # final_location = []
    # og_seeds = seeds.copy()
    # for s in seeds:

    #     if map_dict.get("seed2soil").get(s) == None:
    #         soil = s
    #     else:
    #         soil = map_dict.get("seed2soil").get(s)
        
    #     if map_dict.get("soil2fert").get(soil) == None:
    #         fert = soil
    #     else:
    #         fert = map_dict.get("soil2fert").get(soil)

    #     #"fert2water"
    #     if map_dict.get("fert2water").get(fert) == None:
    #         water = fert
    #     else:
    #         water = map_dict.get("fert2water").get(fert)

    #     #"water2light"
    #     if map_dict.get("water2light").get(water) == None:
    #         light = water
    #     else:
    #         light = map_dict.get("water2light").get(water)
        
    #     #"light2temp"
    #     if map_dict.get("light2temp").get(light) == None:
    #         temp = light
    #     else:
    #         temp = map_dict.get("light2temp").get(light)

    #     #"temp2humidity"
    #     if map_dict.get("temp2humidity").get(temp) == None:
    #         humidity = temp
    #     else:
    #         humidity = map_dict.get("temp2humidity").get(temp)

    #     #"humidity2location"
    #     if map_dict.get("humidity2location").get(humidity) == None:
    #         location = humidity
    #     else:
    #         location = map_dict.get("humidity2location").get(humidity)
    #     print("seed: ", s,  " soil: ", soil, " fertilizer: ", fert, " water: ", water, " light: ", light, " temp: ", temp, " humidity: ", humidity, " location: ", location)
    #     final_location.append(location)

    # print("sta: ", og_seeds)
    # print("end:", final_location)

    # print(min(final_location))
    # #print(map_dict)
    
    toc = time.perf_counter()
    print(f"Finished in {toc - tic:0.4f} seconds")

        

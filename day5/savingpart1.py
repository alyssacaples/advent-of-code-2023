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

range_changer(5, 1000000, 2, 10)

with open("test.txt") as lines:

    map_dict = {"seed2soil": [], "fert2water":[], "humidity2location":[], "light2temp":[], "water2light":[], "soil2fert":[], "temp2humidity":[]}
    tp_map_dict={"seed2soil": {}, "fert2water":{}, "humidity2location":{}, "light2temp":{}, "water2light":{}, "soil2fert":{}, "temp2humidity":{}}
    map_name = ""
    map_active = False
    for line in lines:

        if map_active == True:
            if line[0].isdigit():
                map_dict[map_name].append([int(i) for i in line.strip().split()]) 
            else:
                #could try converting here
                map_active = False
                tp_map_dict[map_name] = create_number_dict(map_dict[map_name])

        if "seeds" in line:
            seeds = [int(i) for i in line.split(":")[1].strip().split()]
            print(seeds)
            
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

    tp_map_dict[map_name] = create_number_dict(map_dict[map_name])  

    print(map_dict)

    final_location = []
    og_seeds = seeds.copy()
    for s in seeds:
        for k in map_dict["seed2soil"]:
            
            soil = range_changer(s, k[0], k[1], k[2]) 

            if soil != s:
                break
            
        for k in map_dict["soil2fert"]:
            fert = range_changer(soil, k[0], k[1], k[2])

            if fert != soil:
                break
            
        for k in map_dict["fert2water"]:
            water = range_changer(fert, k[0], k[1], k[2])
            if water != fert:
                break
            
        for k in map_dict["water2light"]:
            light = range_changer(water, k[0], k[1], k[2])

            if light != water:
                break
    
        for k in map_dict["light2temp"]:
            temp = range_changer(light, k[0], k[1], k[2])

            if temp != light:
                break
        for k in map_dict["temp2humidity"]:
            humidity = range_changer(temp, k[0], k[1], k[2])

            if humidity != temp:
                break

        for k in map_dict["humidity2location"]:
            location = range_changer(humidity, k[0], k[1], k[2])
            if location != humidity:
                break

        print("seed: ", s,  " soil: ", soil, " fertilizer: ", fert, " water: ", water, " light: ", light, " temp: ", temp, " humidity: ", humidity, " location: ", location)
        final_location.append(location)

    print("sta: ", og_seeds)
    print("end:", final_location)

    print(min(final_location))
    #print(tp_map_dict)
    
    toc = time.perf_counter()
    print(f"Finished in {toc - tic:0.4f} seconds")
    

        

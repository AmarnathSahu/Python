#Input : AABBBDDDD
#Output : A2B3D4
if __name__ == '__main__' :
    input = "AABBBDDDD"
    map = {}
    for ch in input:
        map[ch] = map.get(ch, 0) + 1
    result = ""
    for key in map.keys():
        result = result + key + str(map[key])
        
    print(result)
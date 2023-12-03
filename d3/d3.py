digits = "1234567890"

result = 0

with open("input.txt", "r") as file:
    # putting all of the file in a list
    engine_map = file.readlines()
    # putting an '\n' at the last line to get the last number 
    engine_map[-1] += "\n"
    

    curr_number = ""
    for i, line in enumerate(engine_map):
        for j, char in enumerate(line):
            if char in digits:
                curr_number += char
            else:
                if curr_number != "":
                    connected = False
                    y_char = i
                    for x_char in range(j-len(curr_number), j):
                        for a in range(-1, 2):
                            for b in range(-1, 2):
                                if 0 <= y_char + a < len(engine_map) and 0 <= x_char + b < len(line):
                                    if engine_map[y_char + a][x_char + b] not in digits + ".\n":
                                        connected = True
                                
                                if connected:
                                    break
                            
                            if connected:
                                    break
                        
                        if connected:
                                    break
                    
                    if connected:
                        result += int(curr_number)
                    
                    curr_number = ""

print(result)

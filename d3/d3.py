digits = "1234567890"

result = 0

with open("input.txt", "r") as file:
    # putting all of the file in a list
    engine_map = file.readlines()
    # putting an '\n' at the last line to get the last number 
    engine_map[-1] += "\n"
    
    # declaring a variable that will hold the numbers we pass through
    curr_number = ""

    # iterating through every caracters of every lines in the engine
    for i, line in enumerate(engine_map):
        for j, char in enumerate(line):
            # if caracter is a digit we add it to our number
            if char in digits:
                curr_number += char
            # if its no longer a digit we end our number
            else:
                if curr_number != "":
                    connected = False

                    # y_char corresponds to the line number of the caracter
                    # x_char corresponds to the row number of the caracter
                    y_char = i
                    for x_char in range(j-len(curr_number), j):
                        # this 'for a' and 'for b' loops are creating all these combinations:
                        #   (-1, -1)
                        #   (-1, 0)
                        #   (-1, 1)
                        #   (0, -1)
                        #   (0, 0)
                        #   (0, 1)
                        #   (1, -1)
                        #   (1, 0)
                        #   (1, 1)
                        # with these values we can obtain the position of the adjacent caracters
                        # of each digit in our number   
                        for a in range(-1, 2):
                            for b in range(-1, 2):
                                # we only test a caracter at a certain position if it does not
                                # go out of the range of the engine
                                if 0 <= y_char + a < len(engine_map) and 0 <= x_char + b < len(line):
                                    if engine_map[y_char + a][x_char + b] not in digits + ".\n":
                                        connected = True
                                
                                # once we added it once we can get out we dont want it multiple times
                                if connected:
                                    break
                            # its a lot of breaks because of the two 'for a' and 'for b' loops
                            if connected:
                                    break
                        
                        if connected:
                                    break
                    
                    if connected:
                        result += int(curr_number)
                    
                    # we reset the number
                    curr_number = ""

print(result)

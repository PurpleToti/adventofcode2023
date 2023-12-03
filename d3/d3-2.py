digits = "1234567890"

result = 0

with open("input.txt", "r") as file:
    # putting all of the file in a list
    engine_map = file.readlines()
    # putting an '\n' at the last line to get the last number 
    engine_map[-1] += "\n"
    

    for i, line in enumerate(engine_map):
        for j, char in enumerate(line):
            if char == "*":
                # we keep count of the numbers we encountered and their positions
                # so that we dont add them again to the same gear
                numbers_connected = []
                already_checked_coordinates = []

                # see d3.py
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        # if we encounter a digit at an unchecked position we explore his number and add it to the 
                        # numbers connected
                        if engine_map[i + a][j + b] in digits and (i + a, j + b) not in already_checked_coordinates:
                            number = engine_map[i + a][j + b]

                            # we keep expanding our number on  the rigth until there is no more digits
                            count = 1
                            while (engine_map[i + a][j + b + count]) in digits:
                                number = number + engine_map[i + a][j + b + count]
                                already_checked_coordinates.append((i + a, j + b + count))
                                count += 1
                            
                            # same but to the left
                            count = 1
                            while (engine_map[i + a][j + b - count]) in digits:
                                number = engine_map[i + a][j + b - count] + number
                                already_checked_coordinates.append((i + a, j + b - count))
                                count += 1
                            
                            # we now have our whole number and can add it (simple)
                            numbers_connected.append(number)
                
                # we only add the gear ratio if there are exactly two connected numbers
                if len(numbers_connected) == 2:
                    result += int(numbers_connected[0]) * int(numbers_connected[1])

print(result)
result = 0

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        # get the game data by first splitting in two at ': '
        gameID, game_data = line.split(": ")
        # get the game ID by splitting by space the first part and taking second element
        gameID = gameID.split(" ")[1]

        dict_min_amount_cubes = {
            "red": 0,
            "blue": 0,
            "green": 0,
        }

        # get each set of cubes picked
        for round in game_data.split("; "):
            # get number of cubes of each color picked
            for nb_color_cube in round.split(", "):
                number, cube_color = nb_color_cube.split(" ")
                # checking if we need to raise the minimum amount of cubes
                if dict_min_amount_cubes[cube_color] < int(number):
                    dict_min_amount_cubes[cube_color] = int(number)

        result += dict_min_amount_cubes["red"] * dict_min_amount_cubes["green"] * dict_min_amount_cubes["blue"]

        

print(result)
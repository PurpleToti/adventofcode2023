# number of cubes for each color
cubes_max_number = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

result = 0

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        # get the game data by first splitting in two at ': '
        gameID, game_data = line.split(": ")
        # get the game ID by splitting by space the first part and taking second element
        gameID = gameID.split(" ")[1]
        possible_game = True

        # get each set of cubes picked
        for round in game_data.split("; "):
            # get number of cubes of each color picked
            for nb_color_cube in round.split(", "):
                number, cube_color = nb_color_cube.split(" ")
                if cubes_max_number[cube_color] < int(number):
                    possible_game = False

        if possible_game:
            result += int(gameID)

print(result)
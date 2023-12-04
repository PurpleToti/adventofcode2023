result = 0
# this is where we store the additional number of cards that we get
dict_additional_cards = {}

with open("input.txt", "r") as file:
    for line in file:
        # We get rid of '\n' caracter and isolate winning and picked numbers
        line = line.strip()
        game_number, line_data = line.split(": ")
        # we get the number of the card
        game_number = int(game_number.split(" ")[-1])

        winning_nums, picked_nums = line_data.split(" | ")
        winning_nums = winning_nums.split(" ")
        picked_nums = picked_nums.split(" ")

        # we initialize the number of this card at 1
        number_of_duplicates = 1

        # if we have some info about the number of additional copy of this
        # card we add it to our number_of_duplicates
        if game_number in dict_additional_cards:
            number_of_duplicates += dict_additional_cards[game_number]
        
        # now that we know how much of this specific card we have we can add it to the total
        # number of cards
        result += number_of_duplicates

        # we use this variable to keep track of wich card we need to win
        # when we get a winning number
        nb_winning_nums = 0

        for num in picked_nums:
            # we get some "" caracters using .split(" ") so we don't count them
            # we get those because there are some times double spaces in the line
            # and we extract the string between them that is ""
            if (num in winning_nums) and (num != ""):
                nb_winning_nums += 1
                # if there already is info about the card we add the number of 
                # copies to it else we create the info
                if game_number + nb_winning_nums in dict_additional_cards:
                    # adding the number of duplicates is the same as executing
                    # this loop for each copy of this card 
                    dict_additional_cards[game_number + nb_winning_nums] += number_of_duplicates
                else:
                    dict_additional_cards[game_number + nb_winning_nums] = number_of_duplicates

                

print(result)
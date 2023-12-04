result = 0

with open("input.txt", "r") as file:
    for line in file:
        # We get rid of '\n' caracter and isolate winning and picked numbers
        line = line.strip()
        line_data = line.split(": ")[1]
        winning_nums, picked_nums = line_data.split(" | ")
        winning_nums = winning_nums.split(" ")
        picked_nums = picked_nums.split(" ")

        card_score = 0

        for num in picked_nums:
            # we get some "" caracters using .split(" ") so we don't count them
            # we get those because there are some times double spaces in the line
            # and we extract the string between them that is ""
            if (num in winning_nums) and (num != ""):
                if card_score == 0:
                    card_score = 1
                else:
                    card_score *= 2
        
        result += card_score

print(result)
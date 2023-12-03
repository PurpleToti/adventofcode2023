digits = "0123456789"
result = 0

with open("input.txt", "r") as file:
    for line in file:
        first_n = None
        last_n = None
        # PART 1
        for i_carac in range(len(line)):
            if line[i_carac] in digits:
                last_n = line[i_carac]
                if first_n is None:
                    first_n = line[i_carac]

        result += int(first_n + last_n)

print(result)

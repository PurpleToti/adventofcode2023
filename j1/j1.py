digits = "0123456789"
dict_spelled_digits = {
    "one": "1", 
    "two": "2", 
    "three": "3", 
    "four": "4", 
    "five": "5", 
    "six": "6", 
    "seven": "7", 
    "eight": "8", 
    "nine": "9",
}
result = 0

test = """nineltnphnvhpvrxbfc1
tcvmnphpmthree56rx
99rsvrmxbgxtjtclnbbmb8sixone3
sevenvfjzctwoqjqmvjrdxpxzsfour5
3d2nhtrhbtfourgsml"""

with open("input.txt", "r") as file:
    for line in file:
        first_n = None
        last_n = None
        for i_carac in range(len(line)):
            if line[i_carac] in digits:
                last_n = line[i_carac]
                if first_n is None:
                    first_n = line[i_carac]
            
            else:
                for spelled_digit in dict_spelled_digits:
                    if len(line) - i_carac >= len(spelled_digit):
                        if line[i_carac:i_carac + len(spelled_digit)] == spelled_digit:
                            last_n = dict_spelled_digits[spelled_digit]
                            if first_n is None:
                                first_n = dict_spelled_digits[spelled_digit]

        result += int(first_n + last_n)

print("RESULT:")
print(result)
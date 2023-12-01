# Combine first and last digits on each line
# def aoc() -> int:
#     # Using readlines() to read input text file
#     file = open('input.txt', 'r')
#     lines = file.readlines()

#     sum = 0
#     for line in lines:

#         # create list of digits
#         digits = []
#         for s in line:
#             if (s.isdigit()):
#                 digits.append(s)

#         num = digits[0] + digits[-1]
#         sum += int(num)

#     print(sum)
#     return sum

# run aoc
# aoc()

# +-----------+
# | Part 2    |
# +-----------+

def aoc() -> int:
    # Using readlines() to read input text file
    file = open('input.txt', 'r')
    lines = file.readlines()

    # dictionary
    # key: string
    # val: int
    numbers_dic = {
        {"one", 1},
        {"two", 2},
        {"three", 3},
        {"four", 4},
        {"five", 5},
        {"six", 6},
        {"seven", 7},
        {"eight", 8},
        {"nine", 9}
    }

    sum = 0
    for line in lines:

        # create list of digits
        line_numbers = []
        for s in line:
            if (s.isdigit()):
                line_numbers.append(s)

        # create list of numbers
        for key, val in numbers_dic:
            if key in line:
                line_numbers.append(val)

        # concatenate first and last nums
        num = line_numbers[0] + line_numbers[-1]

        # calculate sum
        sum += int(num)

    print(sum)
    return sum

# run
import os
print("Current Working Directory: ", os.getcwd())


# aoc()





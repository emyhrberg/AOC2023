# Combine first and last digits on each line
def aoc() -> int:
    # Using readlines() to read input text file
    file = open('input.txt', 'r')
    lines = file.readlines()

    sum = 0
    for line in lines:

        # create list of digits
        digits = []
        for s in line:
            if (s.isdigit()):
                digits.append(s)

        num = digits[0] + digits[-1]
        sum += int(num)

    print(sum)
    return sum

# run aoc
aoc()


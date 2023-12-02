digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def list_of_words(s) -> list[str]:
    # Convert overlapping numbers to list of numbers
    # E.g "eightwothree" -> [eight, two, three]
    result = []
    currentWord = ""
    for i in range(len(s)):

        # digit found, add to result
        if (s[i].isdigit()):
            result.append(s[i])
            currentWord = ""
            continue

        currentWord += s[i]

        # Check if prefix can build a key
        if not any(key.startswith(currentWord) for key in digits.keys()):
            # No key starts with currentWord, reset current word
            currentWord = s[i]
            continue  # Skip to the next iteration of the outer loop
        
        # current word is done, start over currentWord at current index
        if currentWord in digits.keys():
            result.append(currentWord)
            currentWord = s[i]
            i += 1

    return result

def list_of_numbers(s) -> list[int]:
    # Convert list of words to list of numbers
    result = []
    for word in s:
        if word in digits:
            result.append(digits[word])
        elif word.isdigit():
            result.append(word)

    return result

def sum_of_first_and_last(numbers) -> int:
    # Get sum of first and last
    # E.g [8, 2, 3] -> 8 + 3 = 11
    if (len(numbers) == 0):
        return 0
    elif len(numbers) == 1:
        return numbers[0]

    first = str(numbers[0])
    last = str(numbers[-1])
    concat = int(first + last)

    return concat

def solution():
    with open("input.txt", 'r') as file: 
        lines = file.read().split('\n')

    sum = 0

    for s in lines:
        words = list_of_words(s)                # "z4ztwone" -> [4, two, one]
        numbers = list_of_numbers(words)        # [4, two, one] -> [4, 2, 1]
        sum += int(sum_of_first_and_last(numbers))   # [4, 2, 1] -> 4 + 1 = 5

        # print
        print(s, " -> ", ' '.join(map(str, numbers)), " -> ", " -> ", sum_of_first_and_last(numbers))


    print(sum)
    return sum

solution()
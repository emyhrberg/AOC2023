def is_symbol(char):
    return char in "*#+$"

def main():
    with open("day3/input2.txt", 'r') as file: 
        lines = file.read().split('\n')

    ans = 0


    for i, line in enumerate(lines):
        print("------------")

        start_index = None
        currNumIndices = []

        for j, char in enumerate(line):
            if char.isdigit():
                if start_index is None:
                    start_index = j
            else:
                if start_index is not None:
                    currNumIndices.append((start_index, j - 1))
                    start_index = None

        if start_index is not None:
            currNumIndices.append((start_index, len(line) - 1))

        print(f"Row {i}: {currNumIndices}")

        # --- End line for loop ---

    # --- Print answer here ---

if __name__ == '__main__':
    main()

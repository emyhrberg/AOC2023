s = "20blue15green2red"

def extract(color):
    if color in s:
        start_idx = s.index(color)
        num_str = ""
        # Iterate backwards from the character before the first character of the color to extract the entire number
        for i in range(start_idx - 1, -1, -1):
            if s[i].isnumeric():
                num_str = s[i] + num_str
            else:
                break
        return int(num_str) if num_str else 0
    return 0

# Extract values for each color
r = extract("red")
g = extract("green")
b = extract("blue")

print(r, g, b)

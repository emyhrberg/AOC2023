def main():
    with open("input.txt", 'r') as file: 
        lines = file.read().split('\n')

    sum = 0

    # replace with first and last char and its digit in the middle
    string2num = {"one": "o1e", 
                  "two": "t2o", 
                  "three": "t3e", 
                  "four": "f4r", 
                  "five": "f5e", 
                  "six": "s6x", 
                  "seven": "s7n", 
                  "eight": "e8t", 
                  "nine": "n9e"}

    for line in lines:
        # convert to digits
        for k, v in string2num.items():
            line = line.replace(k, v)
        
        # extract digits from each line
        digits: list[int] = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        
        toAdd = 0
        if len(digits) == 0:
            continue
        elif len(digits) == 1:
            toAdd = int(digits[0])
        else:
            toAdd = int(digits[0] + digits[-1])
        
        sum += toAdd
        mainMap[line] = toAdd
            
    print(sum)

def number(line: str):
    if line.startswith("one"):   return "1"
    if line.startswith("two"):   return "2"
    if line.startswith("three"): return "3"
    if line.startswith("four"):  return "4"
    if line.startswith("five"):  return "5"
    if line.startswith("six"):   return "6"
    if line.startswith("seven"): return "7"
    if line.startswith("eight"): return "8"
    if line.startswith("nine"):  return "9"
    return None

def working():
    with open("input.txt") as f:
        content = f.readlines()
    
    total = 0
    for l in content:
        l = l.strip()
        num = ""
        last = ""
        for i, c in enumerate(l):
            if c.isdigit():
                if num == "":
                    num += c
                last = c
            elif number(l[i:]) is not None:
                if num == "":
                    num += number(l[i:])
                last = number(l[i:])
        
        toAdd = int(num+str(last))
        workingMap[l] = toAdd
        total += toAdd
    print(total)

# maps with keys as the test case and values as the result of each test case
mainMap = {}
workingMap = {}

def checkDiff():
    diffMap = {}
    
    for key in mainMap:
        if key in workingMap and mainMap[key] != workingMap[key]:
            diffMap[key] = (mainMap[key], workingMap[key])
    
    # Determine the maximum width for the test case column
    max_key_len = max(len(key) for key in diffMap.keys())

    # Print the header with formatting
    print(f"\n{'Test case':<{max_key_len}} | Main | Working\n{'-'*70}")
    
    # Print the differences with formatting
    for k, v in diffMap.items():
        print(f"{k:{max_key_len}} |  {v[0]}   |  {v[1]}")

# Run code
if __name__ == '__main__':
    main()
    working()
    # checkDiff()
    
    
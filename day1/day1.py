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
            if c.isnumeric():
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
    
mainMap = {}
workingMap = {}

def checkDiff():
    # check for what test cases I get wrong input.
    # maps have key: "4oneight", value: 48 
    # compare two maps. they should contain identical keys but for some they differ values.
    diffMap = {}
    
    for key in mainMap:
        if key in workingMap and mainMap[key] != workingMap[key]:
            diffMap[key] = (mainMap[key], workingMap[key])
          
    print("Test case | Main | Working")
    for k, v in diffMap.items():
        print(f"{k} | {v[0]} | {v[1]}")

# Run code
if __name__ == '__main__':
    main()
    working()
    checkDiff()
    
    
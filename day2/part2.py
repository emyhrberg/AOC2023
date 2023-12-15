def main():
    with open("input.txt", 'r') as file: 
        lines = file.read().split('\n')

    ans = 0

    for line in lines:
        print(line)
        gameIDPart, game = line.split(':')

        segments = game.split(';')

        # print(f"R  | G | B")
        
        r = g = b = 0
        r2 = g2 = b2 = -1
        for segment in segments:
            # Find highest red green and blue 
            colors = segment.split(',')
            for color in colors:
                nums = color.strip().split()
                num, color = nums
                num = int(num)

                if color == "red":
                    r = num
                    if (r > r2):
                        r2 = r
                elif color == "green":
                    g = num
                    if (g > g2):
                        g2 = g
                elif color == "blue":
                    b = num
                    if (b > b2):
                        b2 = b
            
            print(f"{r2}  | {g2} | {b2}")

        toAdd = r2*g2*b2
        print("add: ", toAdd)
        ans += toAdd

    print(ans)

if __name__ == '__main__':
    main()

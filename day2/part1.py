def main():
    with open("input.txt", 'r') as file: 
        lines = file.read().split('\n')

    ans = 0

    for line in lines:
        gameIDPart, game = line.split(':')
        gameID = int(gameIDPart.split()[-1])

        game_valid = True
        segments = game.split(';')

        for segment in segments:
            r = g = b = 0

            colors = segment.split(',')
            for color in colors:
                nums = color.strip().split()
                num, color = nums
                num = int(num)

                if color == "red":
                    r += num
                elif color == "green":
                    g += num
                elif color == "blue":
                    b += num

            if r > 12 or g > 13 or b > 14:
                game_valid = False
                break
        
        if game_valid:
            ans += gameID

    print(ans)

if __name__ == '__main__':
    main()

fp = 'day2.txt'

with open(fp,'r') as f:
    input = f.readlines()

# transform input string into list of each elf's list of calories
clean_input = [x.rstrip() for x in input]



# number of games per day is not fixed
# colour of cubes are fixed
# based on each game, what is the maximum number of each colour
# hierarchy - game, reveal, colour

answer1 = 0
answer2 = 0

for line in clean_input:
    d = {}
    id, reveals = line.split(':')

    id = int(id.split(' ')[1])


    red   = 0
    green = 0
    blue  = 0

    reveals = reveals.split(';')   
    for reveal in reveals:
        cubes = reveal.split(',')
        for cube in cubes:
            _, val, colour = cube.split(' ')
            val = int(val)

            if colour == 'red':
                
                red = max(red, val)
            elif colour == 'green':
                green = max(green, val)
            elif colour == 'blue':
                blue = max(blue, val)

    if (red <= 12) & (green <= 13) & (blue <= 14):
        answer1 += id

    power = red * blue * green
    answer2 += power

print(f'Solution Part 1: {answer1}')
print(f'Solution Part 2: {answer2}')

fp = 'day1.txt'

with open(fp,'r') as f:
    input = f.readlines()

# transform input string into list of each elf's list of calories
clean_input = [x.rstrip() for x in input]

lines = []
for input in clean_input:
    line = []
    for c in input:
        if c.isdigit():
            line.append(c)

    line = ''.join(line)

    lines.append(line)

vals = 0 
for line in lines:
    if len(line) == 1:
        val = 2*line  # this is string, not int
    else:
        val = line[0] + line[-1]  # still string manipulation, not math

    val = int(val)
    vals += val

print(f'Solution Part 1: {vals}')


### PART TWO ###

# for line in clean inputs
# subst digit 
# everything else is the same

d_digit_subsitution = {
    'one'   : '1',
    'two'   : '2',
    'three' : '3',
    'four'  : '4',
    'five'  : '5',
    'six'   : '6',
    'seven' : '7',
    'eight' : '8',
    'nine'  : '9'
} 

subst_input = []
for input in clean_input:
    line = input
    for k,v in d_digit_subsitution.items():
        line = line.replace(k,v)
    subst_input.append(line)    

    # TODO: xtwone3four causes an issue. two should be rendered first, before one



lines = []
for input in subst_input:
    line = []
    for c in input:
        if c.isdigit():
            line.append(c)

    line = ''.join(line)

    lines.append(line)


vals = 0 
for line in lines:
    if len(line) == 1:
        val = 2*line  # this is string, not int
    else:
        val = line[0] + line[-1]  # still string manipulation, not math

    val = int(val)
    vals += val
    print(line,val)


print(f'Solution Part 2: {vals}')

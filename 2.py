with open("2.txt", "r") as file:
    lines = [[i.split()[0], int(i.split()[1])] for i in file.readlines()]

depth = 0
pos = 0
aim = 0

for line in lines:
    if line[0] == "forward":
        pos += line[1]
        depth += aim*line[1]
    elif line[0] == "down":
        aim += line[1]
    elif line[0] == "up":
        aim -= line[1]

print(pos*depth)

with open("3.txt", "r") as file:
    lines = [i for i in file.readlines()]

gamma = ""
epsilon = ""

for i in range(len(lines[0])-1):
    count_zero = 0
    count_one = 0
    for line in lines:
        if line[i] == "0":
            count_zero += 1
        elif line[i] == "1":
            count_one += 1
    if count_one > count_zero:
        gamma += "1"
        epsilon += "0"
    elif count_one < count_zero:
        gamma += "0"
        epsilon += "1"

output = int(gamma, 2) * int(epsilon, 2)
print(output)

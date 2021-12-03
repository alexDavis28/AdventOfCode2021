with open("3.txt", "r") as file:
    lines = [i for i in file.readlines()]

gamma = ""
epsilon = ""

for i in range(len(lines[0]) - 1):
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
# print(output)

# Find oxygen rating

oxygen_lines = lines.copy()
n = 0
while len(oxygen_lines) > 1:
    count_zero = 0
    count_one = 0
    for line in oxygen_lines:
        if line[n] == "0":
            count_zero += 1
        elif line[n] == "1":
            count_one += 1
    if count_one > count_zero:
        oxygen_lines = [i for i in oxygen_lines if i[n] == "1"]
    elif count_one < count_zero:
        oxygen_lines = [i for i in oxygen_lines if i[n] == "0"]
    elif count_one == count_zero:
        oxygen_lines = [i for i in oxygen_lines if i[n] == "1"]
    n += 1

oxygen = int(oxygen_lines[0], 2)

# Find scrubber

scrubber_lines = lines.copy()
n = 0
while len(scrubber_lines) > 1:
    count_zero = 0
    count_one = 0
    for line in scrubber_lines:
        if line[n] == "0":
            count_zero += 1
        elif line[n] == "1":
            count_one += 1
    if count_one < count_zero:
        scrubber_lines = [i for i in scrubber_lines if i[n] == "1"]
    elif count_one > count_zero:
        scrubber_lines = [i for i in scrubber_lines if i[n] == "0"]
    elif count_one == count_zero:
        scrubber_lines = [i for i in scrubber_lines if i[n] == "0"]
    n += 1

scrubber = int(scrubber_lines[0], 2)
print(oxygen*scrubber)

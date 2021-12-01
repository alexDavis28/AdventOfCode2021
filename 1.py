def part_one():
    with open("1.txt", "r") as file:
        text = [int(i) for i in file.readlines()]

    increases = 0

    for x, value in enumerate(text[1:]):
        print(x, value)
        if value > text[x]:
            increases += 1
            print(increases)
    print(increases)


def part_two():
    with open("1.txt", "r") as file:
        values = [int(i) for i in file.readlines()]

    sums = []

    for x, i in enumerate(values):
        if (x + 2) == len(values):
            break
        else:
            sums.append(sum([i, values[x + 1], values[x + 2]]))

    increases = 0

    for x, value in enumerate(sums[1:]):
        if value > sums[x]:
            increases += 1
    print(increases)


part_two()

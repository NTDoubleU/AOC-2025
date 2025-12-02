filename = "C:\\Users\\nathan wright\\Desktop\\FOLDER OF FOLDERS\\Personal Code Archive\\Advent of code 2025\\Day 1\\data.txt"

def solve_part1(filename):
    pos = 50   # starting position
    hits_on_zero = 0

    with open(filename) as f:
        for line in f:
            line = line.strip()

            direction = line[0]      # 'L' or 'R'
            amount = int(line[1:])   # number after the letter

            # L = left = lower numbers = subtract
            # R = right = higher numbers = add
            if direction == "L":
                pos = (pos - amount) % 100
            else:
                pos = (pos + amount) % 100

            # Count whenever we land on 0
            if pos == 0:
                hits_on_zero += 1

    return hits_on_zero

print("Password:", solve_part1(filename))


def solve_part2(filename):
    pos = 50
    hits_on_zero = 0

    with open(filename) as f:
        for line in f:
            line = line.strip()
            direction = line[0]
            amount = int(line[1:])

            if direction == "L":
                step = -1
            else:
                step = 1

            # simulate each click!
            for _ in range(amount):
                pos = (pos + step) % 100
                if pos == 0:
                    hits_on_zero += 1

    return hits_on_zero


print("Part 2 Password:", solve_part2(filename))

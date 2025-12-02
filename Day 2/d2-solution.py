filename = "C:\\Users\\nathan wright\\Desktop\\FOLDER OF FOLDERS\\Personal Code Archive\\Advent of code 2025\\Day 2\\data.txt"

def p1_is_invalid_id(num):
    """Check if a number is invalid (made by repeating a sequence exactly twice)."""
    s = str(num)
    n = len(s)
    if n % 2 != 0:
        return False  # odd length cannot be repeated twice
    half = n // 2
    return s[:half] == s[half:]  # first half equals second half

def solve_part1(filename):
    total_invalid = 0

    with open(filename) as f:
        line = f.read().strip()  # all ranges are on a single line

    ranges = line.split(",")
    for r in ranges:
        start, end = map(int, r.split("-"))
        for num in range(start, end + 1):
            if p1_is_invalid_id(num):
                total_invalid += num

    return total_invalid

print("Sum of invalid IDs (Part 1):", solve_part1(filename))

# Part 2

def p2_is_invalid_id(num):
    s = str(num)
    # duplicate the string, remove first and last character, and see if original exists inside
    return s in (s + s)[1:-1]

def solve_part2(filename):
    total_invalid = 0

    with open(filename) as f:
        line = f.read().strip()  

    ranges = line.split(",")
    for r in ranges:
        start, end = map(int, r.split("-"))
        for num in range(start, end + 1):
            if p2_is_invalid_id(num):
                total_invalid += num

    return total_invalid

print("Sum of invalid IDs (Part 2):", solve_part2(filename))

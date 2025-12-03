filename = "C:\\Users\\nathan wright\\Desktop\\FOLDER OF FOLDERS\\Personal Code Archive\\Advent of code 2025\\Day 3\\data.txt"

def p1_max_joltage_from_line(line):
    # Convert the line into a list of digits
    digits = [int(ch) for ch in line.strip() if ch.isdigit()]
    
    best = 0  

    # Check all pairs of digits in order
    for i in range(len(digits) - 1):
        for j in range(i + 1, len(digits)):
            value = digits[i] * 10 + digits[j]
            if value > best:
                best = value

    return best

def p1_solve_total_joltage(filename):
    total = 0

    with open(filename) as f:
        for line in f:
            total += p1_max_joltage_from_line(line)

    return total

print("Total output joltage:", p1_solve_total_joltage(filename))

def p2_max_number_from_line_greedy(digits, pick):
    number = 0
    start = 0
    n = len(digits)
    
    for remaining in range(pick, 0, -1):
        # Only look ahead as far as needed to still pick remaining digits
        end = n - remaining + 1
        best_digit = max(digits[start:end])
        best_index = digits.index(best_digit, start, end)
        number = number * 10 + best_digit
        start = best_index + 1  # move past the picked digit
        
    return number

def p2_solve_total_joltage(filename, pick):
    total = 0
    with open(filename) as file:
        for line in file:
            digits = [int(ch) for ch in line.strip() if ch.isdigit()]
            if len(digits) >= pick:
                total += p2_max_number_from_line_greedy(digits, pick)
    return total

# Run the solver for 12 digits per line
print("Total output joltage:", p2_solve_total_joltage(filename, 12))


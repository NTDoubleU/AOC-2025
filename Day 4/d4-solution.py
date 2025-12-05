filename = "C:\\Users\\nathan wright\\Desktop\\FOLDER OF FOLDERS\\Personal Code Archive\\Advent of code 2025\\Day 4\\data.txt"

def p1_accessible_rolls(filename):
    # Read file in grid format
    with open(filename, 'r') as f:
        grid = [line.strip() for line in f]

    rows = len(grid) #number of rows
    cols = len(grid[0]) #number of columns

    #area to check around each roll
    check_area = [
        (-1,-1), (-1,0), (-1,1),
        (0,-1),          (0,1), 
        (1,-1),  (1,0),  (1,1)
    ]

    accessible_rolls = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@': # skip if not a roll
                continue

            count = 0

            for dr, dc in check_area: #check surrounding area
                nr, nc = r + dr, c + dc 

                if 0 <= nr < rows and 0 <= nc < cols: #ensure not our of bounds
                    if grid[nr][nc] == '@':
                        count += 1

            if count < 4:  #if less than 4 rolls ad to accessible count
                accessible_rolls += 1
            
    return accessible_rolls
    
print(p1_accessible_rolls(filename))
    

def p2_accessible_rolls(filename):
    # Read file in grid format
    with open(filename, 'r') as f:
        grid = [list(line.strip()) for line in f]

    rows = len(grid) #number of rows
    cols = len(grid[0]) #number of columns

    #area to check around each roll
    check_area = [
        (-1,-1), (-1,0), (-1,1),
        (0,-1),          (0,1), 
        (1,-1),  (1,0),  (1,1)
    ]

    accessible_rolls = 0
    changed = True

    while changed:  # repeat until no changes
            changed = False
            new_grid = [row[:] for row in grid]

            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] != '@':
                        continue

                    # count neighbors
                    count = 0
                    for dr, dc in check_area:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == '@':
                                count += 1

                    # rule
                    if count < 4:
                        new_grid[r][c] = 'x'
                        accessible_rolls += 1
                        changed = True

            grid = new_grid  # update entire grid at once

    return accessible_rolls

print(p2_accessible_rolls(filename))

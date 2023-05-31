# Application checks whether a completed Sudoku puzzle has a valid solution
# User inputs row from their completed Sudoku puzzle. Rows printed for verification

rows = []
[rows.append(input("Please enter the next row: ")) for x in range(0, 9)]
sudoku_valid = True
print(rows)

# Checking if all rows are valid (checking that all numbers 1 through 9 appear once per row)

for x in range(1, 10):
    for y in range(0, 9):
        if rows[y].find(str(x)) == -1:
            sudoku_valid = False

# Checking if all columns are valid
# First creating a list of columns from the initial row input

columns = []
new_column = ""
for x in range(0, 9):
    for y in range(0, 9):
        new_column += rows[y][x]
    columns.append(new_column)
    new_column = ""

# Checking if all columns are valid (checking that all numbers 1 through 9 appear once per columns)

for x in range(1, 10):
    for y in range(0, 9):
        if columns[y].find(str(x)) == -1:
            sudoku_valid = False

# Checking if all 9x9 boxes are valid
# First creating a list of boxes from the initial row input

boxes = []
for x in range(0, 9, 3):
    boxes.append(rows[0][x:(x+3)] + rows[1][x:(x+3)] + rows[2][x:(x+3)])
    boxes.append(rows[3][x:(x+3)] + rows[4][x:(x+3)] + rows[5][x:(x+3)])
    boxes.append(rows[6][x:(x+3)] + rows[7][x:(x+3)] + rows[8][x:(x+3)])

# Checking if all 9x9 boxes are valid (checking that all numbers 1 through 9 appear once per box)

for x in range(1, 10):
    for y in range(0, 9):
        if boxes[y].find(str(x)) == -1:
            sudoku_valid = False

# Print statement output

if sudoku_valid is True:
    print("Yes, solution is valid")
else:
    print("No, solution is not valid")

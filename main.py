from classes import Cell, Puzzle

puzzle1 = Puzzle('sudoku1.csv')


# print(type(puzzle1.cells))
# print(puzzle1.cells)
assert type(puzzle1.cells) is list   # make sure cells are in a list


cell = puzzle1.cells[0][0]
print(cell.row)
print(cell.col)
print(cell.grid)


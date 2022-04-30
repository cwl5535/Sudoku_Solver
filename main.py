from classes import Cell, Puzzle

puzzle1 = Puzzle('sudoku1.csv')


# print(type(puzzle1.cells))
# print(puzzle1.cells)
assert type(puzzle1.cells) is list   # make sure cells are in a list


cell = puzzle1.cells[8][8]
print(cell.options, cell.grid_location)


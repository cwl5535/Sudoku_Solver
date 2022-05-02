from classes import Cell, Puzzle

puzzle1 = Puzzle('sudoku1.csv')


assert type(puzzle1.cells) is list   # make sure cells are in a list


cell = puzzle1.cells[8][8]
puzzle1.Greedy()

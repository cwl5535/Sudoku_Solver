class Puzzle:
    def __init__(self, filename):
        self.filename = filename
        self.importData()

    def importData(self):
        '''
        Data is imported and formatted. Zeros are inserted where there are empty spaces. 
        '''
        with open(self.filename) as file:
            puzzle = []
            for lines in file.readlines():
                line = lines.rstrip()
                row = []
                idx = -1
                for char in line:
                    row.append(char)
                for char in row: 
                    if char == row[idx]:
                        row.insert(idx+1, "0")
                    elif row[0] == ";":
                        row.insert(0, "0")
                    elif row[-1] == ";":
                        row.append("0")
                    idx += 1
                puzzle.append(row)
            for row in puzzle: 
                print(row)
#TODO begin solving Sudoku, watch lecture videos



puzzle1 = Puzzle('sudoku1.csv')
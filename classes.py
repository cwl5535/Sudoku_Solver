class Puzzle:
    def __init__(self, filename):
        self.filename = filename
        self.rows = []
        self.options = list(range(1,10))
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
                    row.append(char)  # puts data into a list format
                for char in row: 
                    # if statements do not affect the fixed values
                    if char == row[idx]:  #if the current character equals the one before it, add a 0 to the beginning of the list
                        row.insert(idx+1, "0")
                    elif row[0] == ";":  #if the first character is a semicolon, add a 0 before it
                        row.insert(0, "0")
                    elif row[-1] == ";":  # if the last character is a semicolon, add a 0 to the end
                        row.append("0")
                    idx += 1
                row = list(filter(lambda val: val != ";", row))  # removes semicolons
                self.rows.append(row)
            # for row in self.rows:
            #     # print(row)
#TODO start with a Greedy search and then work with local search
#TODO create list of options to work with and remove options if value is in the row, column, or grid
    def filterOptions(self):
        for row in self.rows:
            for val in row:
                if val in self.options:
                    self.options.remove(val)
                print(self.options)
    def Greedy(self):
        
    # def tryGuess(): 
    #     if 
    # def backtrack(): 


puzzle1 = Puzzle('sudoku1.csv').Greedy()
# print("----break----")
# puzzle2 = Puzzle('sudoku2.csv')
# print("----break----")
# puzzle3 = Puzzle('sudoku3.csv')
# print("----break----")
# puzzle4 = Puzzle('sudoku4.csv')
# print("----break----")
# puzzle5 = Puzzle('sudoku5.csv')
# print("----break----")
# puzzle6 = Puzzle('sudoku6.csv')
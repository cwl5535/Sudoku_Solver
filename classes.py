class Puzzle:
    def __init__(self, filename):
        self.filename = filename
        self.rows = []
        # self.options = list(range(1,10))
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
#TODO apply greedy after each row is filtered
    def filterOptions(self, row, options):
        # for row in self.rows:
        #     options =  ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for val in row:
            if val in options:
                options.remove(val)  # removing the option if it exists in the row
                # print(options), print("REMOVED " + val)
        return options
        # print("----NEW ROW----")

    def Greedy(self):
        row_no = 1
        for row in self.rows: 
            options =  ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            filtered_options = self.filterOptions(row, options)
            index = 0

            for val in row:
                if len(options) == 0:  # if there are no more options, leave loop
                    break 
                elif val == "0":
                    row[index] = filtered_options[0]
                    filtered_options.pop(0)
                # print("options: " + str(filtered_options))
                index += 1
            # print("row " + str(row_no) + ": " + str(row))
            row_no += 1

def improve(self):
    




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
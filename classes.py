
class Cell:
    def __init__(self, value, rows, fixed, row = [], col = []):
        self.value = value
        self.row = row 
        self.col = col
        self.rows = rows
        self.fixed = fixed
        self.options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    def assignGrid(self):

        ''' 
    Grid Numbering: 

    |__1__||__2__||__3__|
    |__4__||__5__||__6__|
    |__7__||__8__||__9__|
    
        '''

        if self.row_no <= 2:
            if self.col_no <= 2:
                self.grid_location = 1
            elif (self.col_no > 2) and (self.col_no <= 5):
                self.grid_location = 2
            elif (self.col_no > 5) and (self.col_no < 10):
                self.grid_location = 3
        elif  (self.row_no > 2) and  (self.row_no <= 5):
            if self.col_no <= 2:
                self.grid_location = 4
            elif (self.col_no > 2) and (self.col_no <= 5):
                self.grid_location = 5
            elif (self.col_no > 5) and (self.col_no < 10):
                self.grid_location = 6
        elif  (self.row_no > 5) and  (self.row_no < 10):
            if self.col_no <= 2:
                self.grid_location = 7
            elif (self.col_no > 2) and (self.col_no <= 5):
                self.grid_location = 8
            elif (self.col_no > 5) and (self.col_no < 10):
                self.grid_location = 9

    def filterCellOptions(self):
        # check values in row
        for val in self.row:
            if val in self.options:
                self.options.remove(val)  # removing the option if it exists in the row
        
        # check values in column
        for val in self.col: 
            if val in self.options: 
                self.options.remove(val)

        # check values in grid
        for val in self.grid:
            if val in self.options:
                self.options.remove(val)

class Puzzle:
    def __init__(self, filename):
        self.cells = []
        self.filename = filename
        self.rows = []
        self.importData()  # puzzle is created with 0s as placeholders for non fixed values
        self.columns = [[],[],[],[],[],[],[],[],[]]
        self.createColumns()
        self.createCells()
        self.assignCellLocations()
        self.createGrid()

    def createGrid(self): # want a list of options within in the grid
        grids = [[],[],[],[],[],[],[],[],[]]
        for row in self.cells: # self.cells are Cell objects

            # Create list of all the grids based on the cells location number
            for cell in row: 
                if cell.grid_location == 1:
                    grids[0].append(cell.value)
                elif cell.grid_location == 2:
                    grids[1].append(cell.value)
                elif cell.grid_location == 3:
                    grids[2].append(cell.value)
                elif cell.grid_location == 4:
                    grids[3].append(cell.value)
                elif cell.grid_location == 5:
                    grids[4].append(cell.value)
                elif cell.grid_location == 6:
                    grids[5].append(cell.value)
                elif cell.grid_location == 7:
                    grids[6].append(cell.value)
                elif cell.grid_location == 8:
                    grids[7].append(cell.value)
                elif cell.grid_location == 9:
                    grids[8].append(cell.value)

    # assign an attribute 'grid' to each cell based on the cells within its grid
        for row in self.cells:
            for cell in row:       
                if cell.grid_location == 1:
                    cell.grid = grids[0]
                elif cell.grid_location == 2:
                    cell.grid = grids[1]
                elif cell.grid_location == 3:
                    cell.grid = grids[2]
                elif cell.grid_location == 4:
                    cell.grid = grids[3]
                elif cell.grid_location == 5:
                    cell.grid = grids[4]
                elif cell.grid_location == 6:
                    cell.grid = grids[5]
                elif cell.grid_location == 7:
                    cell.grid = grids[6]
                elif cell.grid_location == 8:
                    cell.grid = grids[7]
                elif cell.grid_location == 9:
                    cell.grid = grids[8]

    def assignCellLocations(self):
        r = 0
        for row in self.cells: 
            c = 0
            for cell in row: 
                self.cells[r][c].row_no = self.cells.index(row)  # each cells row number
                self.cells[r][c].col_no = self.cells[self.cells[r][c].row_no].index(cell) # each cells column number
                self.cells[r][c].assignGrid()  #assigns grid number to cell instance
                c += 1
                # can only index the list within the list so the row which gives column value
            r += 1
    
    def createColumns(self):
        # modifies self.columns matrix to give to each Cell instance to know what other values are in its column
        for row in self.rows:
            loop = 0 
            for col in row: 
                    self.columns[loop].append(col)  # trying to get [[col_1],[col_2],[col_3],[col_4]]
                    loop += 1
        # print(self.columns[0])

    def createCells(self):
        # create Cell instances and add to 'cells' attribute
        for row in self.rows:
            self.cell_row = []
            loop = 0 
            for col in row: 
                # self.cell_row.append(Cell(col, self.rows, row, self.columns[loop]))  # create a matrix of cells
                if col != '0': 
                    self.cell_row.append(Cell(col, self.rows, True, row, self.columns[loop]))  # create a matrix of cells
                else:
                    self.cell_row.append(Cell(col, self.rows, False, row, self.columns[loop]))  # create a matrix of cells
                loop += 1
            self.cells.append(self.cell_row)
        # print(self.cells)

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

    def Greedy(self):
        # method for initial attempt to solve the problem 
        for row in self.cells: 
            for cell in row:
                cell.filterCellOptions() 
                if not cell.fixed: 
                    cell.value = (cell.options[0])
                    cell.options.pop(0)

        self.toPuzzle()
    
    def toPuzzle(self):
        # puzzle_list = []
        for row in self.cells: 
            row_list = []
            for cell in row: 
                row_list.append(cell.value)
            print(row_list)
            # puzzle_list.append(row_list)


#TODO self.row, self.col, and self.grid need to be updated after each guess so that the filter works
        


# def improve(rows):
#     # check each value now, starting with the second row (assuming first row is right)
#     for val in rows[1::]:

        

# def columnCheck(self):
#     # check at the cell level
#     options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#     options.pop(index(self.rows[0][]))
#     for item in self.rows: 
# # 

# def gridCheck(self): 
    # check at the cell level
    # if index() = 0, 3, 6 look to the right 2, if index() = 1,4,7 look to the left and right, and if index() == 2,5,8 look to the left two

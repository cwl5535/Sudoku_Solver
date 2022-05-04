
class Cell:
    def __init__(self, value, rows, fixed, row, col):
        # cells also have .row_no, .col_no, .grid, and .grid_location
        self.value = value
        self.row = row 
        self.col = col
        self.rows = rows
        self.fixed = fixed
        self.options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    def assignGrid(self):

        ''' 
    Cell Method
    
    Description: Assigns a the grid_location atrribute to each cell object based on the cell's location. 
    Input(s): None
    Returns: None

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

        """
        Cell Method
        
        Description: Used for checking the current row, column, and grid that the cell is and removing any values seen from the options to use for the value of the current cell. 
        Input(s): None
        Returns: None
        """
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

    def updates(self, puzzle_object): 
        """
        Cell Method

        Description: Wrapper function used for updating columns and rows of a current Cell object after a guess has been made
        Input(s): Puzzle Object
        Returns: None
        """
        self.updateColumns(puzzle_object)
        self.updateRows(puzzle_object)
        # grids updated with Puzzle method, createGrid()
    
    def updateRows(self, puzzle_object): 
        """
        Cell Method

        Description: Wrapper function used for updating rows of a current Cell object after a guess has been made
        Input(s): Puzzle Object
        Returns: None
        """

        #create updated rows
        rows = [[],[],[],[],[],[],[],[],[]]
        # idx = 0
        # for row in puzzle_object.cells: 
        #     rows[idx].append(row)
        #     idx += 1
        
        # assign updated rows to Cell objects self.row attribute
        idx = 0 
        for row in puzzle_object.cells:
            for cell in row: 
                rows[idx].append(cell.value)
                if cell.row_no == idx: 
                    cell.row = rows[idx]
                assert type(rows[0][0]) is str
            idx += 1

    def updateColumns(self, puzzle_object): 
        """
        Cell Method

        Description: Wrapper function used for updating columns of a current Cell object after a guess has been made
        Input(s): Puzzle Object
        Returns: None

        [[col_1],[col_2],[col_3],[col_4],[col_5],[col_6],[col_7],[col_8],[col_9]]
        """


        #create updated columns
        columns = [[],[],[],[],[],[],[],[],[]]
        for row in puzzle_object.cells:
            loop = 0 
            for cell in row: 
                    columns[loop].append(cell.value) 
                    loop += 1
        
        # assign updated columns to Cell objects self.col attribute
        for row in puzzle_object.cells:
            idx = 0 
            for cell in row: 
                if cell.col_no == idx: 
                    cell.col = columns[idx]
                idx += 1           

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

    def createGrid(self): 
        """
        Puzzle Method
        Description: Creates lists, each containing on of the 9 puzzle grids, and assigns them to each cell based on grid location (self.grid_location)
        Input(s): None
        Returns: None
        
        """
        
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

    # assign an attribute 'grid' to each Cell object based on the cells within its grid
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
        """
        Puzzle Method
        Description: Determines the row and column numbers (self.row_no and self.col_no) that a cell is located and then assigns a grid location
        Input(s): None
        Returns: None
        """
        r = 0
        for row in self.cells: 
            c = 0
            for cell in row: 
                self.cells[r][c].row_no = self.cells.index(row)  # each cells row number
                self.cells[r][c].col_no = self.cells[self.cells[r][c].row_no].index(cell) # each cells column number
                self.cells[r][c].assignGrid()  #assigns grid number to cell instance
                c += 1
            r += 1
    
    def createColumns(self):
        '''
        Puzzle Method
        Description: Creates a list that contains 9 lists, all of which are each of the columns. This is used later to assign Cell.col 
        Input(s): None
        Returns: self.columns 
        
        List setup -> [[col_1],[col_2],[col_3],[col_4], [col_5], [col_6], [col_7], [col_8], [col_9]]
        '''
        
        for row in self.rows:
            loop = 0 
            for col in row: 
                    self.columns[loop].append(col) 
                    loop += 1
        return self.columns

    def createCells(self):
        '''
        Puzzle Method
        Actions: Used to create a 9 x 9 matrix (list) where each of the cells contains a 'Cells' object
        Creates: self.cells (Puzzle object attribute containing a list of lists. Each list is a puzzle row containing 'Cell' objects)
        Returns: None
        '''
        for row in self.rows:
            cell_row = []  # placeholder list
            loop = 0 
            for col in row: 
                if col != '0': 
                    # if not a blank cell (0), make the cell fixed
                    cell_row.append(Cell(col, self.rows, True, row, self.columns[loop]))  # create a matrix of cells
                else:
                    # cell is not made fixed
                    cell_row.append(Cell(col, self.rows, False, row, self.columns[loop]))  # create a matrix of cells
                loop += 1
            self.cells.append(cell_row)

    def importData(self):
        '''
        Puzzle Method
        Description: Used to import and format data. Zeros are inserted where there are empty spaces. 
        Input(s): None
        Returns: None
        '''
        with open(self.filename) as file:
            for lines in file.readlines():
                line = lines.rstrip()
                row = []
                idx = -1  # index starts at -1 to look at last object in list
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
        '''
        Puzzle Method
        Description: Used for initial attempt to solve the problem 
        Input(s): None
        Returns: None
        '''
        print("\n\n---------------------------------\n")
        print("---      S O L U T I O N      ---\n")
        print("---------------------------------\n")
        for row in self.cells: 
            for cell in row:
                cell.filterCellOptions()
                if not cell.fixed:
                    if len(cell.options) != 0: 
                        cell.value = (cell.options[0])
                        cell.options.pop(0)
                        self.createGrid()   # updating the grids
                        cell.updates(self)  # updates rows and columns
                    # else: 
                    #     # try the previous cells OTHER option
                    #     if cell.col_no == 0:
                    #         # if all the way to the left side of the puzzle, move UP a row and try again
                            
                    #         prev_cell = self.cells[cell.row_no-1][cell.col_no-3]
                    #         print(prev_cell.options)
                    #         prev_cell.value = (prev_cell.options[1])
                    #         self.createGrid()   # updating the grids
                    #         cell.updates(self)  # updates rows and columns
                    #     else:
                    #         prev_cell = self.cells[cell.row_no][cell.col_no-3]
                    #         print(prev_cell.options)
                    #         prev_cell.value = (prev_cell.options[1])
                    #         self.createGrid()   # updating the grids
                    #         cell.updates(self)  # updates rows and columns
                    #     self.Greedy()
        self.getCost()
        # t = self.cells[2][8]
        # print("\n\n\n" + str(t.options))
        # print(str(t.fixed))
        # print(str(t.row))
        # print(str(t.col))
    
 

    
    def getCost(self) -> int:
        '''
        Puzzle Method
        Description: Used to get the cost of each row within the puzzle
        Input(s): None
        Returns: row_cost (int) - the total cost of each row of the puzzle i.e. how many cells will need to be changed after the Greedy
        '''
        
        puzzle_rows = self.toPuzzle()
        r_num = 0
        
        print("\n\n---------------------------------\n")
        print("---     R O W   C O S T S     ---\n")
        print("---------------------------------\n")
        
        for row in puzzle_rows: 
            row_cost = 0
            row_appeared = []   # elements that have appeared in the row will be added to this list
            for cell in row: 
                if cell == "0":
                    row_cost += 1 
                elif cell not in row_appeared:  # if the cell hasn't appeared already, add it to the list
                    row_appeared.append(cell)
                else:
                    row_cost += 1
            r_num += 1
            print("Row " + str(r_num) + " Cost: " + str(row_cost))
        return row_cost



    def toPuzzle(self) -> list:
        '''
        Puzzle Method
        Actions: Prints each row of the puzzle
        Input(s): None
        Returns: puzzle_list (list) - list of lists containing the entire puzzle values, where each row is a list
        '''
        puzzle_list = []
        r_num = 0
        for row in self.cells:
            r_num += 1
            row_list = []
            for cell in row: 
                row_list.append(cell.value)
            print("Row " + str(r_num) + ": " + str(row_list))
            puzzle_list.append(row_list)
        print("\n")
        return puzzle_list
        
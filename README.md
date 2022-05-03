# Sudoku Solver (CS5007 Final Project)

## **Table of Contents**
1. [How to Solve a Puzzle](#how-to-solve-a-puzzle)
2. [Puzzles](#puzzles)
3. [Classes](#classes)

## **How to Solve a Puzzle**
1. ### Open and run `main.py`
2. ### You will then be prompted in the terminal: 
        
        Which sudoku puzzle would you like the computer to solve?

        1 | 2 | 3 | 4 | 5 | 6

        (To see preview of a puzzle, enter 'p'.) 

    You have 2 options here: 
    
    1.  #### *Solve a Puzzle*
    
        Enter a Puzzle Number
        
        - **Options**: 1 , 2 , 3 , 4 , 5 , and 6
        - Proceed to [Solving the Puzzle](#3--solving-the-puzzle)
        
    
    2. #### *Preview a Puzzle* 
    
        (Enter 'p' [not case sensitive] to preview a puzzle.)
    
            p
                
        * If preview is chosen, a follow up prompt will appear: 
 
                Which puzzle which you like to preview?

                1 | 2 | 3 | 4 | 5 | 6 ? 

        * Enter a choice (1 , 2 , 3 , 4 , 5 , or 6) from the above options.

                1 
        
        * The chosen puzzle (in this example, `1`) is printed to the terminal

                Row 1: ['0', '0', '3', '0', '0', '0', '0', '9', '0']
                Row 2: ['0', '1', '0', '0', '7', '0', '2', '0', '4']
                Row 3: ['4', '0', '0', '0', '0', '1', '0', '5', '0']
                Row 4: ['0', '0', '0', '9', '0', '0', '3', '0', '0']
                Row 5: ['0', '8', '0', '0', '1', '0', '0', '7', '0']
                Row 6: ['0', '0', '6', '0', '0', '4', '0', '0', '0']
                Row 7: ['0', '3', '0', '5', '0', '0', '0', '0', '7']
                Row 8: ['9', '0', '5', '0', '8', '0', '0', '6', '0']
                Row 9: ['0', '7', '0', '0', '0', '0', '4', '0', '0']

        * The original prompt will then reappear:
                    
                Which sudoku puzzle would you like the computer to solve?

                1 | 2 | 3 | 4 | 5 | 6

                (To see preview of a puzzle, enter 'p'.)
            Enter a puzzle number to solve the desired puzzle.  
3. ### Solving the Puzzle         
    
    * Once you've entered a puzzle number, the computer will solve the puzzle. In this example, the puzzle is **Puzzle 1**. 

            1
    
            ---------------------------------

            ---      S O L U T I O N      ---

            ---------------------------------

            Row 1: ['2', '5', '3', '2', '3', '5', '1', '9', '3']
            Row 2: ['6', '1', '8', '6', '7', '8', '2', '8', '4']
            Row 3: ['4', '9', '7', '0', '9', '1', '6', '5', '0']
            Row 4: ['1', '2', '4', '9', '2', '5', '3', '1', '2']
            Row 5: ['3', '8', '9', '3', '1', '6', '5', '7', '6']
            Row 6: ['5', '0', '6', '7', '0', '4', '8', '0', '9']
            Row 7: ['8', '3', '1', '5', '2', '6', '1', '2', '7']
            Row 8: ['9', '2', '5', '1', '8', '3', '0', '6', '3']
            Row 9: ['0', '7', '0', '0', '9', '0', '4', '8', '5']
        
    * In addition to the attempted solution, the `cost` of each row is printed to the terminal. The higher the cost, the more elements need reassigned to achieve the true solution. 

            ---------------------------------

            ---     R O W   C O S T S     ---

            ---------------------------------

            Row 1 Cost: 4
            Row 2 Cost: 3
            Row 3 Cost: 2
            Row 4 Cost: 3
            Row 5 Cost: 2
            Row 6 Cost: 2
            Row 7 Cost: 2
            Row 8 Cost: 1
            Row 9 Cost: 3

---
## **Puzzles**
    
**Note**: *Zeros* (0) *are placeholders for empty cells*

### Puzzle 1
   
    Row 1: ['0', '0', '3', '0', '0', '0', '0', '9', '0']
    Row 2: ['0', '1', '0', '0', '7', '0', '2', '0', '4']
    Row 3: ['4', '0', '0', '0', '0', '1', '0', '5', '0']
    Row 4: ['0', '0', '0', '9', '0', '0', '3', '0', '0']
    Row 5: ['0', '8', '0', '0', '1', '0', '0', '7', '0']
    Row 6: ['0', '0', '6', '0', '0', '4', '0', '0', '0']
    Row 7: ['0', '3', '0', '5', '0', '0', '0', '0', '7']
    Row 8: ['9', '0', '5', '0', '8', '0', '0', '6', '0']
    Row 9: ['0', '7', '0', '0', '0', '0', '4', '0', '0']

### Puzzle 2
    
    Row 1: ['1', '0', '8', '0', '2', '6', '0', '0', '0']
    Row 2: ['3', '7', '0', '0', '1', '0', '0', '0', '0']
    Row 3: ['0', '0', '2', '0', '0', '7', '0', '0', '0']
    Row 4: ['0', '0', '0', '0', '0', '8', '0', '0', '5']
    Row 5: ['0', '5', '0', '0', '0', '0', '0', '0', '7']
    Row 6: ['0', '3', '6', '0', '0', '0', '0', '0', '0']
    Row 7: ['0', '0', '0', '9', '0', '0', '0', '5', '3']
    Row 8: ['0', '0', '0', '3', '0', '1', '7', '0', '0']
    Row 9: ['7', '9', '0', '2', '0', '0', '0', '0', '8']

### Puzzle 3

    Row 1: ['0', '0', '0', '0', '0', '0', '0', '0', '1']
    Row 2: ['9', '0', '1', '0', '0', '2', '0', '4', '3']
    Row 3: ['0', '0', '0', '0', '0', '0', '9', '0', '0']
    Row 4: ['0', '0', '0', '0', '5', '6', '0', '0', '2']
    Row 5: ['0', '0', '0', '0', '1', '0', '0', '0', '0']
    Row 6: ['0', '0', '0', '0', '0', '0', '4', '3', '5']
    Row 7: ['1', '6', '0', '9', '8', '0', '0', '0', '0']
    Row 8: ['0', '5', '4', '0', '0', '0', '8', '0', '9']
    Row 9: ['0', '8', '0', '0', '0', '3', '0', '2', '0']

### Puzzle 4

    Row 1: ['0', '0', '0', '9', '0', '2', '8', '0', '0']
    Row 2: ['0', '4', '9', '0', '0', '1', '0', '7', '0']
    Row 3: ['7', '0', '0', '0', '0', '0', '0', '9', '0']
    Row 4: ['3', '5', '0', '0', '9', '0', '7', '0', '0']
    Row 5: ['0', '0', '0', '7', '0', '5', '0', '0', '0']
    Row 6: ['0', '0', '2', '0', '3', '0', '0', '8', '4']
    Row 7: ['0', '9', '0', '0', '0', '0', '0', '0', '3']
    Row 8: ['0', '6', '0', '3', '0', '0', '9', '1', '0']
    Row 9: ['0', '0', '5', '6', '0', '9', '0', '0', '0']

### Puzzle 5

    Row 1: ['0', '0', '8', '0', '0', '1', '5', '0', '0']
    Row 2: ['7', '4', '0', '0', '8', '0', '0', '0', '2']
    Row 3: ['6', '0', '0', '0', '0', '0', '0', '0', '0']
    Row 4: ['0', '0', '0', '2', '0', '9', '1', '7', '0']
    Row 5: ['0', '7', '0', '0', '0', '0', '0', '2', '0']
    Row 6: ['0', '3', '1', '7', '0', '8', '0', '0', '0']
    Row 7: ['0', '0', '0', '0', '0', '0', '0', '0', '5']
    Row 8: ['4', '0', '0', '0', '3', '0', '0', '6', '1']
    Row 9: ['0', '0', '3', '4', '0', '0', '9', '0', '0']

### Puzzle 6

    Row 1: ['8', '1', '0', '5', '2', '0', '0', '0', '0']
    Row 2: ['0', '2', '0', '4', '3', '0', '0', '0', '9']
    Row 3: ['0', '0', '4', '0', '0', '9', '0', '0', '0']
    Row 4: ['0', '0', '0', '0', '0', '0', '6', '7', '5']
    Row 5: ['0', '8', '0', '0', '0', '0', '0', '3', '0']
    Row 6: ['9', '5', '3', '0', '0', '0', '0', '0', '0']
    Row 7: ['0', '0', '0', '2', '0', '0', '3', '0', '0']
    Row 8: ['7', '0', '0', '0', '5', '1', '0', '6', '0']
    Row 9: ['0', '0', '0', '0', '6', '4', '0', '9', '8']

---
## **Classes**

### *Puzzle*

#### **Attributes**

1. ***self*.cells**

    * *Type:* `list`
    * *Description:* Contains a 9 x 9 `list` of `lists` that holds all of the puzzle's cells. Each of the 9 `lists` contain 9 `Cell` objects. Each of the 9 lists (of length 9) are the rows of the puzzle. 
    * *Origin:* 

2. ***self*.filename**

    * *Type:* `str`
    * *Description:* File name of the `.csv` sudoku file used as input. 


3. ***self*.rows**

    * *Type:* `list`
    * *Description:* 9 x 9 `list` of `lists`; Each of the 9 `lists` contain the values in the Puzzle's rows.


4. ***self*.columns**

    * *Type:* `list`
    * *Description:* 9 x 9 `list` of `lists`; Each of the 9 `lists` contain the values in the Puzzle's columns.



### *Cell*

#### **Attributes**
1. ***self*.value**

    * *Type:* `str`
    * *Description:* Contains the value of the cell. 


2. ***self*.row**

    * *Type:* `list`
    * *Description:* 9 element `list` containing the row that the `Cell` object is within. 


3. ***self*.col**

    * *Type:* `list`
    * *Description:* 9 element `list` containing the column that the `Cell` object is within. 


4. ***self*.rows**

    * *Type:* `list`
    * *Description:* 9 x 9 `list` of `lists`. Each of the 9 `lists` contains the puzzle's rows. 


5. ***self*.col_no**

    * *Type:* `int`
    * *Description:* Column number that the `Cell` object is located within. 


6. ***self*.row_no**

    * *Type:* `int`
    * *Description:* Row number that the `Cell` object is located within. 


7. ***self*.grid_location**

    * *Type:* `int`
    * *Description:* Grid number that the `Cell` object is located within. Grids are numbered as follows: 

        
            Grid Numbering: 

            |__1__||__2__||__3__|
            |__4__||__5__||__6__|
            |__7__||__8__||__9__|
            


8. ***self*.fixed**

    * *Type:* `bool`
    * *Description:* Whether or not the cell value is fixed. If the value was given from the beginning, it is **fixed**. 


9. ***self*.options**

    * *Type:* `list`
    * *Description:* `list` of options for the cell to choose from for guessing a solution; 
        
            self.options = [1,2,3,4,5,6,7,8,9]

10. ***self*.grid**

    * *Type:* `list`
    * *Description:* 9 element `list` containing the grid that the `Cell` object is within. 


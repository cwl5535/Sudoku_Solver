from sudoku_classes import Puzzle, Cell

def userInput():
    while True:
        answer = input("Which sudoku puzzle would you like the computer to solve?\n (To see preview of a puzzle, enter 'p'.)\n").lower()    
        if answer == 'p': 
            preview_question = input("Which puzzle which you like to preview? 1 | 2 | 3 | 4 | 5 | 6 ?\n").strip()
            if (int(preview_question) > 6) or (int(preview_question) > 1): 
                print("Please enter a valid puzzle number: 1 | 2 | 3 | 4 | 5 | 6 \n")
                continue
            puzzle = Puzzle("sudoku" + preview_question + ".csv").toPuzzle()
            continue
        elif answer == '1': 
            puzzle = Puzzle("sudoku1.csv")
            break
        elif answer == '2': 
            puzzle = Puzzle("sudoku2.csv")
            break
        elif answer == '3': 
            puzzle = Puzzle("sudoku3.csv")
            break
        elif answer == '4': 
            puzzle = Puzzle("sudoku4.csv")
            break
        elif answer == '5': 
            puzzle = Puzzle("sudoku5.csv")
            break
        elif answer == '6': 
            puzzle = Puzzle("sudoku6.csv")
            break
        else: 
            print("Invalid Input! Enter the puzzle number or 'p' to preview a puzzle.")
    return puzzle

def main(): 
    puzzle = userInput()
    puzzle.Greedy()
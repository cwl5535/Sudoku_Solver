with open('sudoku1.csv', newline = '') as file:
    for line in file.readlines():
        row = ''
        for char in line: 
            if (char == ";"): 
                row += "0;"
            else: 
                row += (char + ";")
        print(row)
        # for char in line:
        #     new_char = char.strip("\r")
        #     blank_row.append(char)
        # print(blank_row)
    #         edited_row = row.append(char).replace(";", "0")
    # print(edited_row)

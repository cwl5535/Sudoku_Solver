with open('sudoku1.csv', newline = '') as file:
    for line in file.readlines():
        row = ''
        for char in line:
            prev_char = line[(line.index(char)-1)] 
            if (char == ";" and prev_char == ";"):
                row += ("0;")
            else: 
                row += (char + ";")

            # if (line[0] == ";") or (line[-1] == ";"): 
            #     row += ("0" + char)
            # elif (char != ';'): 
            #     row += (char + ";")
        print(row)
        # print(row)
        # for char in line:
        #     new_char = char.strip("\r")
        #     blank_row.append(char)
        # print(blank_row)
    #         edited_row = row.append(char).replace(";", "0")
    # print(edited_row)

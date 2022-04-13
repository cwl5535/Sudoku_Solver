with open('sudoku1.csv', newline = '') as file:
    for lines in file.readlines():
        line = ((lines).rstrip())
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
        print(row)
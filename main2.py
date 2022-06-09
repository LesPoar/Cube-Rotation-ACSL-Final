cube = []

rows = [[(0, 0, 0), (0, 0, 1), (0, 0, 2), (3, 0, 2), (3, 1, 2), (3, 2, 2), (5, 2, 2), (5, 2, 1), (5, 2, 0), (1, 2, 0), (1, 1, 0), (1, 0, 0)],
        [(0, 1, 0), (0, 1, 1), (0, 1, 2), (3, 0, 1), (3, 1, 1), (3, 2, 1), (5, 1, 2), (5, 1, 1), (5, 1, 0), (1, 2, 1), (1, 1, 1), (1, 0, 1)],
        [(0, 2, 0), (0, 2, 1), (0, 2, 2), (3, 0, 0), (3, 1, 0), (3, 2, 0), (5, 0, 2), (5, 0, 1), (5, 0, 0), (1, 2, 2), (1, 1, 2), (1, 0, 2)],
        [(1, 0, 0), (1, 0, 1), (1, 0, 2), (2, 0, 0), (2, 0, 1), (2, 0, 2), (3, 0, 0), (3, 0, 1), (3, 0, 2), (4, 0, 0), (4, 0, 1), (4, 0, 2)],
        [(1, 1, 0), (1, 1, 1), (1, 1, 2), (2, 1, 0), (2, 1, 1), (2, 1, 2), (3, 1, 0), (3, 1, 1), (3, 1, 2), (4, 1, 0), (4, 1, 1), (4, 1, 2)],
        [(1, 2, 0), (1, 2, 1), (1, 2, 2), (2, 2, 0), (2, 2, 1), (2, 2, 2), (3, 2, 0), (3, 2, 1), (3, 2, 2), (4, 2, 0), (4, 2, 1), (4, 2, 2)]]

cols = [[(0, 0, 0), (0, 1, 0), (0, 2, 0), (2, 0, 0), (2, 1, 0), (2, 2, 0), (5, 0, 0), (5, 1, 0), (5, 2, 0), (4, 2, 2), (4, 1, 2), (4, 0, 2)],
        [(0, 0, 1), (0, 1, 1), (0, 2, 1), (2, 0, 1), (2, 1, 1), (2, 2, 1), (5, 0, 1), (5, 1, 1), (5, 2, 1), (4, 2, 1), (4, 1, 1), (4, 0, 1)],
        [(0, 0, 2), (0, 1, 2), (0, 2, 2), (2, 0, 2), (2, 1, 2), (2, 2, 2), (5, 0, 2), (5, 1, 2), (5, 2, 2), (4, 2, 0), (4, 1, 0), (4, 0, 0)],
        [(3, 0, 0), (3, 1, 0), (3, 2, 0), (5, 0, 2), (5, 0, 1), (5, 0, 0), (1, 2, 2), (1, 1, 2), (1, 0, 2), (0, 2, 0), (0, 2, 1), (0, 2, 2)],
        [(3, 0, 1), (3, 1, 1), (3, 2, 1), (5, 1, 2), (5, 1, 1), (5, 1, 0), (1, 2, 1), (1, 1, 1), (1, 0, 1), (0, 1, 0), (0, 1, 1), (0, 1, 2)],
        [(3, 0, 2), (3, 1, 2), (3, 2, 2), (5, 2, 2), (5, 2, 1), (5, 2, 0), (1, 2, 0), (1, 1, 0), (1, 0, 0), (0, 0, 0), (0, 0, 1), (0, 0, 2)]]


def reset_cube():
    global cube

    cube = [[["O0", "O1", "O2"], ["O3", "O4", "O5"], ["O6", "O7", "O8"]],
            [["B0", "B1", "B2"], ["B3", "B4", "B5"], ["B6", "B7", "B8"]],
            [["R0", "R1", "R2"], ["R3", "R4", "R5"], ["R6", "R7", "R8"]],
            [["G0", "G1", "G2"], ["G3", "G4", "G5"], ["G6", "G7", "G8"]],
            [["Y0", "Y1", "Y2"], ["Y3", "Y4", "Y5"], ["Y6", "Y7", "Y8"]],
            [["P0", "P1", "P2"], ["P3", "P4", "P5"], ["P6", "P7", "P8"]]]


def find_focus(focus):
    for color in range(0, 6):
        for row in range(0, 3):
            for col in range(0, 3):
                if focus == cube[color][row][col]:
                    return color, row, col


def rotate_cube(focus, row, clockwise, n):
    if row:  # If row
        row_index = None

        # Find index of row from rows list
        if focus[0] == 0 or focus[0] == 5:
            for r in rows[0:3]:
                if focus in r:
                    row_index = (rows.index(r), r.index(focus))
        else:
            for r in rows[3:6]:
                if focus in r:
                    row_index = (rows.index(r), r.index(focus))

        # Append elements in the row of the focus to a temporary list
        tmp = []
        for i in range(0, len(rows[row_index[0]])):
            pos = rows[row_index[0]][i]
            tmp.append(cube[pos[0]][pos[1]][pos[2]])

        # Shift elements in the row of the focus n times left if clockwise, right if counter-clockwise
        for i in range(0, len(rows[row_index[0]])):
            pos = rows[row_index[0]][i]
            cube[pos[0]][pos[1]][pos[2]] = tmp[(i + (-1)**((clockwise+1)+(focus[0] == 5))*n) % len(tmp)]

    else:  # If column
        col_index = None

        # Find index of column from cols list
        if focus[0] == 0 or focus[0] == 2 or focus[0] == 4 or focus[0] == 5:
            for c in cols[0:3]:
                if focus in c:
                    col_index = (cols.index(c), c.index(focus))
        else:
            for c in cols[3:6]:
                if focus in c:
                    col_index = (cols.index(c), c.index(focus))

        # Append elements in the column of the focus to a temporary list
        tmp = []
        for i in range(0, len(cols[col_index[0]])):
            pos = cols[col_index[0]][i]
            tmp.append(cube[pos[0]][pos[1]][pos[2]])

        # Shift elements in the column of the focus n times left if clockwise, right if counter-clockwise
        for i in range(0, len(cols[col_index[0]])):
            pos = cols[col_index[0]][i]
            cube[pos[0]][pos[1]][pos[2]] = tmp[(i + (-1)**((clockwise+1)+(focus[0] == 1 or focus[0] == 4))*n) % len(tmp)]


if __name__ == "__main__":
    inputs = "O8 CC2\nP3 CR4\nG0 RR3\nB6 RC1\nR5 RC1 CR2\nR8 CR4 RC3\nY5 RC1 CR1 RR1 CC1\nB6 CR3 CC4 RC1 RR2\nP4 RR0 CC0 RC7 CR9\nY2 CR1 RC2 CR3 RC4 CC5 RC6 CR7 RC8 CR9".split("\n")

    for line in inputs:
        reset_cube()
        line = line.split()
        focus_point = line[0]
        for rotation in line[1:]:
            focus_pos = find_focus(focus_point)
            rotate_cube(focus_pos, rotation[0] == "R", rotation[1] == "C", int(rotation[2]))

        # Print the face of the cube with the focus point
        new_focus_pos = find_focus(focus_point)
        for cube_row in cube[new_focus_pos[0]]:
            for cube_col in cube_row:
                print(cube_col, end="")
        print()

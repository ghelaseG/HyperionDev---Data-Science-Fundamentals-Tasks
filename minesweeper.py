"""
Create a function that takes a grid of # and -, where each hash (#) represents a
mine and each dash (-) represents a mine-free spot.
Return a grid, where each dash is replaced by a digit, indicating the number of
mines immediately adjacent to the spot i.e. (horizontally, vertically, and
diagonally)
"""

import random

# we first create a function to access the grid example from the task
def create_grid_example(): # taking no arguments

    example_grid = [ 
        ["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"] ]
    
    return example_grid

print('This is the grid example from our task. \n')
[print(row) for row in create_grid_example()] # print our grid example using list comprehension
print(' ')

# now we create a function where the user is able to create a random grid, by inserting the number of rows, columns and mines
def create_random_grid(rows, columns, mines):

    total_cells = rows * columns # here we calculate the total nr of cells to determine the range of position of each cell
    
    # we make use of this method to randomly choose the mines position
    mine_positions = random.sample(range(total_cells), mines) 

    new_grid = [] # we create our new empty list to store everything afterwards

    # we iterate over each row and column using for loop
    for i in range(rows):

        row = []  # create a new row to store our "#" or "-"
        
        for j in range(columns):
            # now let's check the index position if it matches and if we should add our mines or not
            if i * columns + j in mine_positions:
                row.append('#')  # if True add at that index position the "#"
            else:
                row.append('-')  

        new_grid.append(row)  # add the row to the new grid/empty list

    return new_grid

# here we create a function that counts and replace the number of adjacent mines for each empty ('-') cell in our grid
def replace_dash_with_digit(grid):

    nr_rows = len(grid) 
    nr_columns = len(grid[0])
    empty_grid = [['#'] * nr_columns for _ in range(nr_rows)] # we create a 2d array with same dimensions as the original

    # here we make use of the example from our task to make our program easier, where for exp(NW position = current_row - 1, current_col - 1 = (-1,-1))
    adjacent_indexes = [(-1, -1), (-1, 0), (-1, 1),
                        (0, -1),           (0, 1),
                        (1, -1),  (1, 0),  (1, 1)]

    # in the following for loops we iterate over each row and column in the grid
    for index_row, row in enumerate(grid):
        for index_column, column in enumerate(row):
            if column == '-':  # if the current cell is empty we start the count of our digits
                count = 0
                # in this for loop we iterate through each adjacent position using our example above and then we calculate the digits
                for adj_row, adj_column in adjacent_indexes:
                    adj_row_index = index_row + adj_row
                    adj_col_index = index_column + adj_column

                    # we use this if statement to check if on the edges of the grid we go out of bounds
                    if 0 <= adj_row_index < len(grid) and 0 <= adj_col_index < len(row):
                        # and if the adjacent position contains a mine
                        if grid[adj_row_index][adj_col_index] == '#':
                            count += 1  # we increase the count of adjacent mines each time it runs

                empty_grid[index_row][index_column] = str(count) # here we fill in our empty grid

    return empty_grid

# now we can check if we can get the same output for the grid example
print(' ')
print('The result for our replaced grid with digits from our task is: \n')
[print(row) for row in replace_dash_with_digit(create_grid_example())]

# for our random grid, let's first ask the user for the input
print(' ')
print("It's time to create our grid.")
rowsR = int(input('Please enter the number of rows for your random grid: '))
columnsR = int(input('Please enter the number of columns for your random grid: '))
minesR = int(input('Please insert a random number of mines for your grid: '))
print(' ')
print(f'You chose a grid with {rowsR} rows, {columnsR} columns and to randomly place a number of {minesR} mines inside.')
print('This is your random grid created without the empty cell replaced: \n')

# now let's test our random grid and see how it goes
rand_grid = create_random_grid(rowsR, columnsR, minesR) # we make sure we write the arguments in the same order
[print(row) for row in rand_grid]
print(' ')
result_count_grid = replace_dash_with_digit(rand_grid)
print('The result for our replaced grid with digits lying next or near our randomly placed mines is: \n')
[print(row) for row in result_count_grid] # print using list comprehension




def select_sections(occupancy_probability):
    """
    Approach Description:
    Will be explaining my approach base on steps of my implementation. Started of by creating
    a table with the same amount of elements needed for occupancy_probability. Since I'm using
    a bottom to top approach by iterating through each row and column of the table and finding
    the mimnimum sum of the elements on the array below it and the elements below to the right
    and to the left of it. Thus making the last row of the table with be filled with elements
    from the last row, before beginning with our operation and perform each iteration towards
    the last array on the top.

    The calcuation before performing backtracking, based on the test case above:
    table = [[183, 168, 200, 140, 118],
            [155, 152, 114, 106, 177],
            [129, 164, 127, 90, 159],
            [133, 90, 137, 77, 108],
            [91, 104, 70, 56, 98],
            [61, 82, 93, 51, 81],
            [24, 25, 23, 66, 68],
            [22, 38, 9, 19, 99]]

    Once it has reach the top, a backtracking algorithm has been implemented to find the optimal
    path through a table of occupancy probabilities. After finding the index of the minimum value
    in the first row of the table. We can apply a similar approach as we did above. For each row
    in the table, it checks for the current element having a lower value by comparing it's current
    position "below", left, and right then decrementing the column index. Lastly, the current row
    and column index will be appended to the "results" list along with the minimum value of the
    array at the top.

    Input:
        occupancy_probability: An array of occupancy probabilities.
    Output:
        the minimum value of the array at the top and the index of the row and column.
    Time Complexity:
        O(nm) where n is the number of rows and m is the number of columns/ aisles in
        the occupancy_probability.
    Aux Space Complexity:
        O(nm) where n is the number of rows and m is the number of columns/ aisles in
        the occupancy_probability.
    """
    # number of rows
    rows_num = len(occupancy_probability)
    # number of aisles/columns
    columns_num = len(occupancy_probability[0])

    # create an array with all elements of the arrays within initialized to 0
    table = []
    for row in range(rows_num):
        table.append([0 for column in range(columns_num)])

    # fill in the last row of table with the elements obtained from occupancy_probability
    table[-1] = occupancy_probability[-1]

    # calculation for table, starting from bottom to top
    for row in range(rows_num - 2, -1,- 1):
        for column in range(columns_num):
            # the element directly below
            element = [table[row + 1][column]]
            if column > 0:
                # the element below and to the left
                element.append(table[row + 1][column - 1])
            if column < columns_num - 1:
                # the element below and to the right
                element.append(table[row + 1][column + 1])
            table[row][column] = occupancy_probability[row][column] + min(element)

    # backtracking from top to bottom, after finding the minimum
    results = []
    column = table[0].index(min(table[0]))
    for row in range(0, rows_num):
        left = False
        right = False

        # checking if there is a column to the left of the current element and if
        # the value of that element is less than the value of the current element.
        if column > 0 and table [row][column-1] < table[row][column]:
            left = True

        # checking if there is a column to the right of the current element and
        # if the value of that element is less than the value of the current element.
        # If both true, append value of the element to list.
        if column < columns_num-1 and table[row][column+1] < table[row][column]:
            right = True

        if left == True and right == True:
            if table[row][column-1] < table[row][column+1]:
                right = False
            else:
                left = False
        if left:
            column -= 1

        elif right:
            column += 1

        results.append((row, column))

    return [min(table[0]),results]
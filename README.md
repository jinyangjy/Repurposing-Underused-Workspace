# Repurposing-Underused-Workspace
Utilising concepts of Dynamic Programming

A large technology company wants to install a new high-performance computing (HPC) facility in their building. They don't have any empty space, so they need to use some of the underused office space. The office space is arranged in a rectangular grid with m aisles and n rows. The HPC facility needs an area of n connected sections, which means that one section will need to be removed from each row. This will leave one empty aisle after the remaining sections are shuffled around. The company knows the occupancy probability for each section, which is a number between 0 and 100 that represents the percent of working hours the section is usually occupied.

The company wants to find the n sections with the lowest total occupancy rate. To do this, they can use a matrix of n rows and m aisles/columns, P[0...n-1][0...m-1], which contains the occupancy probability values for a total of n*m sections. The task is to simply identify the list of locations (i, j) for n sections which has the lowest total occupancy rate.

The input, occupancy_probability is a list of lists. There are n interior lists. All interior lists are length m (columns/aisles). Each interior list represents a different row of sections. Occupancy_probability[i][j] is an integer number between 0 and 100 (inclusive) which represents the occupancy probability for a section located at row i and column/ aisle j. The algorithm returns a list of 2 items
  - minimum_total_occupancy, which is an integer, representing the total occupancy for the selected n sections to be removed
  - sections_location, whihc is a list of n tuples in the form of (i, j). Each tuple represents the location of one section selected for removal.
        - i refers to the row index and can range from 0 to n-1.
        - j refers to the column index and can range from 0 to m-1.

Here's an example input 
- occupancy_probability = [31, 54, 94, 34, 12],
                        [26, 25, 24, 16, 87],
                        [39, 74, 50, 13, 82],
                        [42, 20, 81, 21, 52],
                        [30, 43, 19, 5, 47],
                        [37, 59, 70, 28, 15],
                        [ 2, 16, 14, 57, 49],
                        [22, 38, 9, 19, 99]]

My approach base on steps of my implementation. Started of by creating a table with the same amount of elements needed for occupancy_probability. Since I'm using a bottom to top approach by iterating through each row and column of the table and finding the mimnimum sum of the elements on the array below it and the elements below to the right and to the left of it. Thus making the last row of the table with be filled with elements from the last row, before beginning with our operation and perform each iteration towards the last array on the top.

The calcuation before performing backtracking, based on the test case above:
  -  table = [[183, 168, 200, 140, 118],
            [155, 152, 114, 106, 177],
            [129, 164, 127, 90, 159],
            [133, 90, 137, 77, 108],
            [91, 104, 70, 56, 98],
            [61, 82, 93, 51, 81],
            [24, 25, 23, 66, 68],
            [22, 38, 9, 19, 99]]

Once it has reach the top, a backtracking algorithm has been implemented to find the optimal path through a table of occupancy probabilities. After finding the index of the minimum value in the first row of the table. We can apply a similar approach as we did above. For each row in the table, it checks for the current element having a lower value by comparing it's current position "below", left, and right then decrementing the column index. Lastly, the current row and column index will be appended to the "results" list along with the minimum value of the array at the top.


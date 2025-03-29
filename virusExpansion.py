"""  Virus Expansion
You are given a mxn grid where each cell can have one of three values:
0 - Representing an empty cell
1 - Representing a healthy person
2 - Representing a sick person

Any healthy person who is 4-directionally adjacent to a sick person become sick every minute.
Return TRUE if all people get sick (not healthy people on the grid).
Return FALSE otherwise (if there is at least someone who was not infected).
"""


# Approach:
# Use a BFS algorithm to expand the virus and queue to store the position of sick people
# Identify the position of the sick people
# Verify ig there are remaining healthy persons
from collections import deque
def virusExpansion(grid):
    if not grid or not grid[0]:
        return True     # Empty grid - No healthy people - Return True

    # Determine the dimensions of the grid
    rows, cols = len(grid), len(grid[0])
    healthy_count = 0
    sick_positions = deque()

    # Retrieve the coordinates of the sick people and amount of healthy people
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:                     # If is a sick person
                sick_positions.append((row, col))       # Store its coordinate
            elif grid[row][col] == 1:                   # If is a healthy person
                healthy_count += 1                      # Update counter

    # Check if there aren't healthy people
    if healthy_count == 0:
        return True             # All the coordinates on the grid are empty cells or sick people

    # Define the directions to move across the grid
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Propagate the virus
    while sick_positions:
        row, col = sick_positions.popleft()
        # Check the 4-directional adjacent person to the infected person and infected if needed
        for dir_row, dir_col in directions:
            new_row, new_col = row+dir_row, col+dir_col
            # Make sure that the coordinates are inside the grid side, if its true check if is a healthy person
            if 0 <= new_row < rows and 0 <= new_col < col and grid[new_row][new_col] == 1:
                # Infect the person
                grid[new_row][new_col] = 2
                # Update counter
                healthy_count -= 1
                # Add the position to the list of coordinates
                sick_positions.append((new_row, new_col))
    if healthy_count == 0:
        return True
    else:
        print(healthy_count)
        return False

    return  healthy_count == 0  # Check if there are remaining healhty persons

grid_1 = [
    [0, 1, 2],
    [0, 1, 1],
    [1, 0, 1]
]

grid_2 = [
    [0, 1, 2],
    [0, 1, 1],
    [2, 0, 2]
]

print(virusExpansion(grid_1))

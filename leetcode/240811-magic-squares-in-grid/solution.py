def is_magic_square(grid, row, col):
    nums = []
    for i in range(3):
        for j in range(3):
            nums.append(grid[row + i][col + j])
    
    if sorted(nums) != list(range(1, 10)):
        return False
    
    s = grid[row][col] + grid[row][col + 1] + grid[row][col + 2] 
    
    return (
        grid[row][col] + grid[row][col + 1] + grid[row][col + 2] == s and
        grid[row + 1][col] + grid[row + 1][col + 1] + grid[row + 1][col + 2] == s and
        grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2] == s and
 
        grid[row][col] + grid[row + 1][col] + grid[row + 2][col] == s and
        grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1] == s and
        grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2] == s and
     
        grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2] == s and
        grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col] == s
    )


def num_magic_squares(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    for i in range(rows - 2):
        for j in range(cols - 2):
            if is_magic_square(grid, i, j):
                count += 1
    
    return count
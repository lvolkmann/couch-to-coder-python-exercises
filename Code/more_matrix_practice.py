def initialize_grid(length, width):
	lst = []
	for row in range(length):
		row_build = []
		for col in range(width):
			row_build.append(0)
		lst.append(row_build)
	return lst

def print_grid(grid):
    for row in grid:
        print(row)

def initialize_item(grid,x,y):
    grid[y][x] = 1

def check_below(grid,x,y):
    """Return True if space available below coord and False otherwise"""
    if (y + 1) >= len(grid):
        return False
    elif grid[y+1][x] == 0:
        return True
    else:
        return False

def fall(grid, x, y):
    if check_below(grid,x,y):
        temp = grid[y+1][x]
        grid[y+1][x] = grid[y][x]
        grid[y][x] = 0

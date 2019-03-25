def initialize_grid(length, width):
	lst = []
	for row in range(length):
		row_build = []
		for col in range(width):
			row_build.append(0)
		lst.append(row_build)
	return lst

def is_in(x, lst):
	for row in lst:
		if x in row:
			return True
	return False

def create_col(col_num,lst, value):
	for row in lst:
		row[col_num] =  value

def create_row(row_num,lst, value):
        for col in range(len(lst)):
                lst[row_num][col] = value
	

def move_col(col_num, direction, lst):
	if direction > 0:
		for row in lst:
			temp = row[col_num + 1]
			row[col_num + 1] = row[col_num]
			row[col_num] = temp
	elif direction < 0:
			temp = row[col_num - 1]
			row[col_num - 1] = row[col_num]
			row[col_num] = temp


def move_row(row_num, direction, lst):
	if direction < 0:
		temp = lst[row_num + 1]
		lst[row_num + 1] = lst[row_num]
		lst[row_num] = temp
	elif direction > 0:
		temp = lst[row_num - 1]
		lst[row_num - 1] = lst[row_num]
		lst[row_num] = temp

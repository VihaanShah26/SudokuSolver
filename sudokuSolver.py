class variables:
	counter=0

# function to check whether a particular assignment obeys the constraints 
def can_yx_be_z(sudoku, y, x, z):
	for i in range(9):
		if (sudoku[y][i]==z):
			return False
		if (sudoku[i][x]==z):
			return False
		if(sudoku[int(y/3)*3+int(i/3)][int(x/3)*3+i%3]==z): 
			return False
	return True

# function to solve the board using back tracking 
def sudoku_backtracking(sudoku):
	variables.counter = 0

	def BT(sudoku):
		variables.counter = variables.counter + 1

		if check_complete(sudoku): 
			return True
		else:
			for y in range(9):
				for x in range(9):
					if sudoku[y][x] == 0:
						for i in range(9):
							if can_yx_be_z(sudoku, y, x, i+1):
								sudoku[y][x] = i+1
								R = BT(sudoku)
								if R: 
									return True
								else: 
									sudoku[y][x] = 0
						return False
					
	BT(sudoku)

	return variables.counter

# function to solve the board using forward checking 
def sudoku_forwardchecking(sudoku):
	variables.counter = 0
	
	# domain = [[[i+1 for i in range(9) if can_yx_be_z(sudoku, k, j, i+1)] for j in range(9)] for k in range(9)]
	domain = [[[i+1 for i in range(9)] for j in range(9)] for k in range(9)]

	for y in range(9):
		for x in range(9):
			value = sudoku[y][x]
			if not value == 0:
				D = update_domain(domain, x, y, sudoku[y][x], sudoku)

	def FC(sudoku, domain):
		variables.counter += 1

		if check_complete(sudoku):
			return True
		
		else:
			for y in range(9):
				for x in range(9):
					if sudoku[y][x] == 0:
						for value in range(9):
							if can_yx_be_z(sudoku, y, x, value+1):
								old_domain = copy_domain(domain)
								sudoku[y][x] = value+1
								D = update_domain(domain, x, y, value+1, sudoku)
								if D:
									R = FC(sudoku, domain)
									if R: return True
								sudoku[y][x] = 0
								domain = copy_domain(old_domain)
						return False
		# helper function ends 

	FC(sudoku, domain)
	return variables.counter

def check_complete(board):
	for i in range(9):
		for j in range(9):
			if board[i][j] == 0: return False
	return True

def copy_domain(domain):
	new_domain = [[[domain[k][j][i] for i in range(len(domain[k][j]))] for j in range(9)] for k in range(9)]
	return new_domain

def update_domain(domain, x, y, value, sudoku):
	for i in range(9):
		if sudoku[i][x] == 0:
			if value in domain[i][x]: domain[i][x].remove(value)
		if sudoku[y][i] == 0:
			if value in domain[y][i]: domain[y][i].remove(value)
		if sudoku[int(y/3)*3+int(i/3)][int(x/3)*3+i%3] == 0:
			if value in domain[int(y/3)*3+int(i/3)][int(x/3)*3+i%3]: domain[int(y/3)*3+int(i/3)][int(x/3)*3+i%3].remove(value)

	for j in range(9):
		for i in range(9):
				if domain[j][i] == [] and sudoku[j][i] == 0: 
					return False
	return True


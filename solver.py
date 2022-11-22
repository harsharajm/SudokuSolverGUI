def find(b):
	for i in range(9):
		for j in range(9):
			if b[i][j]==0:
				return i,j
	return False

def valid(b, r, c, n):
	for i in range(9):
		if b[r][i]==n or b[i][c]==n :
			return False

	x = r//3*3
	y = c//3*3
		
	for k in range(x,x+3):
		for l in range(y,y+3):
			if b[k][l]==n:
				return False
	return True

def solve(b):
	if not find(b):
		return True
	else:
		r,c = find(b)
	for i in range(1,10):
		if valid(b,r,c,i):
			b[r][c] = i
			if solve(b):
				return True
			
			
			b[r][c]=0
	return False
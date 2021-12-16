TEST_INPUT = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

MOVES = [[1,1], [1,-1], [-1, 1], [-1,-1], [1,0], [0,1], [-1, 0], [0, -1]]


def reset(0):
	for y in range(y_bounds):
		for x in range(x_bounds):

def flash():
	y_bounds = len(input)
	x_bounds = len(input[0])
	flash_count = 0
	
	def _update(y, x, input):
		input[y][x] += input[y][x]
		if input[y][x] > 8:
			flash_count += 1
			for move in moves:
				x2, y2 = move
				next_y = y + y2
				next_x = x + x2
				if next_y >= y_bounds or next_y < 0:
					continue
				if next_x >= x_bounds or next_x < 0:
					continue

	for y in (y_bounds):
			for x in range(x_bounds):
				_update(y, x, input)
				reset(input)
	

def part1(input, steps=100):
	
	for _ in range(steps):
		flash(input)

def main():
	input = TEST_INPUT.splitlines()
	part1(input)
	
	
if __name__ == "__main__":
	main()

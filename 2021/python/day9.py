TEST_INPUT = """2199943210
3987894921
9856789892
8767896789
9899965678"""

def get_low_coords(input):
	movements = [[-1,0], [1,0], [0,1], [0,-1]]
	low_coords = [] 
	for y in range(len(input)):
		for x in range(len(input[0])):
			curr = input[y][x]
			print(x, y)
			adjacent = []
			for movement in movements:
				j, k = movement
				next_y, next_x = y+j, x+k
				if next_y in [-1, len(input)] or next_x in [-1, len(input[0])]:
					continue;
				adjacent.append([next_y, next_x])
			if all([input[b][a] > curr for b,a in adjacent]):
				low_coords += [x, y],
	return low_coords
	

def part1(input):	
	low_coords = get_low_coords(input)
	print(low_coords)
	return(sum([int(input[y][x]) + 1 for x,y in low_coords]))
	
def find_basin(coord, input):
	basin = []
	q = [coord]
	visited = [[False] * len(input[0]) for _ in range(len(input))]
	movements = [[-1,0], [1,0], [0,1], [0,-1]]
	while q:
		x, y = q[0]
		basin += q[0],
		q = q[1:]
		curr = input[y][x]
		for movement in movements:
			j, k = movement
			next_y, next_x = y+j, x+k
			if next_y in [-1, len(input)] or next_x in [-1, len(input[0])]:
				continue
			if visited[next_y][next_x] or curr > input[next_y][next_x] or int(input[next_y][next_x]) > 8:
				continue;
			q.append([next_x, next_y])
			visited[next_y][next_x] = True
	return basin
		
def part2(input):
	low_coords = get_low_coords(input)
	print(low_coords)
	sizes = []
	basins = []
	for low in low_coords:
		basins += find_basin(low, input),
	sizes = sorted([len(basin) for basin in basins], reverse=True)[:3]
	total = 1
	for size in sizes:
		total *= size
	return total
 		#print(sum([int(input[y][x]) for x, y in basin]))

def main():
	with open("../data/day9.txt", "r") as f:
		input = f.read().splitlines()
		#print(part1(TEST_INPUT.splitlines()))
		print(part2(input))

if __name__ == "__main__":
	main()

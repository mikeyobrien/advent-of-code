TEST_INPUT = """2199943210
3987894921
9856789892
8767896789
9899965678"""

def part1(input):
	movements = [[-1,0], [1,0], [0,1], [0,-1]]
	low_points = []
	for y in range(len(input)):
		for x in range(len(input[0])):
			curr = input[y][x]
			adjacent = []
			for movement in movements:
				j, k = movement
				next_y, next_x = y+j, x+k
				print(next_y, next_x)
				if next_y in [-1, len(input)] or next_x in [-1, len(input[0])]:
					continue;
				adjacent.append(input[next_y][next_x])
			if all([a > curr for a in adjacent]):
				low_points.append(curr)
	return(sum([int(p) + 1 for p in low_points]))

def main():
	with open("../data/day9.txt", "r") as f:
		print(part1(f.read().splitlines()))

if __name__ == "__main__":
	main()

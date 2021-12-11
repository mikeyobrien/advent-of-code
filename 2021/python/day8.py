TEST_INPUT = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

def part1(input):
	""" unique  """
	unique = [2, 3, 4, 7]
	total_unique = 0
	for line in input:
		signal, outputs = line.split("|")
		outputs = outputs.lstrip()
		signal = outputs.rstrip()
		for output in outputs.split(" "):
			if len(output) in unique:
				total_unique += 1
	return total_unique
	
	
def get_unique(signals):
	shared = []
	unique = {}
	for signal in signals:
		if len(signal) == 2:
			unique[1] = set(signal)
		elif len(signal) == 3:
			unique[7] = set(signal)
		elif len(signal) == 4:
			unique[4] = set(signal)
		elif len(signal) == 7:
			unique[8] = set(signal)		
		else:
			shared += signal,
	return unique, shared
	
	
def deduce(signals, unique):
	"""
	5: 2,3,5
	6: 0,6,9
	"""
	mappings = {}
	for signal in signals:
		s = set(signal)
		if len(signal) == 5:
			if unique[1].issubset(s):
				mappings[3] = s
			elif len(unique[4] - s) == 1:
				mappings[5] = s
			else:
				mappings[2] = s
		if len(signal) == 6:
			if unique[4].issubset(s):
				mappings[9] = s
			elif len(unique[1] - s) == 0:
				mappings[0] = s
			else:
				mappings[6] = s
	return {**mappings, **unique}
	
def part2(input):
	results = []
	for line in input:
		signals, outputs = line.split("|")
		signals = signals.rstrip().split(" ")
		outputs = outputs.lstrip().split(" ")
		unique_mappings, shared = get_unique(signals)
		mappings = deduce(shared, unique_mappings)
		for k,v in mappings.items():
			mappings[k] = "".join(v)
		if len(mappings) != 10:
			raise RuntimeError()
		n = []
		for output in outputs:
			n += [str(k) for k, v in mappings.items() if set(v) == set(output)][0],
		results.append("".join(n))
	return sum([int(r) for r in results])
		

def main():
	input = TEST_INPUT.splitlines()
	with open("../data/day8.txt", "r") as f:
		input = f.read().splitlines()
		print(part1(input))
		print(part2(input))


if __name__ == "__main__":
	main()




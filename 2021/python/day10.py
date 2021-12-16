TEST_INPUT = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

PAIRS = {
 	"}": "{", 
 	"]": "[",
 	">": "<",
 	")": "("
}

SCORES = {
 ")": 3,
 "]": 57,
 "}": 1197,
 ">": 25137,
}

def part1(input):
	sum = 0
	for line in input:
		stack = []
		for char in line:
			if char in PAIRS.values():
				stack.append(char)
				continue
			if stack[-1] != PAIRS[char]:
				print("Expected:", stack[-1], "Got:", char)
				sum += SCORES[char]
			stack.pop()
	return sum
				

def main():
	input = TEST_INPUT.splitlines()
	print(part1(input))
	
main()

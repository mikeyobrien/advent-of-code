def part1(input):
    return sum([1 for i, line in enumerate(input[1:], start=1) if line > input[i - 1]])


def part2(input, step):
    cnt = 0
    windows = [input[i - step : i] for i in range(step - 1, len(input))]
    for i, window in enumerate(windows[1:], start=1):
        print(sum(window), sum(windows[i - 1]))
        if sum(window) > sum(windows[i - 1]):
            cnt += 1
    return cnt


def main():
    with open("../data/day1.txt") as f:
        lines = [int(line) for line in f.read().splitlines()]
        print("part1", part1(lines))
        print("part2", part2(lines, 3))


if __name__ == "__main__":
    main()

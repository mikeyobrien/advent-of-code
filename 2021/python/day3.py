from dataclasses import dataclass


@dataclass
class Counter:
    zeros: int = 0
    ones: int = 0

    def common(self):
        return 0 if self.zeros > self.ones else 1

    def least_common(self):
        return 1 if self.zeros > self.ones else 0


def to_decimal(string):
    res = 0
    for i, bit in enumerate(string[::-1]):
        if int(bit) == 1:
            res = res + pow(2,i)
    return res

def part1(input):
    counts = [Counter() for i in range(len(input[0]))]
    for report in input:
        for i, bit in enumerate(report):
            if bit == "0":
                counts[i].zeros += 1
            elif bit == "1":
                counts[i].ones += 1
            else:
                raise ValueError()
    gamma = "".join([str(count.common()) for count in counts])
    epsilon = "".join([str(count.least_common()) for count in counts])
    gamma_rate = to_decimal(gamma)
    epsilon_rate = to_decimal(epsilon)
    return gamma_rate * epsilon_rate


def find_rating(reports, rating_type,index):
    if len(reports) == 1:
        return to_decimal(reports[0])
    counts = [Counter() for i in range(len(reports[0]))]
    for report in reports:
        for i, bit in enumerate(report):
            if bit == "0":
                counts[i].zeros += 1
            elif bit == "1":
                counts[i].ones += 1
            else:
                raise ValueError()
    gamma = "".join([str(count.common()) for count in counts])
    if "oxygen" == rating_type:
        return find_rating([report for report in reports if report[index] == gamma[index]], rating_type, index + 1)
    return find_rating([report for report in reports if report[index] != gamma[index]], rating_type, index + 1)


def part2(input):
    oxygen = find_rating(input, "oxygen", 0)
    co2 = find_rating(input, "co2", 0)
    print(oxygen * co2)


def main():
    with open("../data/day3.txt", "r") as f:
        lines = f.read().splitlines()
        print(part1(lines))
        print(part2(lines))

if __name__ == '__main__':
    main()

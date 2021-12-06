from dataclasses import dataclass


@dataclass
class Coordinates:
    position: int = 0
    depth: int = 0
    aim: int = 0  # part 2


def part1(input):
    coords = Coordinates()
    for direction in input:
        direction, distance = direction.split(" ")
        distance = int(distance)
        print(direction, distance)
        if direction == "forward":
            coords.position += distance
        elif direction == "up":
            coords.depth += distance
        elif direction == "down":
            coords.depth -= distance
        else:
            raise ValueError("unexpected")
    print(coords)
    return abs(coords.depth * coords.position)


def part2(input):
    coords = Coordinates()
    for direction in input:
        direction, distance = direction.split(" ")
        distance = int(distance)
        print(direction, distance)
        if direction == "forward":
            coords.position += distance
            coords.depth += coords.aim * distance
        elif direction == "up":
            coords.aim -= distance
        elif direction == "down":
            coords.aim += distance
        else:
            raise ValueError("unexpected")
    print(coords)
    return abs(coords.depth * coords.position)


def main():
    with open("../data/day2.txt", "r") as f:
        lines = f.read().splitlines()
        print(part1(lines))
        print(part2(lines))


if __name__ == "__main__":
    main()

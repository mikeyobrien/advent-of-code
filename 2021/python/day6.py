TEST_INPUT = "3,4,3,1,2"
PUZZLE_INPUT = "1,1,1,2,1,1,2,1,1,1,5,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,4,1,1,1,1,3,1,1,3,1,1,1,4,1,5,1,3,1,1,1,1,1,5,1,1,1,1,1,5,5,2,5,1,1,2,1,1,1,1,3,4,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,5,4,1,1,1,1,1,5,1,2,4,1,1,1,1,1,3,3,2,1,1,4,1,1,5,5,1,1,1,1,1,2,5,1,4,1,1,1,1,1,1,2,1,1,5,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,3,1,1,3,1,3,1,4,1,5,4,1,1,2,1,1,5,1,1,1,1,1,5,1,1,1,1,1,1,1,1,1,4,1,1,4,1,1,1,1,1,1,1,5,4,1,2,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,4,1,1,1,2,1,4,1,1,1,1,1,1,1,1,1,4,2,1,2,1,1,4,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,3,2,1,4,1,5,1,1,1,4,5,1,1,1,1,1,1,5,1,1,5,1,2,1,1,2,4,1,1,2,1,5,5,3"


def simulate_lanternfish(input, days=256):
    timer_state = [0] * 9
    for time in input:
        timer_state[time] += 1
    print(timer_state)
    for i in range(days):
        new_state = [0] * 9
        for i, time in enumerate(timer_state[1:], start=1):
            to_add = timer_state[0]
            new_state[i - 1] = time
        new_state[6] += to_add
        new_state[8] += to_add
        timer_state = new_state
    return sum(timer_state)


def main():
    input = [int(i) for i in PUZZLE_INPUT.split(",")]
    print(simulate_lanternfish(input, days=80))
    print(simulate_lanternfish(input, days=256))  # part2


if __name__ == "__main__":
    main()

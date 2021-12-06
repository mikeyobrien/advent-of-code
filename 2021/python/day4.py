from collections import namedtuple

TEST_INPUT = [
    line.rstrip("\n")
    for line in """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
""".split(
        "\n\n"
    )
]

Mark = namedtuple("Mark", "x y")


class Bingo:
    def __init__(self, board):
        self.board = [row.split() for row in board.splitlines()]

    def __repr__(self):
        return "\n".join([" ".join(row) for row in self.board])

    @property
    def row_length(self):
        return len(self.board)

    @property
    def col_length(self):
        return len(self.board[0])

    def mark(self, number):
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                if self.board[x][y] == number:
                    self.board[x][y] = "x"

    def has_won(self):
        for row in self.board:
            has_row = all([pos == "x" for pos in row])
            if has_row:
                break
        for y in range(self.col_length):
            has_col = all([self.board[x][y] == "x" for x in range(self.row_length)])
            if has_col:
                break
        return has_row or has_col

    def score(self, number):
        unmarked = []
        for x in range(self.row_length):
            for y in range(self.col_length):
                if self.board[x][y] != "x":
                    unmarked.append(int(self.board[x][y]))
        return sum(unmarked) * int(number)


def part1(input):
    numbers = input[0].split(",")
    boards = [Bingo(board) for board in input[1:]]

    for number in numbers:
        print(number)
        for board in boards:
            board.mark(number)
            if board.has_won():
                print(boards)
                return board.score(number)
    return 0


def part2(input):
    numbers = input[0].split(",")
    boards = [Bingo(board) for board in input[1:]]
    winning_boards = [False] * len(boards)
    for number in numbers:
        print(number)
        for i, board in enumerate(boards):
            board.mark(number)
            if board.has_won():
                winning_boards[i] = True
            if all(winning_boards):
                return board.score(number)
        print(winning_boards)


def main():
    with open("../data/day4.txt", "r") as f:
        input = [line.rstrip("\n") for line in f.read().split("\n\n")]
        # print(part1(input))
        print(part2(input))


if __name__ == "__main__":
    main()

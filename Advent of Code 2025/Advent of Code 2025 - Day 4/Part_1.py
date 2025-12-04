INPUT = r"Advent of Code 2025\Advent of Code 2025 - Day 4\input.txt"
TEST_INPUT = r"Advent of Code 2025\Advent of Code 2025 - Day 4\test_input.txt"

PAPER = "@"
MAX_ADJACENT = 3

def main():
    with open(INPUT, "r", encoding="utf-8") as file:
        input = [f.strip("\n") for f in file.readlines()]
        grid = [[c for c in i] for i in input]

        res = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])): # assuming grid is n^2
                if grid[y][x] == PAPER and adjacent_rolls(grid, (x, y)):
                    res += 1

        print(res)


def adjacent_rolls(grid: list[list[str]], coords: tuple[int, int]) -> bool:
    found = 0
    for y in range(max(0, coords[1] - 1), min(len(grid), coords[1] + 2)):
        for x in range(max(0, coords[0] - 1), min(len(grid[y]), coords[0] + 2)):
            if coords == (x, y):
                continue

            if grid[y][x] == PAPER:
                found += 1

    return found <= MAX_ADJACENT


if __name__ == "__main__":
    main()
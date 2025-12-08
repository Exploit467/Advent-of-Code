INPUT = r"input.txt"
TEST_INPUT = r"test_input.txt"

PAPER = "@"
MARKER = "x"
MAX_ADJACENT = 3

def main():
    with open(INPUT, "r", encoding="utf-8") as file:
        input = [f.strip("\n") for f in file.readlines()]
        grid = [[c for c in i] for i in input]

        count = 0
        while True:
            grid, res = step(grid)
            count += res

            if res == 0:
                break

        print(count)

def step(grid: list[list[str]]):
    res = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == PAPER and adjacent_rolls(grid, (x, y)):
                grid[y][x] = MARKER
                res += 1

    return [[c.replace("x", ".") for c in i] for i in grid], res

def adjacent_rolls(grid: list[list[str]], coords: tuple[int, int]) -> bool:
    found = 0
    for y in range(max(0, coords[1] - 1), min(len(grid), coords[1] + 2)):
        for x in range(max(0, coords[0] - 1), min(len(grid[y]), coords[0] + 2)):
            if coords == (x, y):
                continue

            if grid[y][x] in [PAPER, MARKER]:
                found += 1

    return found <= MAX_ADJACENT


if __name__ == "__main__":
    main()
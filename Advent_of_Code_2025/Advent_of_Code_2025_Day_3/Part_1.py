INPUT = r"input.txt"
TEST_INPUT = r"test_input.txt"

DIGITS = 2

def main():
    with open(INPUT, "r") as file:
        results = []
        for line in file.readlines():
            line = line.strip("\n")

            digits = []
            t_idx = 0
            left = DIGITS - 1
            while left >= 0:
                digit, idx = find_next_highest(line, left, t_idx)
                digits.append(digit)

                left -= 1
                t_idx = idx + 1

            combined = "".join(digits)
            results.append(int(combined))

        print(sum(results))

def find_next_highest(string: str, digits_left: int, start_from: int) -> tuple[int, int]:
    for i in range(9, 0, -1):
        try:
            idx = string.index(str(i), start_from)
            if idx >= len(string) - digits_left:
                continue

            return (string[idx], idx)

        except ValueError:
            continue


if __name__ == "__main__":
    main()
INPUT = r"input.txt"
TEST_INPUT = r"test_input.txt"

START = "S"
BEAM = "|"
SPLITTER = "^"

def main():
    with open(INPUT, "r", encoding="utf-8") as file:
        lines = [f.replace("\n", "") for f in file.readlines()]

        lines, splits = calc(lines)

        fancy_print(lines, splits)

# Seperate function as it is also used in Part_2.py
def calc(lines: str) -> tuple[list[str], int]:
    splits = 0
    for i in range(len(lines) - 1):
        lines, s = iteration(lines, i)
        splits += s
    
    return lines, splits

def fancy_print(lines: list[str], splits: int = -1):
    print("############ Manifold ##############")
    print("\n".join(lines))
    print("####################################")
    if splits != -1:
        print("Splits: " + str(splits))
        print("####################################")

def iteration(lines: list[str], line_idx: int) -> tuple[list[str], int]:
    if (line_idx >= len(lines) - 1):
        return (lines, 0)

    cur_line = lines[line_idx]
    next_line = lines[line_idx + 1]
    splits = 0

    for i in get_indices(cur_line):
        below = next_line[i]
        if below == SPLITTER:
            next_line = string_set(next_line, i - 1, BEAM)
            next_line = string_set(next_line, i + 1, BEAM)
            splits += 1
        
        else:
            next_line = string_set(next_line, i, BEAM)

    lines[line_idx + 1] = next_line
    return (lines, splits)

def string_set(string: str, idx: int, value: str):
    if idx == 0:
        return value + string[1:]
    
    elif idx == len(string) - 1:
        return string[:len(string) - 1] + value
    
    else: 
        return string[:idx] + value + string[idx + 1:]

def get_indices(line: str) -> list[int]:
    res = []
    for i in range(len(line)):
        if line[i] in [START, BEAM]:
            res.append(i)

    return res

if __name__ == "__main__":
    main()
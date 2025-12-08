INPUT = r"input.txt"
TEST_INPUT = r"test_input.txt"

START = "S"
BEAM = "|"
SPLITTER = "^"

def main():
    with open(TEST_INPUT, "r", encoding="utf-8") as file:
        timelines = [[f.replace("\n", "") for f in file.readlines()]]

        m = len(timelines[0])
        for i in range(m - 1):
            s = f"{len(timelines):,}".replace(",", ".")
            print(f"Currently in line {i} of {m} ({int(i/m*100)}%) with {s} timelines", end=" " * 30 + "\r")
            timelines = next_iteration(timelines, i)

        s = f"{len(timelines):,}".replace(",", ".")
        print(f"Timelines: {s}")

def fancy_print(lines: list[str]):
    print("############ Manifold ##############")
    print("\n".join(lines))
    print("####################################")

def next_iteration(timelines: list[list[str]], line_idx: int) -> list[list[str]]:
    result = []
    for t in timelines:
        result += single_iteration(t, line_idx)

    return result

def single_iteration(timeline: list[str], line_idx: int) -> list[list[str]]:
    if (line_idx >= len(timeline) - 1):
        return [timeline]

    cur_line = timeline[line_idx]
    next_line = timeline[line_idx + 1]

    beam_idx = cur_line.find(BEAM) if BEAM in cur_line else cur_line.find(START)
    below = next_line[beam_idx]

    if below == SPLITTER:
        t1 = timeline.copy()
        t1[line_idx + 1] = string_set(next_line, beam_idx - 1, BEAM)

        t2 = timeline.copy()
        t2[line_idx + 1] = string_set(next_line, beam_idx + 1, BEAM)

        return [t1, t2]
    
    else:
        next_line = string_set(next_line, beam_idx, BEAM)

    timeline[line_idx + 1] = next_line
    return [timeline]

def string_set(string: str, idx: int, value: str) -> str:
    if idx == 0:
        return value + string[1:]
    
    elif idx == len(string) - 1:
        return string[:len(string) - 1] + value
    
    else: 
        return string[:idx] + value + string[idx + 1:]

if __name__ == "__main__":
    main()
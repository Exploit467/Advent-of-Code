INPUT = r"Advent of Code 2025\Advent of Code 2025 - Day 6\input.txt"
TEST_INPUT = r"Advent of Code 2025\Advent of Code 2025 - Day 6\test_input.txt"

def main():
    with open(INPUT, "r", encoding="utf-8") as file:
        data = strip(file.readlines())

        result = 0
        for line in data:
            result += calc(line)

        print("Result: " + str(result))

def calc(data: list[str]) -> int:
    operator = data[-1].strip()
    values = calc_parameters(data[:len(data) - 1])

    current = values[0]
    for i in range(1, len(values)):
        current = handle(current, values[i], operator)

    print(operator, values, current)
    return current

def handle(v1: int, v2: int, op: str) -> int:
    return v1 + v2 if op == "+" else v1 * v2

def calc_parameters(t_list: list[str]) -> list[int]:
    result = []
    while True:
        param = ""
        for i in range(len(t_list)):
            val = t_list[i]
            if val == "":
                continue
            param += val[-1]
            t_list[i] = val[:len(val) - 1]

        # no chars left
        if param == "":
            break

        result.append(int(param.strip()))

    return result

def strip(t_list: list[str]) -> list[str]:  
    # Split at space columns but keep other spaces
    t_list = [s.replace("\n", "") for s in t_list]
    result = []
    while True:
        s = len(t_list[0])
        line = []

        if s <= 0:
            break
        for idx in range(s + 1):
            all_spaces = True
            eol = True
            for i in range(len(t_list)):
                if idx < len(t_list[i]):
                    eol = False

                    if t_list[i][idx] != " ":
                        all_spaces = False

            # End of line reached => no more split required
            if eol:
                for i in range(len(t_list)):
                    line.append(t_list[i])
                    t_list[i] = []
                
                result.append(line)
                break

            # Whole column is spaces => split
            if all_spaces:
                for i in range(len(t_list)):
                    line.append(t_list[i][:idx])
                    t_list[i] = t_list[i][idx + 1:]

                result.append(line)
                break

    return result
        
if __name__ == "__main__":
    main()
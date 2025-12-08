INPUT = r"input.txt"
TEST_INPUT = r"test_input.txt"

def main():
    with open(INPUT, "r", encoding="utf-8") as file:
        data = strip(file.readlines())
        data = [s.split(" ") for s in data]
        data = switch_list_orientation(data)

        result = 0
        for line in data:
            result += calc(line)

        print("Result: " + str(result))

def calc(data: list[str]) -> int:
    operator = data[-1]
    values = data[:len(data) - 1]

    current = values[0]
    for i in range(1, len(values)):
        current = handle(current, values[i], operator)

    return current

def handle(v1: str, v2: str, op: str) -> int:
    v1, v2 = int(v1), int(v2)
    return v1 + v2 if op == "+" else v1 * v2

def switch_list_orientation(t_list: list[list[str]]) -> list[str]:
    # assuming list ist n^2 in size
    s = len(t_list[0])

    reoriented: list[list[str]] = []
    for i in range(s):
        reoriented.append([])
        for sublist in t_list:
            reoriented[i].append(sublist[i]) 

    return reoriented

def strip(list: list[str]) -> list[str]:  
    for i in range(len(list)):
        # remove all multi-spaces
        while "  " in list[i]:
            list[i] = list[i].replace("  ", " ")

        list[i] = list[i].replace("\n", "").strip()

    return list

if __name__ == "__main__":
    main()
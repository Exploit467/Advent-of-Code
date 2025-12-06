INPUT = r"Advent of Code 2025\Advent of Code 2025 - Day 5\input.txt"
TEST_INPUT = r"Advent of Code 2025\Advent of Code 2025 - Day 5\test_input.txt"

def main():
    with open(INPUT, "r", encoding="utf-8") as file:
        data = file.readlines()
        data = [s.replace("\n", "") for s in data]

        ranges, ids = cut_at_condition(data, lambda x: x == "")
        ranges = [r.split("-") for r in ranges]

        valid_ids = set()
        for id in ids:
            id = int(id)
            for range in ranges:
                if id >= int(range[0]) and id <= int(range[1]):
                    valid_ids.add(id)
                    break

        print(len(valid_ids))

def cut_at_condition(list: list[str], condition) -> tuple[list[str], list[str]]:
    for idx in range(len(list)):
        val = list[idx]
        if condition(val):
            return list[:idx], list[idx + 1:]

    raise ValueError(cut_at_condition.__name__, list)

if __name__ == "__main__":
    main()
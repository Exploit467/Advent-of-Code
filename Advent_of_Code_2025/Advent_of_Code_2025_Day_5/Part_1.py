INPUT = r"input.txt"
TEST_INPUT = r"test_input.txt"

def main():
    with open(INPUT, "r", encoding="utf-8") as file:
        data = file.readlines()
        data = [s.replace("\n", "") for s in data]

        ranges, ids = cut_input(data)
        ranges = [r.split("-") for r in ranges]

        valid_ids = set()
        for id in ids:
            id = int(id)
            for range in ranges:
                if id >= int(range[0]) and id <= int(range[1]):
                    valid_ids.add(id)
                    break

        print(len(valid_ids))

def cut_input(list: list[str]) -> tuple[list[str], list[str]]:
    for idx in range(len(list)):
        if list[idx] == "":
            return list[:idx], list[idx + 1:]

    raise ValueError(cut_input.__name__, list)

if __name__ == "__main__":
    main()
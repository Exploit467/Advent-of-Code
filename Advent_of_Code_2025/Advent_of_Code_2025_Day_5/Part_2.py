INPUT = r"input.txt"
TEST_INPUT = r"test_input.txt"

def main():
    with open(TEST_INPUT, "r", encoding="utf-8") as file:
        data = file.readlines()
        data = [s.replace("\n", "") for s in data]

        ranges, _ = cut_input(data)
        ranges = [r.split("-") for r in ranges]
        ranges: list[tuple[int, int]] = [(int(r[0]), int(r[1])) for r in ranges]

        checked_ranges: list[tuple[int, int]] = []
        valid_ids = 0

        for range in ranges:
            valid_ids += get_unique_range(range, checked_ranges)
            checked_ranges.append(range)

        print("Valid IDs: " + str(valid_ids))

def get_unique_range(range: tuple[int, int], checked_ranges: list[tuple[int, int]]) -> int:
    to_check = [range]
    for cr in checked_ranges:
        to_check = cut_overlap(to_check, cr)

    range_lengths = [r[1] - r[0] + 1 if r[0] != -1 else 0 for r in to_check]
    return sum(range_lengths)

def cut_overlap(range: list[tuple[int, int]], overlap: tuple[int, int]):
    result = []
    for subrange in range:
        result += cut_single_overlap(subrange, overlap)

    return result

def cut_single_overlap(subrange: tuple[int, int], overlap: tuple[int, int]) -> list[tuple[int, int]]:
    minR, maxR, minO, maxO = subrange[0], subrange[1], overlap[0], overlap[1]

    if minO >= minR and minO <= maxR:
        if maxO >= maxR:
            # overlap covers upper part
            return [(minR, minO - 1)]
        else:
            # overlap is within => split into two subranges
            return [(minR, minO - 1), (maxO + 1, maxR)]
    
    if maxO <= maxR and maxO >= minR:
        if minO <= minR:
            # overlap covers lower part
            return [(maxO + 1, maxR)]
        else:
            # overlap is within => split into two subranges
            return [(minR, minO - 1), (maxO + 1, maxR)]

    # overlap covers the whole subrange => whole range is NOT unique
    if minO <= minR and maxO >= maxR:
        return [(-1, -1)]

    return [subrange]

def cut_input(list: list[str]) -> tuple[list[str], list[str]]:
    for idx in range(len(list)):
        if list[idx] == "":
            return list[:idx], list[idx + 1:]

    raise ValueError(cut_input.__name__, list)

if __name__ == "__main__":
    main()
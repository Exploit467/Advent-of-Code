def main():
    with open(r"Advent of Code 2025\Advent of Code 2025 - Tag 2\ranges.txt", "r") as file:
        lines = file.readlines()[0]
        ranges = lines.split(",")

        invalidIDS = set()
        for n, r in enumerate(ranges):
            # Fancy log
            print(f"Processing Range {n + 1}/{len(ranges)} ({int((n + 1) / len(ranges) * 100)}%): {r}", end=" " * 30 + "\r")

            rr = r.split("-")

            _from, _to = int(rr[0]), int(rr[1])
            for i in range(_from, _to + 1):
                val = str(i)
                for a in range(2, len(val) + 1):
                    parts = equally_sized_parts(val, a)

                    if (all_equal(parts)):
                        invalidIDS.add(i)

        print("Summe ungültiger IDS:", sum(int(a) for a in invalidIDS), " " * 30)

def equally_sized_parts(string: str, count: int) -> list[str]:
    l = len(string)
    if count <= 1 or l < count or l % count != 0:
        return []
    
    result = []
    step = l // count
    while (string != ""):
        result.append(string[:step])
        string = string[step:]

    return result

def all_equal(list: list[str]) -> bool:
    return all(e == list[0] for e in list) if len(list) > 0 else False

if __name__ == "__main__":
    main()
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
                half_idx = len(str(i)) // 2
                half1, half2 = str(i)[:half_idx], str(i)[half_idx:]

                if half1 == half2:
                    invalidIDS.add(i)

        print("Summe ungültiger IDS:", sum(int(a) for a in invalidIDS), " " * 30)

if __name__ == "__main__":
    main()
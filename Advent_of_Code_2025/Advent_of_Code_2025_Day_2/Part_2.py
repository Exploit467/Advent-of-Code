INPUT = r"input.txt"

def main():
    with open(INPUT, "r") as file:
        ranges = file.readlines()[0].split(",")

        invalidIDS = set()
        for n, r in enumerate(ranges):
            # Fancy log
            # print(f"Processing Range {n + 1}/{len(ranges)} ({int((n + 1) / len(ranges) * 100)}%): {r}", end=" " * 30 + "\r")

            [_from, _to] = [int(s) for s in r.split("-")]
            for i in range(_from, _to + 1):
                val = str(i)
                for a in range(2, len(val) + 1):
                    if(check_by_part_size(val, a)):
                        invalidIDS.add(i)

        print("Solution:", sum(int(a) for a in invalidIDS), " " * 30)

def check_by_part_size(string: str, size: int) -> bool:
    l = len(string)
    if size <= 1 or l < size or l % size != 0:
        return False
    
    sub = None
    step = l // size
    while (string != ""):
        next, string = string[:step], string[step:]
        if next == sub or sub is None:
            sub = next
            continue
        
        return False
    
    return True

if __name__ == "__main__":
    main()
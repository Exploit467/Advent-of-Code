from Part_1 import calc, fancy_print

INPUT = r"input.txt"
TEST_INPUT = r"test_input.txt"

START = "S"
BEAM = "|"
SPLITTER = "^"

def main():
    with open(INPUT, "r", encoding="utf-8") as file:
        lines = [f.replace("\n", "") for f in file.readlines()]

        t1 = Timelines(lines)
        
        while not t1.is_last_line():
            t1.next_iteration()

        t1.print_timelines()


class Timelines:
    def __init__(self, lines: list[str]):
        self.cur_idx: int = -1
        
        tree, _ = calc(lines)
        self.lines: list[str] = self.reverse(tree)

        self.timelines: list['Timeline'] = []

    def is_last_line(self) -> bool:
        return self.cur_idx == len(self.lines) - 1

    def print_tree(self, reverse: bool = True):
        fancy_print(self.reverse(self.lines) if reverse else self.lines)

    def print_timelines(self):
        for t in self.timelines:
            print(str(t))

    def fancy_iteration(self):
        print("#" * 50)
        print("Next iteration!")
        print("#" * 50)
        self.next_iteration()
        self.print_timelines()

    def next_iteration(self):
        if self.cur_idx == -1:
            self.first_line()
        
        else:
            self.merge_all()
        
        self.cur_idx += 1
            

    def first_line(self) -> None:
        string_line = self.lines[0]
        self.timelines = []
        for i in range(len(string_line)):
            if string_line[i] == BEAM:
                self.timelines.append(Timeline(i, 0, 1))

        self.sort()

    def sort(self):
        self.timelines.sort(key = lambda x: x.pos)

    def merge_all(self) -> None:
        current_line = self.lines[self.cur_idx]
        result = []
        
        # assuming timeline are in correct order from left to right
        for idx, current in enumerate(self.timelines):
            if idx >= len(self.timelines) - 1:
                continue

            next = self.timelines[idx + 1]

            merged = Timeline.merge(current_line, current, next)
            if merged is not None:
                result.append(merged)

        # Check for timelines that need to go straigth up
        for t in self.timelines:
            if t.has_beam_above(self.lines):
                t.move_up()
                result.append(t)

        self.timelines = result

        # Last but not least: Sort
        self.sort()

    @staticmethod
    def reverse(list: list) -> list:
        result = []
        for t in reversed(list):
            result.append(t)

        return result

class Timeline:
    def __init__(self, pos: int, line: int, timelines: int):
        self.pos = pos
        self.line = line
        self.timelines = timelines

    def __str__(self):
        formatted_number = f"{self.timelines:,}".replace(",", ".")
        return f"Positon: {self.pos}, Line: {self.line}, Timelines: {formatted_number}"

    def move_up(self):
        self.line += 1

    def has_beam_above(self, lines: list[str]):
        return lines[self.line][self.pos] == BEAM

    @staticmethod
    def merge(string_line: str, t1: 'Timeline', t2: 'Timeline') -> 'Timeline':
        if abs(t1.pos - t2.pos) != 2:
            # Not next to each other => cannot be merged
            return None

        new_pos = min(t1.pos, t2.pos) + 1
        
        if string_line[new_pos] != SPLITTER:
            # No splitter in between => cannot be merged
            return None

        assert t1.line == t2.line, "Given timelines are in different lines"
        new_line = t1.line + 1

        return Timeline(new_pos, new_line, t1.timelines + t2.timelines)

if __name__ == "__main__":
    main()
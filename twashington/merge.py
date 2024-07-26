"""
    T Washington
    Merge Intervals
"""


def intervals_intersect(x, y):
    if x is None or y is None:
        return False
    return not (x[1] < y[0] or y[1] < x[0])


def merge_two_intervals(x, y):
    return [min(x[0], y[0]), max(x[1], y[1])]


def merge_interval_list(intervals):
    ins = intervals.copy()
    size = len(ins)

    for a in range(size):
        for b in range(a + 1, size):
            if intervals_intersect(ins[a], ins[b]):
                ins[a] = merge_two_intervals(ins[a], ins[b])
                ins[b] = None
    return [c for c in ins if c is not None]


def get_input_list():
    ins = [[[1, 3], [2, 6], [8, 10], [15, 18]]]
    ins.append([[1, 4], [4, 5]])
    ins.append([[-1000, 1000]])
    ins.append([[2, 6], [1, 3], [8, 10], [15, 18]])
    ins.append([[1, 4], [0, 0]])
    ins.append([[1, 4], [2, 3]])
    ins.append([[1, 4], [0, 2], [3, 5]])
    ins.append([[5, 6], [1, 2], [2, 4], [7, 9]])
    ins.append([[-1, 1], [-2, 2], [-3, 3]])
    ins.append([[1, 10], [2, 6], [8, 10], [15, 18]])
    ins.append([[5, 6], [5, 5], [6, 6]])
    ins.append([[1, 2], [2, 3], [3, 4], [4, 5]])
    ins.append([[1, 3], [4, 6], [7, 9], [10, 12]])
    ins.append([[10, 20], [15, 25], [5, 15], [0, 5]])
    ins.append([[1, 5], [2, 6], [8, 10], [9, 12]])
    ins.append([[1, 4], [0, 5], [5, 10]])
    ins.append([[-10, -5], [-6, 0], [1, 2], [2, 3]])
    ins.append([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])

    return ins


def main():
    input_list_list = get_input_list()
    for input_list in input_list_list:
        output_list = sorted(merge_interval_list(input_list), key=lambda x: x[0])
        print(f"Input: {input_list}, output: {output_list}")


if __name__ == "__main__":
    main()

"""
    T Washington
    Merge Intervals
"""


def merge_interval_list(intervals):
    ins = intervals.copy()
    for a in range(len(ins)):
        for b in range(a + 1, len(ins)):
            if not (ins[a] is None or ins[b] is None) and not (ins[a][1] < ins[b][0] or ins[b][1] < ins[a][0]):
                ins[a] = [min(ins[a][0], ins[b][0]), max(ins[a][1], ins[b][1])]
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

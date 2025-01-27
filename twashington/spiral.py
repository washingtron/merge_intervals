"""
    T Washington
    Spirals
"""
import time


def get_input_list(filename):
    matrix_list = []

    with open(filename, 'r') as file:
        for line in file:
            # Strip whitespace and newlines, and evaluate the string as a Python expression
            stripped_line = line.strip()
            if stripped_line:  # Check if line is not empty
                matrix = eval(stripped_line)
                matrix_list.append(matrix)

    return matrix_list


def top(input_list, i):
    y = len(input_list)
    x = len(input_list[0])
    if 2 * i <= y and 2 * i < x:
        return input_list[i][i:(x - i - 1)]
    else:
        return []


def right(input_list, i):
    y = len(input_list)
    x = len(input_list[0])
    if 2 * i <= x and 2 * i < y:
        return [input_list[a][x - i - 1] for a in range(i, y - i - 1)]
    else:
        return []


def bottom(input_list, i):
    y = len(input_list)
    x = len(input_list[0])
    if 2 * i + 1 < y and 2 * i < x:
        return input_list[y - 1 - i][(x - i + 1):i:-1]
    else:
        return []


def left(input_list, i):
    y = len(input_list)
    x = len(input_list[0])
    if 2 * i + 1 < x and 2 * i < y:
        return [input_list[a][i] for a in range(y - i - 1, i, -1)]
    else:
        return []


def spiralify(input_list):
    y = len(input_list)
    x = len(input_list[0])
    i = 0
    output = []
    while i <= int(y/2) or i <= int(x/2):
        output.append(top(input_list, i))
        output.append(right(input_list, i))
        output.append(bottom(input_list, i))
        output.append(left(input_list, i))
        i = i + 1
    return output  # [b for item in output for b in item]


def main():
    input_matrix_list = get_input_list("matrix_input.txt")
    start = time.perf_counter_ns()
    for input_list in input_matrix_list:
        output_list = spiralify(input_list)
        end = time.perf_counter_ns()
        print(f"Input: {input_list}, output: {output_list}")
    print(f"Time taken: {(end - start):.4f} ns")


if __name__ == "__main__":
    main()

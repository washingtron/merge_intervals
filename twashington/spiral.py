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
    if i * 2 > y:
        return input_list[i][i:(-1 * i)]
    else:
        return []


def right(input_list, i):
    y = len(input_list)
    x = len(input_list[0])
    return [a for a in range()]


def bottom(input_list, i):
    y = len(input_list)
    x = len(input_list[0])
    pass


def left(input_list, i):
    y = len(input_list)
    x = len(input_list[0])
    pass


def spiralify(input_list):
    y = len(input_list)
    x = len(input_list[0])
    i = 0
    output = []
    while i < int(y/2) and i < int(x/2):
        output.append(top(input_list, i), right(input_list, i), bottom(input_list, i), left(input_list, i))
        i = i + 1


def main():
    input_matrix_list = get_input_list("matrix_input.txt")
    for input_list in input_matrix_list:
        start = time.perf_counter_ns()
        output_list = spiralify(input_list)
        end = time.perf_counter_ns()
        print(f"Input: {input_list}, output: {output_list}")
        print(f"Time taken: {(end - start):.4f} ns")


if __name__ == "__main__":
    main()

"""
    T Washington
    Spirals
"""
import time


def get_input_list(filename):
    matrix_list = []

    with open(filename, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line:
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
    while i <= int(y / 2) or i <= int(x / 2):
        output.append(top(input_list, i))
        output.append(right(input_list, i))
        output.append(bottom(input_list, i))
        output.append(left(input_list, i))
        i = i + 1
    return output  # [b for item in output for b in item]


def spiralify2(raw):
    x0, x1, y0, y1 = 0, len(raw[0]) - 1, 0, len(raw) - 1
    output = []
    while x0 <= x1 and y0 <= y1:
        if x0 == x1:
            output.append([raw[a][x0] for a in range(y0, y1 + 1)])
        elif x0 + 1 == x1:
            output.append(
                [raw[y0][x0]] + [raw[a][x1] for a in range(y0, y1 + 1)] + [raw[a][x0] for a in
                                                                           range(y1, y0, -1)])
        elif y0 == y1:
            output.append([raw[y0][a] for a in range(x0, x1 + 1)])
        elif y0 + 1 == y1:
            output.append(
                [raw[y0][a] for a in range(x0, x1 + 1)] + [raw[y1][a] for a in range(x1, x0 - 1, -1)])
        else:
            output.append([raw[y0][a] for a in range(x0, x1 + 1)])
            output.append([raw[a][x1] for a in range(y0 + 1, y1 + 1)])
            output.append([raw[y1][a] for a in range(x1 - 1, x0 - 1, -1)])
            output.append([raw[a][x0] for a in range(y1 - 1, y0, -1)])
        x0 = x0 + 1
        x1 = x1 - 1
        y0 = y0 + 1
        y1 = y1 - 1
    return [b for item in output for b in item]  # output


def main():
    input_matrix_list = get_input_list("matrix_input.txt")
    input_matrix_list.append([[i * 26 + j + 1 for j in range(26)] for i in range(23)])
    input_matrix_list.append([[i * 35 + j + 1 for j in range(35)] for i in range(23)])
    input_matrix_list.append([[i * 35 + j + 1 for j in range(35)] for i in range(44)])
    start = time.perf_counter_ns()
    for input_list in input_matrix_list[2:]:
        output_list = spiralify2(input_list)
        end = time.perf_counter_ns()
        print(f"Input: {input_list}, output: {output_list}")
        if len(output_list) != len([b for item in input_list for b in item]):
            print(f'Error, input and output lists have different number of elements')
        if len(set(output_list)) != len(output_list):
            print(f'Error, output list values are not unique. len(set(output_list)) ={len(set(output_list))}, len(output_list) = {len(output_list)}')
    print(f"Time taken: {(end - start):.4f} ns")


if __name__ == "__main__":
    main()

input_file = 'input.txt'


def read_file():
    edges = []
    with open(input_file, 'r') as file:
        for line in file:
            edges.append(line.replace('\n', '').split(' '))
        for i in range(len(edges)):
            for j in 0, 1:
                try:
                    edges[i][j] = int(edges[i][j])
                except:
                    raise Exception('Invalid input')
    return edges


def count_degree(edges):
    degrees = {}
    for i in range(len(edges)):
        for j in 0, 1:
            this_edge = edges[i][j]
            if this_edge not in degrees.keys():
                degrees[this_edge] = 1
            else:
                degrees[this_edge] += 1
    return degrees


def frequency(degrees):
    freq_dict = {}
    for value in degrees.values():
        freq_dict[value] = freq_dict.get(value, 0) + 1
    return freq_dict


def selection_sort(degrees):
    items = list(degrees.items())
    n = len(items)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if items[j][1] < items[min_idx][1]:
                min_idx = j
        items[i], items[min_idx] = items[min_idx], items[i]
    sorted_dict = dict(items)
    return sorted_dict


if '__main__' == __name__:
    edges = read_file()
    degrees = count_degree(edges)
    freq = frequency(degrees)
    sorted_vertex = selection_sort(degrees)
    for i in sorted_vertex:
        print("Vertex", i, "degree is", degrees[i])
    for n in freq:
        print("Frequency of degree", n, "is", freq[n])

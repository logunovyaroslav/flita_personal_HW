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


def selection_sort(degrees):
    arr = []
    for i in degrees.keys():
        arr.append(i)
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if '__main__' == __name__:
    edges = read_file()
    degrees = count_degree(edges)
    sorted_vertex = selection_sort(degrees)
    for i in sorted_vertex:
        print("Vertex ", i, '\t', degrees[i], sep='')



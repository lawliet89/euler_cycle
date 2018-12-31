#!/usr/bin/python3


def str_list_to_dict(str_list):
    graph = {}
    for row in str_list:
        i = row.split('->')
        key = i[0].strip()
        value = i[1].strip()
        graph[int(key)] = [int(x) for x in value.split(',')]
    return graph


def get_edges(graph):
    edges = []
    for k, v in graph.items():
        edges += [(k, val) for val in v]

    return edges


def get_vertices(graph):
    return list(graph.keys())


def vertices_from_edges(edges):
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return vertices


def hierholzer(graph):
    edges = get_edges(graph)
    vertices = get_vertices(graph)

    i = 0
    v = vertices[i]

    c = []  # Ordered
    v_i = v

    while True:
        while True:
            edges_from_v = [(v_i, v_i_1) for v_i_1 in graph[v_i]]

            # Find an edge not already in C from v
            eligible_edges = set(edges_from_v) - set(c)
            if len(eligible_edges) == 0:
                # Hmmmmmm we are "stuck"
                break

            # We just choose the first one
            edge_next = next(iter(eligible_edges))
            c.append(edge_next)
            v_i = edge_next[1]

        if set(c) == set(edges):
            # We are done
            break
        # Otherwise, TODO

    return c


def main():
    # Assume Euler Cycle exists
    input_list = ["0 -> 3", "1 -> 0", "2 -> 1,6", "3 -> 2",
                  "4 -> 2", "5 -> 4", "6 -> 5,8", "7 -> 9", "8 -> 7", "9 -> 6"]

    graph = str_list_to_dict(input_list)
    print(graph)
    edges = set(get_edges(graph))
    print(edges)

    print(hierholzer(graph))


if __name__ == "__main__":
    main()

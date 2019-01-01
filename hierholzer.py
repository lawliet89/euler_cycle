#!/usr/bin/python3


def has_next(iterable):
    """
    Check if an iterable (e.g. generator) has a next item
    WARNING: This will consume the next item in a generator
    """
    try:
        next(iterable)
        return True
    except StopIteration:
        return False


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


def build_circuit(starting_vertex, edges):
    # First, build a dictionary of Vertices -> [Vertices]
    graph = {}
    for (a, b) in edges:
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]

    circuit = []
    v = starting_vertex

    while True:
        try:
            # Edges from V not already in circuit
            edges_from_v = ((v, v_next)
                            for v_next in graph[v]
                            if (v, v_next) not in circuit)
            edge_next = next(edges_from_v)
            circuit.append(edge_next)
            v = edge_next[1]
        except (StopIteration, KeyError):
            # We are stuck. There are no more eligible edges
            break

    # Sanity check
    # The end of final node must be starting_vertex
    # It is not possible to get stuck at any vertex other than v,
    # because the even degree of all vertices ensures that,
    # when the trail enters another vertex w
    # there must be an unused edge leaving w.
    assert(starting_vertex == circuit[-1][1])

    return circuit


def hierholzer(graph):
    edges = set(get_edges(graph))
    vertices = get_vertices(graph)

    # Let's start from the first Vertex
    vi = vertices[0]
    # Try to build a circuit
    # Step 1
    ci = build_circuit(vi, edges)  # Ordered
    while True:
        set_ci = set(ci)

        # Step 2.1
        if set_ci == edges:
            # We are done
            break

        # Step 2.2
        # Find a vertex Vi on Ci that is incident to an edge not in Ci
        vi_index = -1
        for i in range(len(ci)):
            edge = ci[i][1]
            # Now try to find an edge in the graph which is not in ci but has`edge`
            # on the left hand side
            if edge not in graph:
                continue
            else:
                other_edges = (other for other in graph[edge] if (
                    edge, other) not in ci)
                if has_next(other_edges):
                    vi_index = i
                    vi = edge
                    break

        # Sanity check
        # We should be able to find a vi_index and vi
        assert(vi_index != -1)

        # Build circuit C_star beginning with vi in the graph G - C
        remaining_edges = edges - set_ci
        assert(len(remaining_edges) > 0)
        ci_star = build_circuit(vi, remaining_edges)
        # Step 3
        # Build a new ci by going from the first node in ci to vi using the circuit in ci
        # Then going from vi to vi again using ci_star
        # And then continuing from vi to the end of ci
        next_ci = ci[0:vi_index + 1] + ci_star + ci[vi_index + 1:]
        ci = next_ci

    return ci


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

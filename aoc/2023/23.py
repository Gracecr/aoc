from aoc.util import *

D = get_data().splitlines()
# D = """#.#####################
# #.......#########...###
# #######.#########.#.###
# ###.....#.>.>.###.#.###
# ###v#####.#v#.###.#.###
# ###.>...#.#.#.....#...#
# ###v###.#.#.#########.#
# ###...#.#.#.......#...#
# #####.#.#.#######.#.###
# #.....#.#.#.......#...#
# #.#####.#.#.#########v#
# #.#...#...#...###...>.#
# #.#.#v#######v###.###v#
# #...#.>.#...>.>.#.###.#
# #####v#.#.###v#.#.###.#
# #.....#...#...#.#.#...#
# #.#########.###.#.#.###
# #...###...#...#...#.###
# ###.###.#.###v#####v###
# #...#...#.#.>.>.#.>.###
# #.###.###.#.###.#.#v###
# #.....###...###...#...#
# #####################.#""".splitlines()
START = (0, 1)
END = (len(D) - 1, len(D[0]) - 2)
V = get_vectors(2)
B = get_bounds(D)


HILL_MAP = {
    "^": [(-1, 0)],
    ">": [(0, 1)],
    "<": [(0, -1)],
    "v": [(1, 0)],
    ".": V,
}


def create_graph(part1: bool):
    # Part 1 does not work :(
    g = nx.Graph()
    for r, line in enumerate(D):
        for c, ch in enumerate(line):
            if ch == "#":
                continue
            vectors = HILL_MAP[ch] if part1 else HILL_MAP["."]
            for n in get_neighbors((r, c), vectors, B):
                if D[n[0]][n[1]] == "#":
                    continue
                g.add_edge((r, c), n, weight=1)

    nodes = list(g.nodes)
    for node in nodes:
        neighbors = list(g.neighbors(node))
        if len(neighbors) == 2:
            new_weight = (
                g.get_edge_data(node, neighbors[0])["weight"]
                + g.get_edge_data(node, neighbors[1])["weight"]
            )
            g.add_edge(neighbors[0], neighbors[1], weight=new_weight)
            g.remove_node(node)

    return g


def dfs2(g, v, goal, vis: set, path_len=0):
    if v == goal:
        return path_len

    vis.add(v)

    path_lens = []
    for n in g.neighbors(v):
        if n in vis:
            continue
        weight = g.get_edge_data(v, n)["weight"]
        path_lens.append(dfs2(g, n, goal, vis, path_len + weight))

    vis.remove(v)
    return max(path_lens) if path_lens else -1


print(dfs2(create_graph(False), START, END, set()))


# def dfs(v, goal, vis: set, path_len=0):
#     # print(v)
#     if v == goal:
#         return path_len

#     vis.add(v)
#     new_vis = set([v])
#     ch = D[v[0]][v[1]]
#     # neighbors = [addt(v, HILL_MAP[ch])] if ch in HILL_MAP else get_neighbors(v, V, B)
#     neighbors = get_neighbors(v, V, B)
#     while len(neighbors) == 2:
#         v = next(n for n in neighbors if n not in vis)
#         vis.add(v)
#         new_vis.add(v)
#         path_len += 1
#         # neighbors = (
#         #     [addt(v, HILL_MAP[ch])] if ch in HILL_MAP else get_neighbors(v, V, B)
#         # )
#         neighbors = get_neighbors(v, V, B)

#     path_lens = []
#     for n in neighbors:
#         if n not in vis and D[n[0]][n[1]] in ".v<>^":
#             path_lens.append(dfs(n, goal, vis, path_len + 1))

#     vis -= new_vis

#     return max(path_lens) if path_lens else -1

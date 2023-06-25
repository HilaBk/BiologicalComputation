import networkx as nx
from itertools import combinations as cb


# ************************************ PART 2 ************************************

# ~ creating directed graph function ~
def create_graph(edges_list):
    return nx.DiGraph(edges_list)


# ~ generating subgraph function ~
def generate_subgraphs(size, graph):
    subgraphs = []
    combinations = graph.nodes()
    num_combinations = len(combinations) + 1
    i = 1
    while i < num_combinations:
        for combination in cb(combinations, i):
            subgraph = graph.subgraph(combination)
            if len(subgraph) == size:
                subgraphs.append(subgraph)
        i += 1
    count_array = [1] * len(subgraphs)
    for i in range(len(subgraphs)):
        for j in range(i + 1, len(subgraphs)):
            if nx.is_isomorphic(subgraphs[i], subgraphs[j]):
                count_array[i] += 1
                count_array[j] = 0
    total_subgraph = [(subgraph, count) for subgraph, count in zip(subgraphs, count_array) if count > 0]
    return total_subgraph


# ~ output text file function ~
def write_results(size, different_motifs):
    with open(f"res{size}.txt", 'w') as f:
        f.write(f"n={size}\n")
        count = 1
        for motif, occurrence_count in different_motifs:
            f.write(f"count={occurrence_count}\n")
            f.write(f"#{count}\n")
            for edge in motif.edges:
                f.write(f"{edge[0]} {edge[1]}\n")
            count += 1

# ~ main function ~
if __name__ == "__main__":
    motif_size = 3
    edges_list = [(1, 2), (2, 3), (1, 4)]
    graph = create_graph(edges_list)
    subgraphs = generate_subgraphs(motif_size, graph)
    write_results(motif_size, subgraphs)

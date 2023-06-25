import itertools
import networkx as nx
from collections import defaultdict


# Generating subgraph function
def generate_subgraphs_size_n(n, graph):
    vertices = list(range(1, len(graph) + 1))
    vertices_len = len(vertices)
    motifs = []  # every combination has a potential to be a motif

    for i in range(1, vertices_len + 1):
        allCombinations = itertools.combinations(vertices, i)
        for combination in allCombinations:
            new_graph = nx.DiGraph()
            new_graph.add_nodes_from(combination)
            for edge in graph.edges:
                s, t = edge
                if s in new_graph.nodes and t in new_graph.nodes:
                    if len(combination) == n:
                        if (s, t) != (0, 0):
                            new_graph.add_edge(s, t)
            if nx.is_weakly_connected(new_graph):
                motifs.append(new_graph.edges())

    print(len(motifs))
    print(motifs)
    return motifs




def save_subgraphs(map, filename, n):
        with open(filename, 'w') as file:
            for subgraph, data in map.items():
                file.write("n=" + str(n) + "\n")
                file.write("count=" + str(data["count"]) + "\n")

                for i, subgraph in enumerate(map.items(), start=1):
                    file.write(f"#{i}\n")

                    for j in range(1, i):
                        previous_subgraph = list(map.items())[j - 1]
                        for node in previous_subgraph:
                            file.write(str(node))
                        file.write("\n")

                    for node in subgraph:
                        file.write(str(node))
                    file.write("\n")
             


if __name__ == "__main__":
    n = 3
    graph = [(1, 2), (2, 3), (1, 4)]
    graphDircted = nx.DiGraph(graph)
    n_subgraphs = []
    subgraph_map = defaultdict(int) 

    # Find all the n subgraphs that exist in the graph
    for subgraph in generate_subgraphs_size_n(n, graphDircted):
        change_to_list = list(tuple(subgraph)) #needed to change to tuple
        n_subgraphs.append(nx.DiGraph(change_to_list))
        subgraph_graph = nx.DiGraph(change_to_list)  # Create a DiGraph from the list of edges
        subgraph_map[subgraph_graph] = {"edges": subgraph_graph.edges(), "count": 1}
 

    subgraphs_to_remove = []  # Store the subgraphs to be removed from the map

    for sub1, sub1_data in subgraph_map.items():
        if len(subgraph_map) == 1:
            break
        for sub2, sub2_data in subgraph_map.items():
            if sub1 != sub2 and nx.is_isomorphic(sub1, sub2):
                subgraph_map[sub1]["count"] += 1
                subgraphs_to_remove.append(sub2)  # Add sub2 to the removal list
                break  # No need to continue checking isomorphism with other subgraphs

    
    for subgraph, data in subgraph_map.items():
        if not data["edges"]:
            subgraphs_to_remove.append(subgraph)

    for subgraph in subgraphs_to_remove:
        if subgraph in subgraph_map:
            del subgraph_map[subgraph]
    
    for subgraph, data in subgraph_map.items():
        print("Subgraph Edges:", data["edges"])
        print("Count:", data["count"])
        print("---------------")


    filename = f"Part2_subgraphs_{n}.txt"
    save_subgraphs(subgraph_map, filename, n)
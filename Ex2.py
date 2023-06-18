import itertools
import networkx as nx
import time

# ************************************ Quastion A ************************************
# ~ generating subgraph function ~
def findIsomorphism(graph, motifs):
    isIsomorphic = False
    for motif in motifs:
        motif = nx.DiGraph(motif)
        if nx.is_isomorphic(graph, motif):
            isIsomorphic = True
            break
    return isIsomorphic


# ~ generating subgraph function ~
def generate_subgraphs(n):
    vertices = list(range(1, n+1))
    edges = set(itertools.permutations(vertices, 2)) #all the edges for the full graph
    print(edges)

    motifs = [] #every combination has a potential to be a notif

    for i in range(n-1, n* (n-1) + 1): 
        combinations = list(itertools.combinations(edges, i))
        for combination in combinations:
            if len(combination) == 1:
                combination = [combination[0]]
            graph = nx.DiGraph() #our new sub-graph
            graph.add_nodes_from(vertices)
            graph.add_edges_from(combination)
            if nx.is_weakly_connected(graph):
                if not findIsomorphism(graph, motifs):
                    motifs.append(combination)
    print(len(motifs))
    return motifs


# ~ output text file function ~
def save_subgraphs(motifs, filename):
    with open(filename, 'w') as file:
        file.write(f"n={len(motifs[0])}\n")
        file.write(f"count={len(motifs)}\n")

        for i, subgraph in enumerate(motifs, start=1):
            file.write(f"#{i}\n")

            for j in range(1, i):
                previous_subgraph = motifs[j - 1]
                for node in previous_subgraph:
                    file.write(f"{node} ")
                file.write("\n")

            for node in subgraph:
                file.write(f"{node} ")
            file.write("\n")
# ************************************************************************************


# ************************************ Quastion B ************************************
n = 4
for i in range(1, n+1):
    subgraphs = generate_subgraphs(i)
    txt = 'subgraphs' + str(i)
    save_subgraphs(subgraphs, txt+ '.txt')
# ************************************************************************************


# ************************************ Quastion C ************************************
def run_within_time_limit(time_limit):
    n = 1
    max_n = 4 ####### None

    start_time = time.time()

    while True:
        subgraphs = generate_subgraphs(n)
        elapsed_time = time.time() - start_time
        print(f"elapsed_time: {elapsed_time}")

        if elapsed_time > time_limit:
            break

        max_n = n
        n += 1

    return max_n

# ~ 1 hour computing time ~
# Set the desired time limit in seconds (e.g., 3600 for 1 hour)
time_limit = 3600

# Run the program within the time limit and get the maximum n
max_n = run_within_time_limit(time_limit)

print(f"The maximal value of n within {time_limit} seconds is: {max_n}")
# ************************************************************************************


# # ************************************ Quastion D ************************************
# # ~ 2 hours computing time ~
# # Set the desired time limit in seconds (e.g., 7200 for 2 hour)
# time_limit = 7200
# max_n = run_within_time_limit(time_limit)
# print(f"The maximal value of n within {time_limit} seconds is: {max_n}")


# # ~ 4 hours computing time ~
# # Set the desired time limit in seconds (e.g., 14,400 for 4 hour)
# time_limit = 14400
# max_n = run_within_time_limit(time_limit)
# print(f"The maximal value of n within {time_limit} seconds is: {max_n}")

# # ~ 8 hours computing time ~
# # Set the desired time limit in seconds (e.g., 28,800 for 8 hour)
# time_limit = 14400
# max_n = run_within_time_limit(time_limit)
# print(f"The maximal value of n within {time_limit} seconds is: {max_n}")
# # ************************************************************************************

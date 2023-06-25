import itertools
import networkx as nx
import time



# ************************************ question a ************************************
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
    vertices = list(range(1, n + 1))
    edges = set(itertools.permutations(vertices, 2))  # all the edges for the full graph
    print(edges)

    motifs = []  # every combination has a potential to be a notif

    for i in range(n - 1, n * (n - 1) + 1):
        combinations = list(itertools.combinations(edges, i))
        for combination in combinations:
            if is_time_over():  # Quastion c
                return
            if len(combination) == 1:
                combination = [combination[0]]
            graph = nx.DiGraph()  # our new sub-graph
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


def is_time_over():
    elapsed_time = time.time() - start_time
    if elapsed_time > time_limit:
        return True
    return False


if __name__ == "__main__":
    # ************************************ question b ************************************
    for n in range(1, 5):
        motifs = generate_subgraphs(n)
        filename = f"subgraphs_{n}.txt"
        save_subgraphs(motifs, filename)

    # ************************************ question c ************************************

    # time_limit = 3600  # Time limit in seconds
    # max_n = 1
    # start_time = time.time()
    #
    # while True:
    #     motifs = generate_subgraphs(max_n)
    #     # elapsed_time = time.time() - start_time
    #     if is_time_over():
    #         break
    #     max_n += 1
    #
    # print(f"Max n for under 1 hour: {max_n - 1}")
    # filename = f"max_n_1hour.txt"
    # with open(filename, 'w') as file:
    #     file.write(f"maximal n (1 hour):{max_n - 1}\n")


# ************************************ question d ************************************
    time_limits = [7200, 14400, 28800]  # (2 hours, 4 hours, 8 hours)

    for time_limit in time_limits:
        max_n = 1
        start_time = time.time()

        while True:
            motifs = generate_subgraphs(max_n)
            if is_time_over():
                break
            max_n += 1

        curr_max = max_n - 1

        print(f"Max n for under 1 hour: {curr_max}")
        filename = f"max_n_{time_limit // 3600}hour.txt"
        with open(filename, 'w') as file:
            file.write(f"maximal n ({time_limit // 3600} hour):{curr_max}\n")

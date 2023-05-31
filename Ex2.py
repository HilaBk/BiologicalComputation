# ************************************ Quastion A ************************************
# ~ generating subgraph function ~
def generate_subgraphs(n):
    subgraphs = []

    def generate_subgraph(current_subgraph, remaining_nodes):
        if len(current_subgraph) == n:
            subgraphs.append(list(current_subgraph))
            return

        for node in remaining_nodes:
            if node not in current_subgraph:
                current_subgraph.append(node)
                generate_subgraph(current_subgraph, remaining_nodes)
                current_subgraph.pop()

    generate_subgraph([], list(range(1, n + 1)))

    return subgraphs


# ~ output text file function ~
def save_subgraphs(subgraphs, filename):
    with open(filename, 'w') as file:
        file.write(f"n={len(subgraphs[0])}\n")
        file.write(f"count={len(subgraphs)}\n")

        for i, subgraph in enumerate(subgraphs, start=1):
            file.write(f"#{i}\n")

            for j in range(1, i):
                previous_subgraph = subgraphs[j - 1]
                for node in previous_subgraph:
                    file.write(f"{node} ")
                file.write("\n")

            for node in subgraph:
                file.write(f"{node} ")
            file.write("\n")
# ******************************************************************************************************




# ************************************ Quastion B ************************************
n = 4
for i in range(1, n+1):
    subgraphs = generate_subgraphs(i)
    txt = 'subgraphs' + str(i)
    save_subgraphs(subgraphs, txt+ '.txt')
# ******************************************************************************************************

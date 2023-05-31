import time

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
    max_n = None

    start_time = time.time()

    while True:
        subgraphs = generate_subgraphs(n)
        elapsed_time = time.time() - start_time

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
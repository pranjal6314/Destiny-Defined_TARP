import networkx as nx
import matplotlib.pyplot as plt
import time

# Define a graph with nodes and edges
G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
G.add_edges_from([('A', 'B', {'cost': 1, 'time': 5}),
                  ('A', 'C', {'cost': 3, 'time': 10}),
                  ('B', 'D', {'cost': 2, 'time': 5}),
                  ('C', 'D', {'cost': 1, 'time': 5}),
                  ('C', 'E', {'cost': 2, 'time': 10}),
                  ('D', 'F', {'cost': 3, 'time': 10}),
                  ('E', 'F', {'cost': 2, 'time': 5}),
                  ('F', 'G', {'cost': 3, 'time': 5}),
                  ('F', 'H', {'cost': 4, 'time': 10}),
                  ('G', 'H', {'cost': 2, 'time': 5})])

# Define the start and goal nodes
start = 'A'
goals = ['E', 'F', 'G']

# Define functions to calculate the cost and time of a path
def cost_path(path):
    cost = 0
    for i in range(len(path)-1):
        cost += G[path[i]][path[i+1]]['cost']
    return cost

def time_path(path):
    time = 0
    for i in range(len(path)-1):
        time += G[path[i]][path[i+1]]['time']
    return time

# Define a function to plot the results
def plot_results(algorithms, costs, times):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.bar(algorithms, costs)
    plt.title('Cost of path')
    plt.subplot(1, 2, 2)
    plt.bar(algorithms, times)
    plt.title('Time to find path')
    plt.show()

# Apply the algorithms to find the shortest path to each goal node
algorithms = ['Dynamic Programming', 'Dijkstra', 'Uniform Cost', 'Greedy Search', 'A*']
costs = []
times = []
for algorithm in algorithms:
    start_time = time.time()
    if algorithm == 'Dynamic Programming':
        # Dynamic programming algorithm
        paths = []
        for goal in goals:
            path = nx.bidirectional_dijkstra(G, start, goal)
            paths.append(path[1])
        total_cost = sum([cost_path(path) for path in paths])
    elif algorithm == 'Dijkstra':
        # Dijkstra's algorithm
        paths = []
        for goal in goals:
            path = nx.dijkstra_path(G, start, goal)
            paths.append(path)
        total_cost = sum([cost_path(path) for path in paths])
    elif algorithm == 'Uniform Cost':
        # Uniform cost search
        paths = []
        for goal in goals:
            path = nx.astar_path(G, start, goal, weight='cost')
            paths.append(path)
        total_cost = sum([cost_path(path) for path in paths])
    elif algorithm == 'Greedy Search':
        # Greedy search
        paths = []
        for goal in goals:
            path = nx.astar_path(G, start, goal, heuristic=lambda n, goal: 0, weight='cost')
            paths.append(path)
        total_cost = sum([cost_path(path) for path in paths])
    elif algorithm == 'A*':
        # A* algorithm
        paths = []
        for goal in goals:
            path = nx.astar_path(G, start, goal, weight='cost')
            paths.append(path)
        total_cost = sum([cost_path(path) for path in paths])

end_time = time.time()
costs.append(total_cost)
times.append(end_time - start_time)
plot_results(algorithms, costs, times)

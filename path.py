import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# City and road data
cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}

# Create graph
G = nx.Graph()
for city in roads:
    for connected_city, distance in roads[city]:
        G.add_edge(city, connected_city, weight=distance)

# BFS algorithm to find a path
def bfs(start, goal):
    queue = deque([start])
    parent = {start: None}
    
    while queue:
        current = queue.popleft()
        if current == goal:
            break
        for neighbor in G.neighbors(current):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)
    
    # Reconstruct the path
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]  # Reverse the path to get it from start to goal

# Example: Find a path from 'Addis Ababa' to 'Mekelle'
path = bfs('Addis Ababa', 'Mekelle')

# Plot the graph
pos = nx.spring_layout(G)  # Layout for the nodes
plt.figure(figsize=(8, 6))

# Draw the graph with the road network
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold')

# Highlight the path found
path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

# Draw edge labels (showing the distances)
edge_labels = {(city1, city2): data['weight'] for city1, city2, data in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Show plot
plt.title("Ethiopia Road Network with Path Highlighted")
plt.show()

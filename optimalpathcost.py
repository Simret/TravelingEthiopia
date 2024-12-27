import heapq

# Dijkstra's algorithm to find the shortest path from start to goal
def dijkstra(roads, start_city, goal_city):
    """
    Uses Dijkstra's algorithm to find the shortest path from start_city to goal_city.
    """
    # Priority queue for the open set (city, cumulative_cost)
    pq = [(0, start_city, [])]  # (cost, current_node, path_so_far)
    visited = set()

    while pq:
        cost, current_city, path = heapq.heappop(pq)

        if current_city in visited:
            continue

        visited.add(current_city)
        path = path + [current_city]

        if current_city == goal_city:
            return path, cost

        for neighbor, travel_cost in roads.get(current_city, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + travel_cost, neighbor, path))

    return [], -1  # No path found

# Yen's k-Shortest Paths algorithm
def yen_k_shortest_paths(cities, roads, start_city, goal_city, k):
    """
    Finds the k-shortest paths from start_city to goal_city using Yen's algorithm.
    """
    # The list to store the k-shortest paths
    k_shortest_paths = []

    # Step 1: Find the first shortest path using Dijkstra
    first_path, first_cost = dijkstra(roads, start_city, goal_city)

    if not first_path:
        return k_shortest_paths, -1  # No path found

    k_shortest_paths.append((first_path, first_cost))

    # Step 2: Iteratively find the next shortest paths
    for i in range(1, k):
        # Create a "backup" of the roads graph to modify
        backup_roads = {city: list(connections) for city, connections in roads.items()}

        # Set to track blocked edges/nodes
        blocked_edges = set()

        # Try finding a new path by modifying previous paths
        for j in range(len(k_shortest_paths[i - 1][0]) - 1):
            # Block the previous edge and try finding the next path
            blocked_edges.add((k_shortest_paths[i - 1][0][j], k_shortest_paths[i - 1][0][j + 1]))

            # Temporarily remove the edge from the graph
            roads[k_shortest_paths[i - 1][0][j]] = [
                (neighbor, cost) for neighbor, cost in roads[k_shortest_paths[i - 1][0][j]]
                if (k_shortest_paths[i - 1][0][j], neighbor) not in blocked_edges
            ]

            roads[k_shortest_paths[i - 1][0][j + 1]] = [
                (neighbor, cost) for neighbor, cost in roads[k_shortest_paths[i - 1][0][j + 1]]
                if (neighbor, k_shortest_paths[i - 1][0][j + 1]) not in blocked_edges
            ]

        # Use Dijkstra to find the next shortest path
        path, cost = dijkstra(roads, start_city, goal_city)

        if path:
            k_shortest_paths.append((path, cost))
        else:
            break  # No more paths found

    return k_shortest_paths, len(k_shortest_paths)

# Example usage
cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}

# Find the 3 shortest paths from Addis Ababa to Gondar
k = 3
paths, count = yen_k_shortest_paths(cities, roads, 'Addis Ababa', 'Gondar', k)

# Display results
print(f"Found {count} paths:")
for path, cost in paths:
    print(f"Path: {path}, Cost: {cost}")


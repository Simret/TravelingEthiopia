from collections import deque

def traverse_all_cities(cities, roads, start_city, strategy):
    """
    Parameters:
    - cities: List of city names.
    - roads: Dictionary with city connections as {city: [(connected_city, distance)]}.
    - start_city: The city to start the journey.
    - strategy: The uninformed search strategy to use ('bfs' or 'dfs').

    Returns:
    - path: List of cities representing the traversal path.
    - cost: Total cost (distance) of the traversal.
    """

    # Helper function for BFS (Unweighted graph)
    def bfs_all_cities(start):
        queue = deque([(start, [start], 0)])  # (current_city, path_so_far, cumulative_cost)
        visited = set([start])

        while queue:
            current, path, total_cost = queue.popleft()

            # If all cities are visited, return the path and cost
            if len(path) == len(cities):
                return path, total_cost

            for neighbor, cost in roads.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor], total_cost + cost))

        return [], -1  # If no valid traversal found

    # Helper function for DFS (Depth-First Search)
    def dfs_all_cities(start):
        stack = [(start, [start], 0)]  # (current_city, path_so_far, cumulative_cost)
        visited = set([start])

        while stack:
            current, path, total_cost = stack.pop()

            # If all cities are visited, return the path and cost
            if len(path) == len(cities):
                return path, total_cost

            for neighbor, cost in roads.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor, path + [neighbor], total_cost + cost))

        return [], -1  # If no valid traversal found

    # Select the strategy
    if strategy == 'bfs':
        return bfs_all_cities(start_city)
    elif strategy == 'dfs':
        return dfs_all_cities(start_city)
    else:
        raise ValueError("Strategy must be either 'bfs' or 'dfs'.")

# Example usage
cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}

# Test BFS for traversing all cities
path_bfs_all, cost_bfs_all = traverse_all_cities(cities, roads, 'Addis Ababa', 'bfs')
print(f"BFS Path Visiting All Cities: {path_bfs_all}, Cost: {cost_bfs_all}")

# Test DFS for traversing all cities
path_dfs_all, cost_dfs_all = traverse_all_cities(cities, roads, 'Addis Ababa', 'dfs')
print(f"DFS Path Visiting All Cities: {path_dfs_all}, Cost: {cost_dfs_all}")


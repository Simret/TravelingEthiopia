import heapq

def uninformed_path_finder(cities, roads, start_city, goal_city, strategy):
    """
    Parameters:
    - cities: List of city names.
    - roads: Dictionary with city connections as {city: [(connected_city, distance)]}.
    - start_city: The city to start the journey.
    - goal_city: The destination city (for specific tasks).
    - strategy: The uninformed search strategy to use ('bfs', 'dfs', or 'ucs').

    Returns:
    - path: List of cities representing the path from start_city to goal_city.
    - cost: Total cost (number of steps or distance) of the path.
    """

    # Helper function for BFS (Unweighted graph)
    def bfs(start, goal):
        queue = deque([start])
        visited = set([start])
        parent = {start: None}

        while queue:
            current = queue.popleft()
            if current == goal:
                break
            for neighbor, _ in roads.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)

        # Reconstruct the path
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = parent[node]
        return path[::-1], len(path) - 1  # Return path and number of edges (steps)

    # Helper function for DFS (Depth-First Search)
    def dfs(start, goal):
        stack = [start]
        visited = set([start])
        parent = {start: None}

        while stack:
            current = stack.pop()
            if current == goal:
                break
            for neighbor, _ in roads.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    stack.append(neighbor)

        # Reconstruct the path
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = parent[node]
        return path[::-1], len(path) - 1  # Return path and number of edges (steps)

    # function for Uniform Cost Searc
    def ucs(start, goal):
        # Priority queue to explore nodes by lowest cumulative cost
        pq = [(0, start)]
        visited = set([start])
        parent = {start: None}
        cost_so_far = {start: 0}

        while pq:
            current_cost, current = heapq.heappop(pq)  # Get city with lowest cost

            if current == goal:
                break

            for neighbor, weight in roads.get(current, []):
                new_cost = current_cost + weight

                # Only explore this path if it's cheaper or not yet visited
                if neighbor not in visited or new_cost < cost_so_far.get(neighbor, float('inf')):
                    visited.add(neighbor)
                    parent[neighbor] = current
                    cost_so_far[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor))  # Push to priority queue

        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = parent[node]
        return path[::-1], cost_so_far.get(goal, float('inf'))  # Return path and total cost

    # Select the strategy
    if strategy == 'bfs':
        return bfs(start_city, goal_city)
    elif strategy == 'dfs':
        return dfs(start_city, goal_city)
    elif strategy == 'ucs':
        return ucs(start_city, goal_city)
    else:
        raise ValueError("Strategy must be either 'bfs', 'dfs', or 'ucs'.")

cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}

# Test U
path_ucs, cost_ucs = uninformed_path_finder(cities, roads, 'Addis Ababa', 'Mekelle', 'ucs')
print(f"UCS Path: {path_ucs}, Cost: {cost_ucs}")


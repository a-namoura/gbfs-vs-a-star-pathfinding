import heapq

def a_star_search(start, goal):
    frontier = []
    heapq.heappush(frontier, (h[start], 0, start))  # (f, g, node)
    visited = {}

    while frontier:
        f, g, current = heapq.heappop(frontier)
        print(f"Visiting {current}, g(n)={g}, h(n)={h[current]}, f(n)={f}")

        if current == goal:
            print("Goal Reached!")
            return

        if current in visited and visited[current] <= g:
            continue

        visited[current] = g

        for neighbor, cost in graph.get(current, []):
            new_g = g + cost
            new_f = new_g + h[neighbor]
            heapq.heappush(frontier, (new_f, new_g, neighbor))

# Define the map (distances between cities)
graph = {
    'Arad': [('Sibiu', 140), ('Timisoara', 118), ('Zerind', 75)],
    'Sibiu': [('Fagaras', 99), ('Rimnicu Vilcea', 80)], 
    'Timisoara': [('Lugoj', 111)], 
    'Zerind': [('Oradea', 71)], 
    'Fagaras': [('Bucharest', 211)],
    'Rimnicu Vilcea': [('Pitesti', 97), ('Craiova', 146)],
    'Lugoj': [('Mehadia', 70)],
    'Oradea': [('Sibiu', 151)],
    'Mehadia': [('Drobeta', 75)],
    'Drobeta': [('Craiova', 120)],
    'Craiova': [('Pitesti', 138)],
    'Pitesti': [('Bucharest', 101)],
    'Bucharest': []
}

# h(n) values (straight-line distance to Bucharest)
h = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

# Execute the algorithm
a_star_search('Arad', 'Bucharest')

import heapq

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

def greedy_best_first_search(start, goal):
    frontier = []
    heapq.heappush(frontier, (h[start], start))
    visited = set()

    while frontier:
        _, current = heapq.heappop(frontier)
        print(f"Visiting {current}")

        if current == goal:
            print("Goal Reached!")
            return

        visited.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(frontier, (h[neighbor], neighbor))

# Execute the algorithm
greedy_best_first_search('Arad', 'Bucharest')

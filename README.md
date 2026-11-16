# Greedy Best-First Search vs. A* — Romania Map Pathfinding

A Python project comparing **Greedy Best-First Search (GBFS)** and **A* Search** on a city-to-city route-finding problem. Both algorithms use heuristic estimates to guide their search, but only A* also considers the distance already traveled.

Created for the **Artificial Intelligence Lab at Al-Quds University** (May 9, 2025).

## Project Overview

The task is to search for a route from **Arad** to **Bucharest** using a weighted graph of Romanian cities.

- **Nodes** represent cities.
- **Edges** represent the directed road connections defined in the code.
- **Edge weights** represent road distances in kilometers.
- **Heuristic values**, `h(n)`, estimate the straight-line distance from each city to Bucharest.

The project uses Python's `heapq` module to prioritize which city to explore next. The algorithms run in separate scripts so their search orders can be compared.

## Search Algorithms

### Greedy Best-First Search (GBFS)

GBFS prioritizes whichever frontier node appears closest to the goal according to the heuristic:

```text
f(n) = h(n)
```

It does not include the cost of the route traveled so far. This can lead it to reach the goal quickly through a route that is **not the shortest**.

Implemented in [`gbfs.py`](gbfs.py).

### A* Search

A* combines the actual cost from the starting city with the estimated remaining distance:

```text
f(n) = g(n) + h(n)
```

Where:

- `g(n)` is the accumulated road distance from the start.
- `h(n)` is the estimated distance to the goal.
- `f(n)` is the estimated total cost of a route through node `n`.

The provided implementation uses a priority queue and tracks the lowest processed `g(n)` value for each city. With suitable conditions, including an admissible heuristic, A* can find a lowest-cost path.

Implemented in [`a_star_search.py`](a_star_search.py).

## Getting Started

### Requirements

- Python 3

No external libraries are required; both scripts use Python's built-in `heapq` module.

### Installation

```bash
git clone https://github.com/a-namoura/gbfs-vs-a-star-pathfinding.git
cd gbfs-vs-a-star-pathfinding
```

### Run Greedy Best-First Search

```bash
python3 gbfs.py
```

### Run A* Search

```bash
python3 a_star_search.py
```

On Windows, use `python` instead of `python3` if needed.

Each script runs the Arad-to-Bucharest example immediately; no input files or command-line arguments are required.

## Results

For the included graph and heuristic values, the routes identified by the search are:

| Algorithm | Route | Total distance |
| --- | --- | ---: |
| Greedy Best-First Search | Arad → Sibiu → Fagaras → Bucharest | **450 km** |
| A* Search | Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest | **418 km** |

A* finds a route that is **32 km shorter** in this example.

### Greedy Best-First Search Output

```text
Visiting Arad
Visiting Sibiu
Visiting Fagaras
Visiting Bucharest
Goal Reached!
```

### A* Search Output

```text
Visiting Arad, g(n)=0, h(n)=366, f(n)=366
Visiting Sibiu, g(n)=140, h(n)=253, f(n)=393
Visiting Rimnicu Vilcea, g(n)=220, h(n)=193, f(n)=413
Visiting Fagaras, g(n)=239, h(n)=176, f(n)=415
Visiting Pitesti, g(n)=317, h(n)=100, f(n)=417
Visiting Bucharest, g(n)=418, h(n)=0, f(n)=418
Goal Reached!
```

**Important:** These scripts print the **order in which nodes are visited**, not a reconstructed final path. For instance, A* also visits Fagaras even though the shorter final route goes through Pitesti. The route and total-distance table above is derived from the graph and the verified search results; the code does not currently print full paths or total distances automatically.

## Algorithm Comparison

| Aspect | Greedy Best-First Search | A* Search |
| --- | --- | --- |
| Priority function | `h(n)` | `g(n) + h(n)` |
| Uses traveled distance? | No | Yes |
| Uses a heuristic? | Yes | Yes |
| Finds the shortest path in this example? | No | Yes |
| Generally guarantees optimality? | No | Under appropriate graph and heuristic assumptions |
| Observed result | 450 km | 418 km |

The comparison illustrates how considering both **distance traveled** and **estimated distance remaining** can improve route quality. It is not a runtime or memory benchmark: the current scripts do not measure execution time, memory usage, or numbers of unique expanded nodes.

## Customizing the Example

Edit the following definitions in either Python script:

- `graph` — city connections and their road distances.
- `h` — estimated remaining distance from each city to Bucharest.
- The final function call — the starting and goal cities.

For meaningful A* comparisons, ensure your heuristic estimates apply to the **chosen goal**. If you change the destination, update `h` accordingly. Add any new cities to the appropriate data structures.

The example currently uses hard-coded graph data and a directed adjacency list; it is not an interactive map application.

## Repository Structure

| File | Description |
| --- | --- |
| [`gbfs.py`](gbfs.py) | Greedy Best-First Search implementation and console trace. |
| [`a_star_search.py`](a_star_search.py) | A* Search implementation with `g(n)`, `h(n)`, and `f(n)` output. |
| [`Search Using Greedy Best-First Search and A Search.pdf`](Search%20Using%20Greedy%20Best-First%20Search%20and%20A%20Search.pdf) | Accompanying lab report and discussion. |
| `README.md` | Project documentation and usage instructions. |

## Educational Scope

This project demonstrates **informed search**, **priority queues**, **heuristic evaluation**, and the trade-off between heuristic-only and cost-aware pathfinding. It is a small educational example, not a general-purpose route planner.

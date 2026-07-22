import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [],
    'G': []
}

start = 'A'
goal = 'G'

pq = [(0, start)]
visited = set()

print("UCS Traversal:")

while pq:
    cost, node = heapq.heappop(pq)
    print(node, "with cost", cost)

    if node == goal:
        print("\nGoal Reached")
        print("Total Cost =", cost)
        break

    if node not in visited:
        visited.add(node)
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + edge_cost, neighbor))

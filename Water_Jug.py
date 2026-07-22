from collections import deque

jug1, jug2, target = 4, 3, 2
visited = set()
queue = deque([(0, 0)])

visited.add((0, 0))

print("Water Jug Steps:")
while queue:
    x, y = queue.popleft()
    print((x, y))

    if x == target or y == target:
        print("Target Reached")
        break

    states = [
        (jug1, y),        # Fill jug1
        (x, jug2),        # Fill jug2
        (0, y),           # Empty jug1
        (x, 0),           # Empty jug2
        (x - min(x, jug2 - y), y + min(x, jug2 - y)),  # Pour jug1 → jug2
        (x + min(y, jug1 - x), y - min(y, jug1 - x))   # Pour jug2 → jug1
    ]

    for state in states:
        if state not in visited:
            visited.add(state)
            queue.append(state)

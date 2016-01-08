from collections import deque

GRAPH = {
    "1": ["3"],
    "2": ["3", "4"],
    "3": ["1", "2", "4"],
    "4": ["2", "3", "5"],
    "5": ["4", "6", "7"],
    "6": ["5"],
    "7": ["5"]
}


def bfs(start_node):
    visited = []
    queue = deque()

    visited.append(start_node)
    queue.append(start_node)

    while len(queue) != 0:
        node = queue.popleft()

        for neighbour in GRAPH[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    return visited


def bfs_with_level(start_node, end_node):
    visited = set()
    queue = deque()

    visited.add(start_node)
    queue.append((0, start_node))

    while len(queue) != 0:
        node_with_level = queue.popleft()
        node = node_with_level[1]
        level = node_with_level[0]

        if node == end_node:
            return level

        for neighbour in GRAPH[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((level + 1, neighbour))

    return -1

# Implement BFS (Breath First Search) and DFS (Depth First Search)

from collections import deque
def bfs(graph, start):
  visited = set()
  queue = deque([start])
  while queue:
    node = queue.popleft()
    if node not in visited:
      visited.add(node)
      for neighbor in graph[node]:
        queue.append(neighbor)
  return visited
def dfs(graph, start):
  visited = set()
  stack = [start]
  while stack:
    node = stack.pop()
    if node not in visited:
      visited.add(node)
      for neighbor in graph[node]:
        stack.append(neighbor)
  return visited
if __name__ == "__main__":
  graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
  }
  print(bfs(graph, 'A'))
  print(dfs(graph, 'A'))
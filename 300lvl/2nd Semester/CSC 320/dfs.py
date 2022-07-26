# undirected graph
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs(graph, start):
    visited, stack = [], [start] 
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(graph[vertex] - set(visited)) 
    return visited

dfs(graph, 'A') # ['A', 'B', 'E', 'F', 'C', 'D'] # Correct output

def dfs(graph, start, visited=[]): 
    visited.append(start)
    for next in graph[start] - set(visited): 
        dfs(graph, next, visited)
    return visited

dfs(graph, 'C') # ['C', 'F', 'E', 'B', 'A', 'D', 'A']

# We are able to tweak both of the previous implementations to return all possible paths between a start and goal vertex.
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))
            
list(dfs_paths(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]       


def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])

list(dfs_paths(graph, 'C', 'F')) # [['C', 'F'], ['C', 'A', 'B', 'E', 'F']]
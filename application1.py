# Build the bipartite graph from the enrollment pairs
enrollments = [
    ("Sita",  "Math"),
    ("Sita",  "CS"),
    ("Rahul", "Math"),
    ("Rahul", "Econ"),
    ("Meera", "CS"),
    ("Meera", "Stats"),
    ("Arjun", "Stats"),
    ("Arjun", "AI"),
    ("Kavya", "Econ"),
    ("Kavya", "AI"),
    ("Vivek", "CS"),
    ("Vivek", "Econ"),
]

# Undirected adjacency list
graph = {}
for s, c in enrollments:
    graph.setdefault(s, []).append(c)
    graph.setdefault(c, []).append(s)

from collections import deque

def is_bipartite_bfs(G):
    color = {}
    for start in G:
        if start not in color:
            color[start] = 0
            q = deque([start])
            while q:
                u = q.popleft()
                for v in G[u]:
                    if v not in color:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        return False, None
    return True, color

def is_bipartite_dfs(G):
    color = {}
    def dfs(u, c):
        color[u] = c
        for v in G[u]:
            if v not in color:
                if not dfs(v, 1 - c):
                    return False
            elif color[v] == c:
                return False
        return True

    for start in G:
        if start not in color:
            if not dfs(start, 0):
                return False, None
    return True, color

b_ok, b_col = is_bipartite_bfs(graph)
d_ok, d_col = is_bipartite_dfs(graph)

print("BFS check result:", b_ok)
print("DFS check result:", d_ok)

# Derive one bipartition from BFS coloring (if bipartite)
if b_ok:
    A = sorted([v for v,c in b_col.items() if c == 0])
    B = sorted([v for v,c in b_col.items() if c == 1])
    print("One valid bipartition (from BFS coloring):")
    print("A =", A)
    print("B =", B)
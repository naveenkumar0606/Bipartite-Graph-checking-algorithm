# Build the bipartite graph from the enrollment pairs (100 entries)
enrollments = [
    ("Sita", "Math"), ("Sita", "CS"), ("Sita", "Stats"),
    ("Rahul", "Math"), ("Rahul", "Econ"), ("Rahul", "AI"),
    ("Meera", "CS"), ("Meera", "Stats"), ("Meera", "AI"),
    ("Arjun", "Stats"), ("Arjun", "AI"), ("Arjun", "CS"),
    ("Kavya", "Econ"), ("Kavya", "AI"), ("Kavya", "Math"),
    ("Vivek", "CS"), ("Vivek", "Econ"), ("Vivek", "Stats"),
    ("Neha", "Math"), ("Neha", "CS"), ("Neha", "AI"),
    ("Rohit", "Econ"), ("Rohit", "Stats"), ("Rohit", "CS"),
    ("Ananya", "AI"), ("Ananya", "Math"), ("Ananya", "Econ"),
    ("Aditya", "Stats"), ("Aditya", "CS"), ("Aditya", "AI"),
    ("Priya", "Math"), ("Priya", "Stats"), ("Priya", "Econ"),
    ("Karan", "CS"), ("Karan", "AI"), ("Karan", "Stats"),
    ("Isha", "Math"), ("Isha", "CS"), ("Isha", "Econ"),
    ("Dev", "Stats"), ("Dev", "AI"), ("Dev", "Math"),
    ("Tanya", "CS"), ("Tanya", "Econ"), ("Tanya", "Stats"),
    ("Sameer", "AI"), ("Sameer", "Math"), ("Sameer", "CS"),
    ("Riya", "Stats"), ("Riya", "Econ"), ("Riya", "AI"),
    ("Varun", "Math"), ("Varun", "CS"), ("Varun", "Stats"),
    ("Diya", "Econ"), ("Diya", "AI"), ("Diya", "Math"),
    ("Aarav", "CS"), ("Aarav", "Stats"), ("Aarav", "Econ"),
    ("Maya", "AI"), ("Maya", "Math"), ("Maya", "CS"),
    ("Nikhil", "Stats"), ("Nikhil", "Econ"), ("Nikhil", "AI"),
    ("Anika", "Math"), ("Anika", "CS"), ("Anika", "Stats"),
    ("Rohan", "Econ"), ("Rohan", "AI"), ("Rohan", "Math"),
    ("Sanya", "CS"), ("Sanya", "Stats"), ("Sanya", "Econ"),
    ("Kabir", "AI"), ("Kabir", "Math"), ("Kabir", "CS"),
    ("Aditi", "Stats"), ("Aditi", "Econ"), ("Aditi", "AI"),
    ("Shiv", "Math"), ("Shiv", "CS"), ("Shiv", "Stats"),
    ("Pooja", "Econ"), ("Pooja", "AI"), ("Pooja", "Math"),
    ("Manav", "CS"), ("Manav", "Stats"), ("Manav", "Econ"),
    ("Ira", "AI"), ("Ira", "Math"), ("Ira", "CS"),
    ("Rhea", "Math"), ("Rhea", "CS"), ("Rhea", "Stats"),
    ("Vikram", "Math"), ("Vikram", "CS"), ("Vikram", "Econ"),
    ("Tara", "Stats"), ("Tara", "AI"), ("Tara", "CS"),
    ("Neil", "AI"), ("Neil", "Econ"), ("Neil", "Stats"),
    ("Naveen", "AI"), ("Naveen", "Math"), ("Naveen", "CS")
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

from collections import deque, defaultdict

def is_bipartite_bfs(adj):
    """
    adj: dict[node] -> list[node], undirected incompatibility graph
    Returns (ok, color) where color[v] in {0,1} if ok else partial coloring.
    """
    color = {}
    for s in adj.keys():
        if s in color:
            continue
        color[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if w not in color:
                    color[w] = 1 - color[u]
                    q.append(w)
                elif color[w] == color[u]:
                    return False, color
    return True, color

def partition_workers(adj):
    ok, color = is_bipartite_bfs(adj)
    if not ok:
        return False, None, None
    A = [v for v,c in color.items() if c == 0]
    B = [v for v,c in color.items() if c == 1]
    return True, A, B

# Example: build incompatibility graph and partition
workers = ['A','B','C','D','E','F','G','H']
edges = [('A','D'),('A','F'),('B','D'),('B','E'),('C','E'),('C','G'),('D','H'),('E','H'),('F','G')]
adj = defaultdict(list)
for u,v in edges:
    adj[u].append(v); adj[v].append(u)

ok, A, B = partition_workers(adj)
print("Bipartite:", ok)
print("Team A:", A)
print("Team B:", B)
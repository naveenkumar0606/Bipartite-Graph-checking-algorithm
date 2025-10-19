from collections import deque, defaultdict

def is_bipartite_bfs(adj):
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

# 100 workers with line breaks every 8 names
workers = [
    'Alice','Bob','Charlie','David','Emma','Frank','Grace','Henry',
    'Irene','Jack','Karen','Leo','Maya','Nathan','Olivia','Peter',
    'Quinn','Rachel','Sam','Tina','Uma','Victor','Wendy','Xavier',
    'Yara','Zach','Aaron','Bella','Caleb','Diana','Ethan','Fiona',
    'George','Hannah','Ian','Julia','Kyle','Laura','Michael','Nina',
    'Oscar','Paula','Quentin','Rebecca','Simon','Teresa','Ulysses','Vanessa',
    'William','Xena','Yusuf','Zoe','Adrian','Bianca','Connor','Danielle',
    'Elijah','Faith','Gavin','Holly','Isaac','Jasmine','Kevin','Lily',
    'Mason','Natalie','Owen','Penelope','Ryan','Sophia','Tyler','Ursula',
    'Vincent','Whitney','Xavier2','Yasmin','Zachary','Amelia','Brandon',
    'Chloe','Dominic','Ella','Finn','Gabriella','Hunter','Isabella','Jacob',
    'Kaitlyn','Liam','Madison','Noah','Ophelia','Parker','Quinn2','Riley','Stella',
    'Thomas','Una','Victor2','Willow'
]
# Edges broken after every 3 tuples
edges = [
    ('Alice','Yusuf'), ('Alice','Zoe'), ('Bob','Adrian'),
    ('Bob','Bianca'), ('Charlie','Connor'), ('Charlie','Danielle'),
    ('David','Elijah'), ('David','Faith'), ('Emma','Gavin'),
    ('Emma','Holly'), ('Frank','Isaac'), ('Frank','Jasmine'),
    ('Grace','Kevin'), ('Grace','Lily'), ('Henry','Mason'),
    ('Henry','Natalie'), ('Irene','Owen'), ('Irene','Penelope'),
    ('Jack','Ryan'), ('Jack','Sophia'), ('Karen','Tyler'),
    ('Karen','Ursula'), ('Leo','Vincent'), ('Leo','Whitney'),
    ('Maya','Xavier2'), ('Maya','Yasmin'), ('Nathan','Zachary'),
    ('Nathan','Amelia'), ('Olivia','Brandon'), ('Olivia','Chloe'),
    ('Peter','Dominic'), ('Peter','Ella'), ('Quinn','Finn'),
    ('Quinn','Gabriella'), ('Rachel','Hunter'), ('Rachel','Isabella'),
    ('Sam','Jacob'), ('Sam','Kaitlyn'), ('Tina','Liam'),
    ('Tina','Madison'), ('Uma','Noah'), ('Uma','Ophelia'),
    ('Victor','Parker'), ('Victor','Quinn2'), ('Wendy','Riley'),
    ('Wendy','Stella'), ('Xavier','Thomas'), ('Xavier','Una'),
    ('Yara','Victor2'), ('Yara','Willow')
]

# Build adjacency list
adj = defaultdict(list)
for u,v in edges:
    adj[u].append(v)
    adj[v].append(u)

# Check bipartiteness
ok, A, B = partition_workers(adj)
print("Bipartite:", ok)
print("Team A:", A)
print("Team B:", B)

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
# List of all 100 workers
workers = [
    'Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry',
    'Irene', 'Jack', 'Karen', 'Leo', 'Maya', 'Nathan', 'Olivia', 'Peter',
    'Quinn', 'Rachel', 'Sam', 'Tina', 'Uma', 'Victor', 'Wendy', 'Xavier',
    'Yara', 'Zach', 'Aaron', 'Bella', 'Caleb', 'Diana', 'Ethan', 'Fiona',
    'George', 'Hannah', 'Ian', 'Julia', 'Kyle', 'Laura', 'Michael', 'Nina',
    'Oscar', 'Paula', 'Quentin', 'Rebecca', 'Simon', 'Teresa', 'Ulysses',
    'Vanessa', 'William', 'Xena', 'Yusuf', 'Zoe', 'Adrian', 'Bianca',
    'Connor', 'Danielle', 'Elijah', 'Faith', 'Gavin', 'Holly', 'Isaac',
    'Jasmine', 'Kevin', 'Lily', 'Mason', 'Natalie', 'Owen', 'Penelope',
    'Ryan', 'Sophia', 'Tyler', 'Ursula', 'Vincent', 'Whitney', 'Xavier2',
    'Yasmin', 'Zachary', 'Amelia', 'Brandon', 'Chloe', 'Dominic', 'Ella',
    'Finn', 'Gabriella', 'Hunter', 'Isabella', 'Jacob', 'Kaitlyn', 'Liam',
    'Madison', 'Noah', 'Ophelia', 'Parker', 'Quinn2', 'Riley', 'Stella',
    'Thomas', 'Una', 'Victor2', 'Willow', 'Xander', 'Yvonne', 'Zach3',
    'Avery', 'Brooke', 'Carter', 'Delilah', 'Everett', 'Freya', 'Grayson',
    'Harper'
]
# List of incompatibility pairs (edges)
edges = [
    ('Alice','David'), ('Alice','Frank'), ('Bob','Emma'),
    ('Bob','David'), ('Charlie','Grace'), ('Charlie','Emma'),
    ('David','Henry'), ('Emma','Henry'), ('Frank','Grace'),
    ('Frank','Isabella'), ('Grace','Jack'), ('Henry','Karen'),
    ('Irene','Leo'), ('Jack','Maya'), ('Karen','Nathan'),
    ('Leo','Olivia'), ('Maya','Peter'), ('Nathan','Quinn'),
    ('Olivia','Rachel'), ('Peter','Sam'), ('Quinn','Tina'),
    ('Rachel','Uma'), ('Sam','Victor'), ('Tina','Wendy'),
    ('Uma','Xavier'), ('Victor','Yara'), ('Wendy','Zach'),
    ('Xavier','Aaron'), ('Yara','Bella'), ('Zach','Caleb'),
    ('Aaron','Diana'), ('Bella','Ethan'), ('Caleb','Fiona'),
    ('Diana','George'), ('Ethan','Hannah'), ('Fiona','Ian'),
    ('George','Julia'), ('Hannah','Kyle'), ('Ian','Laura'),
    ('Julia','Michael'), ('Kyle','Nina'), ('Laura','Oscar'),
    ('Michael','Paula'), ('Nina','Quentin'), ('Oscar','Rebecca'),
    ('Paula','Simon'), ('Quentin','Teresa'), ('Rebecca','Ulysses'),
    ('Simon','Vanessa'), ('Teresa','William'), ('Ulysses','Xena'),
    ('Vanessa','Yusuf'), ('William','Zoe'), ('Xena','Adrian'),
    ('Yusuf','Bianca'), ('Zoe','Connor'), ('Adrian','Danielle'),
    ('Bianca','Elijah'), ('Connor','Faith'), ('Danielle','Gavin'),
    ('Elijah','Holly'), ('Faith','Isaac'), ('Gavin','Jasmine'),
    ('Holly','Kevin'), ('Isaac','Lily'), ('Jasmine','Mason'),
    ('Kevin','Natalie'), ('Lily','Owen'), ('Mason','Penelope'),
    ('Natalie','Ryan'), ('Owen','Sophia'), ('Penelope','Tyler'),
    ('Ryan','Ursula'), ('Sophia','Vincent'), ('Tyler','Whitney'),
    ('Ursula','Xavier2'), ('Vincent','Yasmin'), ('Whitney','Zachary'),
    ('Xavier2','Amelia'), ('Yasmin','Brandon'), ('Zachary','Chloe'),
    ('Amelia','Dominic'), ('Brandon','Ella'), ('Chloe','Finn'),
    ('Dominic','Gabriella'), ('Ella','Hunter'), ('Finn','Isabella'),
    ('Gabriella','Jacob'), ('Hunter','Kaitlyn'), ('Isabella','Liam'),
    ('Jacob','Madison'), ('Kaitlyn','Noah'), ('Liam','Ophelia'),
    ('Madison','Parker'), ('Noah','Quinn2'), ('Ophelia','Riley'),
    ('Parker','Stella'), ('Quinn2','Thomas'), ('Riley','Una'),
    ('Stella','Victor2'), ('Thomas','Willow'), ('Una','Xander'),
    ('Victor2','Yvonne'), ('Willow','Zach3'), ('Xander','Avery'),
    ('Yvonne','Brooke'), ('Zach3','Carter'), ('Avery','Delilah'),
    ('Brooke','Everett'), ('Carter','Freya'), ('Delilah','Grayson'),
    ('Everett','Harper')
]
adj = defaultdict(list)
for u,v in edges:
    adj[u].append(v); adj[v].append(u)

ok, A, B = partition_workers(adj)
print("Bipartite:", ok)
print("Team A:", A)
print("Team B:", B)

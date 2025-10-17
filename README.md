# Bipartite Graph Applications

This repository contains two Python scripts demonstrating how to check whether a graph is **bipartite** using BFS and DFS, and how to **partition nodes** into two disjoint sets if it is bipartite.

---

## Files

- **application1.py** — Builds a bipartite graph from student–course enrollments and checks bipartiteness using both BFS and DFS.
- **application2.py** — Builds an incompatibility graph among workers and partitions them into two compatible teams.

---

## Requirements

These scripts use only Python's **standard library** — no external dependencies are required.

---

## How to Run

### 1. Run the student–course bipartite check
```bash
python3 application1.py
```

**Expected Output Example:**
```
BFS check result: True
DFS check result: True
One valid bipartition (from BFS coloring):
A = ['Arjun', 'Kavya', 'Meera', 'Rahul', 'Sita', 'Vivek']
B = ['AI', 'CS', 'Econ', 'Math', 'Stats']
```

This shows that the graph is bipartite, with the left partition containing students and the right partition containing courses.

---

### 2. Run the worker incompatibility partition
```bash
python3 application2.py
```

**Expected Output Example:**
```
Bipartite: True
Team A: ['A', 'B', 'C', 'H']
Team B: ['D', 'E', 'F', 'G']
```

This demonstrates that the incompatibility graph can be split into two teams where no two incompatible workers are in the same team.

---

## Notes

- Tested with **Python 3.8+**
- You can modify the edges or enrollment pairs directly in each file to test other examples.

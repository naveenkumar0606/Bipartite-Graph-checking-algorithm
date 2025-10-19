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
A = [`Aarav', `Aditya', `Aditi', `Ananya', `Anika', `Dev', `Diya', `Ira',
`Isha', `Karan', `Kabir', `Kavya', `Manav', `Maya', `Meera', `Neha',
`Naveen', `Priya', `Rhea', `Riya', `Rohan', `Rohit', `Sameer', `Shiv',
`Sanya', `Sita', `Tara', `Varun', `Vikram', `Vivek']
B = [`AI', `CS', `Econ', `Math', `Stats']
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
Team A: [`Alice`, `Charlie`, `David`, `Frank`, `Grace`, `Irene`, `Jack`, 
`Leo`, `Maya`, `Nathan`, `Olivia`, `Peter`, `Quinn`, `Rachel`, `Sam`, `
Tina`, `Uma`, `Victor`, `Wendy`, `Xavier`, `Yara`, `Zach`, `Aaron`, `Bella`,
`Caleb`, `Diana`, `Ethan`, `Fiona`, `George`, `Hannah`, `Ian`, `Julia`,
`Kyle`, `Laura`, `Michael`, `Nina`, `Oscar`, `Paula`, `Quentin`, `Rebecca`,
`Simon`, `Teresa`, `Ulysses`, `Vanessa`, `William`, `Xena`, `Yusuf`, 
`Zoe`, `Adrian`, `Bianca`, `Connor`, `Danielle`, `Elijah`, `Faith`, `Gavin`, 
`Holly`, `Isaac`, `Jasmine`, `Kevin`, `Lily`, `Mason`, `Natalie`, `Owen`, 
`Penelope`, `Ryan`, `Sophia`, `Tyler`, `Ursula`, `Vincent`, `Whitney`,
`Xavier2`, `Yasmin`, `Zachary`, `Amelia`, `Brandon`, `Chloe`, `Dominic`,
`Ella`, `Finn`, `Gabriella`, `Hunter`, `Isabella`, `Jacob`, `Kaitlyn`,
`Liam`, `Madison`, `Noah`, `Ophelia`, `Parker`, `Quinn2`, `Riley`, `Stella`,
`Thomas`, `Una`, `Victor2`, `Willow`, `Xander`, `Yvonne`, `Zach3`, `Avery`, 
`Brooke`, `Carter`, `Delilah`, `Everett`, `Freya`, `Grayson`, `Harper`]

Team B: [`David`, `Emma`, `Isabella`, `Karen`, `Peter`, `Quinn`, `Tina`,
`Victor`, `Xavier`, `Bella`, `Caleb`, `Diana`, `Ethan`, `Fiona`, `George`,
`Hannah`, `Ian`, `Julia`, `Kyle`, `Laura`, `Michael`, `Nina`, `Oscar`,
`Paula`, `Quentin`, `Rebecca`, `Simon`, `Teresa`, `Ulysses`, `Vanessa`,
`William`, `Xena`, `Yusuf`, `Zoe`, `Adrian`, `Connor`, `Danielle`, `Elijah`,
`Faith`, `Gavin`, `Holly`, `Isaac`, `Jasmine`, `Kevin`, `Lily`, `Mason`, 
`Natalie`, `Owen`, `Penelope`, `Ryan`, `Sophia`, `Tyler`, `Ursula`, `Vincent`,
`Whitney`, `Xavier2`, `Yasmin`, `Zachary`, `Amelia`, `Brandon`, `Chloe`,
`Dominic`, `Ella`, `Finn`, `Gabriella`, `Hunter`, `Jacob`, `Kaitlyn`,
`Liam`, `Madison`, `Noah`, `Ophelia`, `Parker`, `Quinn2`, `Riley`, `Stella`,
`Thomas`, `Una`, `Victor2`, `Willow`, `Xander`, `Yvonne`, `Zach3`, `Avery`, 
`Brooke`, `Carter`, `Delilah`, `Everett`, `Freya`, `Grayson`, `Harper`]
```

This demonstrates that the incompatibility graph can be split into two teams where no two incompatible workers are in the same team.

---

## Notes

- Tested with **Python 3.8+**
- You can modify the edges or enrollment pairs directly in each file to test other examples.

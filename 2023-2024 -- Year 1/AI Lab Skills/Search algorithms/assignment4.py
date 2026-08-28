#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Artificial Intelligence Lab Skills
Assignment 4 Search

Author(s): Angelina Podolako
Group: 119
Contributor(s): 
Average hours spent per person: (Friday = 2h) + (Sat = 2h) + (Mon = 10-22)
"""
import graph
from search import breadth_first_search as BFS
from search import depth_first_search as DFS
from search import uniform_cost_search as UCS

# Create a graph
graph1 = graph.Graph()

# Add vertices with names from "A" to "G"
for i in range(ord("A"), ord("G") + 1):
  graph.vertex_name = chr(i)
  graph1.add_vertex(graph.vertex_name)

# Add edges
graph1.add_edge("A", "B", cost=2)
graph1.add_edge("A", "C", cost=1)
graph1.add_edge("A", "D", cost=1)
graph1.add_edge("A", "G", cost=6)
graph1.add_edge("C", "E", cost=1)
graph1.add_edge("G", "F", cost=3)
graph1.add_edge("D", "F", cost=1)

# Display the graph
print(graph1)


# -BFS Breadth-First Search--------------------------------------------------
print("\n"+("--"*20))  #Separate code sections for clarity

BFS1 = BFS(graph1, "B", "G") # Execute breadth-first search
print(BFS1) 


# -DFS Depth-First Search----------------------------------------------------
print("\n"+("--"*20))  #Separate code sections for clarity

DFS1 = DFS(graph1, "B", "G") # Execute depth-first search
print(DFS1)


# -UCS  Uniform Cost Search -------------------------------------------------
print("\n"+("--"*20))  #Separate code sections for clarity

UCS1 = UCS(graph1, "B", "G")  # Execute uniform cost search
print(UCS1)
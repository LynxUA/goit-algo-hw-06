import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

eu_capitals = [
    "Vienna", "Brussels", "Sofia", "Zagreb", "Nicosia", "Prague", "Copenhagen",
    "Tallinn", "Helsinki", "Paris", "Berlin", "Athens", "Budapest", "Dublin",
    "Rome", "Riga", "Vilnius", "Luxembourg", "Valletta", "Amsterdam", "Warsaw",
    "Lisbon", "Bucharest", "Bratislava", "Ljubljana", "Madrid", "Stockholm"
]

weighted_roads = [
    ("Vienna", "Bratislava", 80), ("Vienna", "Budapest", 243), ("Vienna", "Prague", 333),
    ("Brussels", "Amsterdam", 210), ("Brussels", "Paris", 320), ("Brussels", "Luxembourg", 190),
    ("Sofia", "Bucharest", 350), ("Sofia", "Athens", 500), ("Zagreb", "Ljubljana", 143),
    ("Zagreb", "Budapest", 345), ("Nicosia", "Athens", 1000), ("Prague", "Berlin", 280),
    ("Prague", "Bratislava", 290), ("Copenhagen", "Berlin", 420), ("Tallinn", "Riga", 300),
    ("Helsinki", "Tallinn", 82), ("Paris", "Luxembourg", 350), ("Paris", "Berlin", 1050),
    ("Berlin", "Warsaw", 573), ("Athens", "Rome", 1050), ("Budapest", "Bucharest", 600),
    ("Dublin", "London", 464), ("Rome", "Valletta", 700), ("Rome", "Ljubljana", 740),
    ("Riga", "Vilnius", 270), ("Vilnius", "Warsaw", 450), ("Luxembourg", "Brussels", 190),
    ("Amsterdam", "Berlin", 650), ("Warsaw", "Vilnius", 450), ("Lisbon", "Madrid", 600),
    ("Bucharest", "Budapest", 600), ("Bratislava", "Vienna", 80), ("Ljubljana", "Budapest", 345),
    ("Madrid", "Lisbon", 600), ("Stockholm", "Copenhagen", 522), ("Paris", "Madrid", 1050)
]

G = nx.Graph()
G.add_nodes_from(eu_capitals)
for road in weighted_roads:
    G.add_edge(road[0], road[1], weight=road[2])

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, params in graph[current_vertex].items():
            distance = distances[current_vertex] + params['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances


shortest_paths = {}
for capital in eu_capitals:
    shortest_paths[capital] = dijkstra(G, capital)

print("Shortest paths between all pairs of EU capitals:")
for start, paths in shortest_paths.items():
    for end, distance in paths.items():
        print(f"Shortest path from {start} to {end}: {distance} km")
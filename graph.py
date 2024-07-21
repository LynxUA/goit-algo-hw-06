import networkx as nx

eu_capitals = [
    "Vienna", "Brussels", "Sofia", "Zagreb", "Nicosia", "Prague", "Copenhagen",
    "Tallinn", "Helsinki", "Paris", "Berlin", "Athens", "Budapest", "Dublin",
    "Rome", "Riga", "Vilnius", "Luxembourg", "Valletta", "Amsterdam", "Warsaw",
    "Lisbon", "Bucharest", "Bratislava", "Ljubljana", "Madrid", "Stockholm"
]

roads = [
    ("Vienna", "Bratislava"), ("Vienna", "Budapest"), ("Vienna", "Prague"), ("Brussels", "Amsterdam"),
    ("Brussels", "Paris"), ("Brussels", "Luxembourg"), ("Sofia", "Bucharest"), ("Sofia", "Athens"),
    ("Zagreb", "Ljubljana"), ("Zagreb", "Budapest"), ("Nicosia", "Athens"), ("Prague", "Berlin"),
    ("Prague", "Bratislava"), ("Copenhagen", "Berlin"), ("Tallinn", "Riga"), ("Helsinki", "Tallinn"),
    ("Paris", "Luxembourg"), ("Paris", "Berlin"), ("Berlin", "Warsaw"), ("Athens", "Rome"),
    ("Budapest", "Bucharest"), ("Dublin", "London"), ("Rome", "Valletta"), ("Rome", "Ljubljana"),
    ("Riga", "Vilnius"), ("Vilnius", "Warsaw"), ("Luxembourg", "Brussels"), ("Amsterdam", "Berlin"),
    ("Warsaw", "Vilnius"), ("Lisbon", "Madrid"), ("Bucharest", "Budapest"), ("Bratislava", "Vienna"),
    ("Ljubljana", "Budapest"), ("Madrid", "Lisbon"), ("Stockholm", "Copenhagen"), ("Madrid", "Paris")
]

G = nx.Graph()
G.add_nodes_from(eu_capitals)
G.add_edges_from(roads)
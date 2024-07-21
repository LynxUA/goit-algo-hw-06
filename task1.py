import graph
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

G = graph.G
num_vertices = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_of_vertices = dict(G.degree())

plt.figure(figsize=(15, 10))
pos = nx.spring_layout(G, seed=42)  # positions for all nodes
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')
nx.draw_networkx_edges(G, pos, width=2)
nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")

plt.title("Roads Between EU Capitals")
plt.show()

print(f"Number of vertices: {num_vertices}")
print(f"Number of edges: {num_edges}")
print("Degree of vertices:")
for capital, degree in degree_of_vertices.items():
    print(f"{capital}: {degree}")

analysis_results = {
    "Capital": list(degree_of_vertices.keys()),
    "Degree": list(degree_of_vertices.values())
}
analysis_df = pd.DataFrame(analysis_results)
print("\nAnalysis DataFrame:")
print(analysis_df)

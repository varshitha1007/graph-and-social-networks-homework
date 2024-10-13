# Import necessary libraries
import networkx as nx
import gzip

# Function to read the graph from the .gz file
def load_graph_from_gz(file_path):
    G = nx.Graph()
    with gzip.open(file_path, 'rt') as f:
        for line in f:
            node1, node2 = map(int, line.strip().split())
            G.add_edge(node1, node2)
    return G

# Load the Facebook graph
file_path = 'facebook_combined.txt.gz'
G = load_graph_from_gz(file_path)

# 1. Calculate the average degree
def average_degree(G):
    degrees = dict(G.degree()).values()
    return sum(degrees) / float(G.number_of_nodes())

avg_degree = average_degree(G)
print(f"Average Degree: {avg_degree}")

# 2. Calculate transitivity (global clustering coefficient)
transitivity = nx.transitivity(G)
print(f"Transitivity (Global Clustering Coefficient): {transitivity}")

# 3. Calculate the diameter of the largest connected component
largest_cc = max(nx.connected_components(G), key=len)
subgraph = G.subgraph(largest_cc)
diameter = nx.diameter(subgraph)
print(f"Diameter: {diameter}")

# 4. Calculate the radius of the largest connected component
radius = nx.radius(subgraph)
print(f"Radius: {radius}")

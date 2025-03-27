import networkx as nx
import matplotlib.pyplot as plt

# classify what region in the brain the node name is from, since its not included in the data. making best guess here
def classify_region(name):
    if name.startswith("V"): return "visual"
    elif name.startswith("M"): return "motor"
    elif name.startswith("F"): return "frontal"
    elif name.startswith("S"): return "somatosensory"
    elif name.startswith("T"): return "temporal"
    elif "Hip" in name or name.startswith("CA"): return "hippocampus"
    else: return "other"

G = nx.read_graphml("data/rhesus_brain_1.graphml")

# for loops to fill up these arrays with different sized node weights, write names to a file

# no weights in the data, so gonna try to color code and adjust weights based on node names
# maybe just show the names instead since they're unique
file1 = open("rhesus_names.txt", "w+")
node_names = []
for node in G.nodes():
    name = G.nodes[node]['name'] # scoring based on length of name
    node_names.append(name) # (score**(1.5))) * 
    
    file1.write(name)
    file1.write("\n")
    
file1.close()

colors = []
for node in G.nodes():
    region_type = classify_region(G.nodes[node]['name'])
    # based on returned region_type, use switch to set color 
    color = {
        "visual": "yellow",
        "motor": "orange",
        "frontal": "aqua",
        "temporal": "darkviolet",
        "somatosensory": "cyan",
        "hippocampus": "red",
        "other": "skyblue"
    }[region_type] 
    colors.append(color)

plt.figure(figsize=(35,35)) # higher resolution 
pos = nx.spring_layout(G)

# had to seperate draw calls to avoid drawing ugly arrows
# nx.draw(G, pos, with_labels=False, node_color="skyblue", edge_color="gray", node_size=node_sizes, width=edge_widths)
nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=550)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, arrows=False, edge_color="paleturquoise", width=0.8)
plt.title("Rhesus Brain Nerve Edges", fontsize=70)
plt.savefig("rhesus_plt.png")
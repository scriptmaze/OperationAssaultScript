import networkx as nx
import matplotlib.pyplot as plt
from code_generator import *

df = generate_df()
df6 = df.iloc[[5],[5]]
df6 = df.count()
df21 = df.iloc[[5],[5]]
df3 = df.iloc[[5],[5]]
df1 = df.iloc[[5],[5]]
df2 = df.count()
G = nx.DiGraph()
df6 = df.iloc[[5],[5]]
df0 = df.iloc[[5],[5]]
G.add_nodes_from(df.columns)
df1 = df.iloc[[5],[5]]

for col in df.columns:
 df0 = df.sort_index()
    for idx, val in enumerate(df[col]):
        G.add_edge(col, df.index[idx], weight=val)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

print (df)

# -*- coding: utf-8 -*-
import networkx as nx
# import matplotlib.pyplot as plt

G = nx.Graph()
id2name = {}
name2id = {}

with open('pages.txt', encoding="utf-8")as pagef:
    lines = pagef.readlines()
    for line in lines:
        line = line.strip()
        id2name[int(line.split('\t')[0])] = line.split('\t')[1]
        name2id[line.split('\t')[1]] = int(line.split('\t')[0])
        G.add_node(int(line.split('\t')[0]))

with open("links.txt")as linkf:
    lines = linkf.readlines()[:-1]
    for line in lines:
        line = line.strip()
        G.add_edge(int(line.split("\t")[0]), int(line.split("\t")[1]))

def cal_shortest_path(input1, input2):
    node1 = name2id.get(input1, None)
    node2 = name2id.get(input2, None)
    if node1 is not None and node2 is not None:
        try:
            paths = nx.shortest_path(G, node1, node2)
            print(len(paths))
            print([id2name[id] for id in paths])
        except nx.NetworkXNoPath:
            print("No path")
    else:
        print("The inputs are not qualified!")

while(True):
    input1 = input("Please input the origin node: ").strip()
    input2 = input("Please input the destination node: ").strip()
    if input1 == "" and input2 == "":
        G.clear()
        name2id = None
        id2name = None
        exit(0)
    else:
        cal_shortest_path(input1, input2)


# for key in page:
#     if len([n for n in G.neighbors(key)]) == 0:
#         G.remove_node(key)


# nx.draw_networkx(G)
# plt.show()


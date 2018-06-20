Homework
===================

Let’s find interesting things from links of wikipedia!

Possible items:
----------------
    Look for a shortest path from ”Google” to ”BBQ”

    Does any other interesting path exist? Are all nodes reachable?

    Create your search engine for wikipedia dataset

    Design your query language to input what you want to search

Data
---------------
wikipedia_links.zip: pages.txt and links.txt are in the zip
https://drive.google.com/file/d/1HT6OiQgG0wfeC0xulLfuWqq7y4KT4xHW/view

Details:
------------
I used a package called networkx, which is used for creation, manipulation, and study the structure, function of complex networks. 

We can draw the graph of wiki structure and find the shortest path effectively.

The key function I used:

import networkx as nx

G = nx.graph() //initialize the graph

G.add_node()  //add nodes to graph G based on pages.txt

G.add_edge(node1, node2)  //add edges to graph G based on links.txt

nx.shortest_path(G, node1, node2)    //get the shortest path between node1 and node2 based on basic graph algorithm.


Planning to do:
----------------------
It costs a lot of time on drawing the graph of wiki structure, especially adding nodes.

We need to wait about 5 mins for constructing the graph each time. 

Considering user-friendly experience of an application is quit important, I want to save the time generating the graph which is very time-consuming. 

Such as an artificial neural network, we don’t need to train the parameters every time, 

I wonder if there is a way to save networkx’s graph into a local file instead of generating the graph every time the program is executed. 

But it seems networkx doesn’t have API like this, so I may try different method...Or, you have some good advice?



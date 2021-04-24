import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
from networkx.algorithms.community import greedy_modularity_communities
import numpy as np
import sys


def get_weight(file_name, weighted):
    if not weighted:
        return {}

    weight_dict = {}
    f = open(file_name, 'r').readlines()
    for line in f:
        line = line.split('\n')[0].split(',')
        post_author = line[2]
        comment_author = line[3]
        key = ''
        if post_author < comment_author:
            key = post_author + comment_author
        else:
            key = comment_author + post_author
        if key in weight_dict:
            weight_dict[key] += 1
        else:
            weight_dict[key] = 1
    return weight_dict


def draw_graph(G):

    # remove isolates and self edges
    G.remove_edges_from(list(G.selfloop_edges()))
    G.remove_nodes_from(list(nx.isolates(G)))

    # compute graph layout
    # (only uncomment if graph has been clipped)
    pos = graphviz_layout(G)

    # plot the network
    plt.figure(figsize=(20,14))

    nx.draw_networkx(G, pos=pos)

    plt.savefig("graph.png")

def weighted_graph(file_name, graph_name, weight_dict):
    G = nx.DiGraph()
    f = open(file_name,'r').readlines()
    i=0
    node = set()
    for line in f:
        
        line = line.split('\n')[0].split(',')
        post_author = line[2]
        comment_author = line[3]
        node.add(post_author)
        node.add(comment_author)
        key = ''
        if post_author < comment_author:
            key = post_author + comment_author
        else:
            key = comment_author + post_author
        weights = weight_dict[key]
        if weights != 0:
            i+= 1
            print("{}: {},{}".format(i,post_author, comment_author))
            G.add_edge(post_author, comment_author, weight = weights)
            weight_dict[key] = 0
    print("There are {} edges in the weighted graph".format(i))
    print("There are {} nodes in the weighted graph".format(len(node)))
    nx.write_graphml(G, graph_name)
    print("saved the graphml")
    return G

def unweighted_graph(file_name, graph_name):
    G = nx.MultiDiGraph()
    f = open(file_name,'r').readlines()
    i = 0
    node = set()
    for line in f:
        line = line.split('\n')[0].split(',')
        post_author = line[2]
        comment_author = line[3]
        node.add(post_author)
        node.add(comment_author)
        i += 1
        # print("{}: {},{}".format(i,post_author, comment_author))
        G.add_edge(post_author, comment_author)
    print("There are {} edges in the unweighted graph".format(i))
    print("There are {} nodes in the unweighted graph".format(len(node)))
    nx.write_graphml(G, graph_name)
    print("saved the graphml")

    return G

def main(argv):
    input_file = ''
    graph_name = ''
    weighted = True
    for index, elem in enumerate(argv):
        if elem == "--input_file":
            input_file = argv[index + 1]
        elif elem == "--graph_name":
            graph_name = argv[index + 1]
        elif elem == "--weighted":
            wei = argv[index + 1]
            if wei == 'n':
                weighted = False

    weight_dict = {}
    weight_dict = get_weight(input_file, weighted)

    if weighted:
        print("Get weighted graph.")
        G = weighted_graph(input_file, graph_name, weight_dict)
    else:
        print("Get unweighed graph.")
        G = unweighted_graph(input_file, graph_name)
    # draw_graph(G)

if __name__ == "__main__":
    main(sys.argv[1:])
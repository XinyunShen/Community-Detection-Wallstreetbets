import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import networkx as nx
import sys
import collections
def degree_histogram_directed(G, in_degree=False, out_degree=False):
    """Return a list of the frequency of each degree value.

    Parameters
    ----------
    G : Networkx graph
       A graph
    in_degree : bool
    out_degree : bool

    Returns
    -------
    hist : list
       A list of frequencies of degrees.
       The degree values are the index in the list.

    Notes
    -----
    Note: the bins are width one, hence len(list) can be large
    (Order(number_of_edges))
    """
    nodes = G.nodes()
    if in_degree:
        in_degree = dict(G.in_degree())
        degseq=[in_degree.get(k,0) for k in nodes]
    elif out_degree:
        out_degree = dict(G.out_degree())
        degseq=[out_degree.get(k,0) for k in nodes]
    else:
        degseq=[v for k, v in G.degree()]
    dmax=max(degseq)+1
    freq= [ 0 for d in range(dmax) ]
    for d in degseq:
        freq[d] += 1
    return freq

def weighted_degree_distribution(G):
    in_degree_freq = degree_histogram_directed(G, in_degree=True)
    out_degree_freq = degree_histogram_directed(G, out_degree=True)
    degrees = range(len(in_degree_freq))
    plt.figure(figsize=(12, 8)) 
    plt.loglog(range(len(in_degree_freq)), in_degree_freq, 'go', label='in-degree') 
    plt.xlabel('In Degree')
    plt.ylabel('Frequency')
    # plt.show()
    plt.savefig("in_degree_frequency.png")
    plt.figure(figsize=(12, 8)) 
    plt.loglog(range(len(out_degree_freq)), out_degree_freq, 'bo', label='out-degree')
    plt.xlabel('Out Degree')
    plt.ylabel('Frequency')
    # plt.show()
    plt.savefig("out_degree_frequency.png")

def unweighed_degree_distribution(G):
    m = 3
    degree_freq = nx.degree_histogram(G)
    degrees = range(len(degree_freq))
    plt.figure(figsize=(12, 8)) 
    plt.loglog(degrees[m:], degree_freq[m:],'go') 
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.savefig("unweighted_degree_frequency.png")

def node_num(G):
    print("There are {} nodes in the graph.".format(len(G)))

def edge_num(G):
    print("There are {} edges in the graph.".format(G.number_of_edges()))

def distance_measure(G):
    print("The radius of the graph is {}.".format(nx.radius(G)))
    print("The diameter of the graph is {}.".format(nx.diameter(G)))

def clustering_coef(G):
    print("The average clustering coefficient is {}.".format((nx.average_clustering(G))))

def main(argv):
    graph_name = ''
    weighted = True
    for index, elem in enumerate(argv):
        if elem == "--graph_name":
            graph_name = argv[index + 1]
        elif elem == "--weighted":
            wei = argv[index + 1]
            if wei == 'n':
                weighted = False

    print("open graph {}".format(graph_name))
    G = nx.read_graphml(graph_name)
    if weighted:
        weighted_degree_distribution(G)
    else:
        unweighed_degree_distribution(G)
    
    node_num(G)
    edge_num(G)
    # distance_measure(G)
    if weighted:
        clustering_coef(G)

if __name__ == "__main__":
    main(sys.argv[1:])
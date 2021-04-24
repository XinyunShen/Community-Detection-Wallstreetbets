import numpy as np
import networkx as nx
from sklearn import cluster
import sys

def graph_to_edge_matrix(G):
    """Convert a networkx graph into an edge matrix.   
    Parameters
    ----------
    G : networkx graph
    """
    # Initialize edge matrix with zeros
    edge_mat = np.zeros((len(G), len(G)), dtype=int)

    # Loop to set 0 or 1 (diagonal elements are set to 1)
    for node in G:
        for neighbor in G.neighbors(node):
            edge_mat[node][neighbor] = 1
        edge_mat[node][node] = 1

    return edge_mat


def conductances(G, communities):
    '''Compute conductance for a list of communities
    '''
    return [nx.algorithms.cuts.conductance(G, community) for community in communities]

def main(argv):
    input_file = ''
    for index, elem in enumerate(argv):
        if elem == "--input_file":
            input_file = argv[index + 1]
    

    # load in preprocessed graph
    G = nx.read_graphml(input_file)


    # put together communities
    cc = nx.convert_node_labels_to_integers(G)
    em = graph_to_edge_matrix(cc)
    for i in range(10,101,10):
        kmeans = cluster.KMeans(n_clusters=i).fit(em)

        kpart = {}
        for j in range(len(kmeans.labels_)):
            label = kmeans.labels_[j]
            if kpart.get(label) is None:
                kpart[label] = []
            kpart[label].append(j)

        ksubgraphs = [nodes for label,nodes in kpart.items()]
        
        # compute conductances
        conductance_list = conductances(cc,ksubgraphs)
        print('Min conductance for k={}: {}'.format(i,np.min(conductance_list)))
        
        # compute modularity
        print('Modularity for k={}: {}'.format(i,nx.algorithms.community.quality.modularity(cc,ksubgraphs)))

if __name__ == "__main__":
    main(sys.argv[1:])
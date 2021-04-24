import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import secrets
import math
import random
import sys



def draw(G, pos, measures, measure_name, graph_name, labels):
    edge_num = G.number_of_edges()
    node_color=list(measures.values())

    #set the argument 'with labels' to False so you have unlabeled graph
    nodes = nx.draw_networkx_nodes(G, pos,node_size=20, cmap=plt.cm.plasma, 
                                   node_color=node_color,
                                   nodelist=measures.keys(),edge_colors=('g'), with_labels=False)
    

    #Now only add labels to the nodes you require (the hubs in my case)
    nx.draw_networkx_labels(G,pos,labels,font_size=15,font_color='r')
        
    nodes.set_norm(mcolors.SymLogNorm(linthresh=0.01, linscale=1))
    # labels = nx.draw_networkx_labels(G, pos)
    edges = nx.draw_networkx_edges(G, pos)
    plt.title(measure_name)
    plt.colorbar(nodes)
    plt.axis('off')
    plt.show()
    plt.savefig(graph_name)


def wirte2file(measure, file_name):
    f = open(file_name,'a')
    sorted_measures = sorted(measure.items(), key=lambda x: x[1], reverse=True)
    for elem in sorted_measures:
        f.write("{},{}\n".format(elem[0], elem[1]))
    print("write to {} done.".format(file_name))
    return sorted_measures

def draw_graph(nodes, authors, G, top_10):
    new_G = nx.DiGraph()
    node_dict = arrar2dict(nodes)
    new_label_node_dict = {}
    new_measure_dict = {}
    for u,v,a in G.edges(data=True):
        if u in authors and v in authors:
            new_measure_dict[u] = node_dict[u]
            new_measure_dict[v] = node_dict[v]
            if u in top_10:
                new_label_node_dict[u] = u
            if v in top_10:
                new_label_node_dict[v] = v
            new_G.add_edge(u, v, weight= a['weight'])
    
    print("There are {} nodes in the new weighted graph".format(len(new_G)))
    print("There are {} edges in the new weighted graph".format(new_G.number_of_edges()))
    # print(new_label_node_dict)
    return new_G, new_label_node_dict, new_measure_dict

def arrar2dict(array):
    node_dict = {}
    for elem in array:
        node_dict[elem[0]] = elem[1]
    return node_dict

def reconstruct_graph(G, sorted_measures, graph_size, output_graph_name, title):
    # only construct graph with 1000 nodes
    # First get top 50 node
    # ramdomly get 950 rest nodes
    top_node_num = math.floor(graph_size)
    rest_node_num = graph_size - top_node_num
    nodes = sorted_measures[:top_node_num]
    rest_nodes = sorted_measures[top_node_num:]

    for i in range(rest_node_num):
        nodes.append(secrets.choice(rest_nodes))

    authors = []
    for elem in nodes:
        authors.append(elem[0])
    print("We'll draw a graph with size {}".format(len(authors)))
    
    top_10 = []
    for elem in sorted_measures[:10]:
        top_10.append(elem[0])

    # Lable only top 10 nodes
    print("create new graph...")
    new_G, new_label_node_dict, new_measure_dict = draw_graph(nodes, authors, G, top_10)
    

    pos = nx.spring_layout(new_G, seed=675)
    labels = {}
    for author in authors:
        labels[author] = author
    print("draw the graph...")
    draw(new_G, pos, new_measure_dict, title, output_graph_name, new_label_node_dict)

    


def pagerank(G, graph_size, output_path, output_graph_name):
    pr = nx.pagerank(G, alpha=0.9)
    print("calculate pagerank done.")
    sorted_measures = wirte2file(pr, output_path)
    reconstruct_graph(G, sorted_measures, graph_size, output_graph_name, 'WallstreetBets DiGraph PageRank')

def closeness(G, graph_size, output_path, output_graph_name):
    closeness = nx.closeness_centrality(G)
    print("calculate closness done.")
    sorted_measures = wirte2file(closeness, output_path)
    reconstruct_graph(G, sorted_measures, graph_size, output_graph_name, 'WallstreetBets DiGraph Closeness')

def betweeness(G, graph_size, output_path, output_graph_name):
    betweeness = nx.betweenness_centrality(G)
    print("calculate betweeness done.")
    sorted_measures = wirte2file(closeness, output_path)
    reconstruct_graph(G, sorted_measures, graph_size, output_graph_name, 'WallstreetBets DiGraph Betweeness')

def katz(G, graph_size, output_path, output_graph_name):
    katz = nx.katz_centrality(DiG, alpha=0.1, beta=1.0)
    print("calculate katz done.")
    sorted_measures = wirte2file(closeness, output_path)
    reconstruct_graph(G, sorted_measures, graph_size, output_graph_name, 'WallstreetBets DiGraph Katz')

def degree(G, graph_size, output_path, output_graph_name):
    centrality = nx.degree_centrality(G)
    print("calculate degree done.")
    sorted_measures = wirte2file(centrality, output_path)
    indegree_centrality = nx.in_degree_centrality(G)
    print("calculate in degree done.")
    indegree_sorted_measures = wirte2file(indegree_centrality, "in"+output_path)
    outdegree_centrality = nx.out_degree_centrality(G)
    print("calculate out degree done.")
    outdegree_sorted_measures = wirte2file(outdegree_centrality, "out" + output_path)
    reconstruct_graph(G, sorted_measures, graph_size, output_graph_name, 'WallstreetBets DiGraph Degree Centrality')
    reconstruct_graph(G, indegree_sorted_measures, graph_size, "in"+output_graph_name, 'WallstreetBets DiGraph In-Degree Centrality')
    reconstruct_graph(G, outdegree_sorted_measures, graph_size, "out"+output_graph_name, 'WallstreetBets DiGraph Out-Degree Centrality')

    

def main(argv):
    graph_name = ''
    measure = ''
    graph_size = 0
    output_path = ''
    output_graph_name = ''
    for index, elem in enumerate(argv):
        if elem == "--graph_name":
            graph_name = argv[index + 1]
        elif elem == "--measure":
            measure = argv[index + 1]
        elif elem == "--graph_size":
            graph_size = int(argv[index + 1])
        elif elem == "--output_path":
            output_path = argv[index + 1]
        elif elem == "--output_graph_name":
            output_graph_name = argv[index + 1]

    print("open graph {}".format(graph_name))
    G = nx.read_graphml(graph_name)
    if measure == 'pagerank':
        pagerank(G, graph_size, output_path, output_graph_name)
    elif measure == 'degree':
        degree(G, graph_size, output_path, output_graph_name)
    elif measure == 'closeness':
        closeness(G, graph_size, output_path, output_graph_name)
    elif measure == 'betweeness':
        closeness(G, graph_size, output_path, output_graph_name)
    elif measure == 'katz':
        closeness(G, graph_size, output_path, output_graph_name)


if __name__ == "__main__":
    main(sys.argv[1:])


import networkx as nx
import sys
from fast_pagerank import pagerank

def main(argv):
    graph_name = ''
    weighted = True
    for index, elem in enumerate(argv):
        if elem == "--graph_name":
            graph_name = argv[index + 1]

    print("open graph {}".format(graph_name))
    G = nx.read_graphml(graph_name)
    # G = nx.DiGraph()
    # G.add_edges_from([(1,2),(2,3),(4,5),(4,6)])
    pr = nx.pagerank(G, alpha=0.9)
    f = open('pagerank.csv','a')
    a = sorted(pr.items(), key=lambda x: x[1], reverse=True)
    for elem in a:
        f.write("{},{}\n".format(elem[0], elem[1]))

if __name__ == "__main__":
    main(sys.argv[1:])
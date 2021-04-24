import networkx as nx
import matplotlib.pyplot as plt
import sys

def convert_graph(file_name, graph_name):
    MG = nx.MultiGraph()
    i = 0
    f = open(file_name,'r').readlines()
    for line in f:
        i += 1
        line = line.split(',')
        post_author = line[2]
        comment_author = line[3]
        # print("{}: {},{}".format(i,post_author, comment_author))
        MG.add_edge(post_author, comment_author)

    print("outside the loop")
    nx.write_graphml(MG, graph_name)
    print("saved the graphml")

def main(argv):
    input_file = ''
    graph_name = ''
    for index, elem in enumerate(argv):
        if elem == "--input_file":
            input_file = argv[index + 1]
        elif elem == "--graph_name":
            graph_name = argv[index + 1]
    
    convert_graph(input_file, graph_name)

if __name__ == "__main__":
    main(sys.argv[1:])
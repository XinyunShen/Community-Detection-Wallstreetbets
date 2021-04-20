import networkx as nx
import matplotlib.pyplot as plt


# f_name = ['post_comments_info1.csv','post_comments_info2.csv','post_comments_info3.csv','post_comments_info4.csv','post_comments_info5.csv','post_comments_info6.csv','post_comments_info7.csv','post_comments_info8.csv']
# f_name = ['post_comments_info1.csv']
MG = nx.MultiGraph()
i = 0
f = open('post_comments_info_total.csv','r').readlines()
for line in f:
    i += 1
    line = line.split(',')
    post_author = line[2]
    comment_author = line[3]
    # print("{}: {},{}".format(i,post_author, comment_author))
    MG.add_edge(post_author, comment_author)

print("outside the loop")
nx.write_gml(MG, "metagraph.graphml")
print("saved the graphml")
# nx.draw(MG)
# plt.savefig("metagraph.png")
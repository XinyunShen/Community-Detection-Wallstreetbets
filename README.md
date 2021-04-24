# EECS476-final-project

## Generate Graph

``python3 graph.py --input_file post_comments_info_total.csv --graph_name weighted_metagraph.graphml --weighted y``

output:

There are 924111 edges in the weighted graph
There are 189825 nodes in the weighted graph

``$ python3 graph.py --input_file post_comments_info_total.csv --graph_name unweighted_metagraph.graphml --weighted n``

output:

There are 2991439 edges in the unweighted graph
There are 189825 nodes in the unweighted graph

## Get Graph info 

``$ python3 graph_info.py --graph_name weighted_metagraph.graphml --weighted y``

output:

There are 189825 nodes in the graph.
There are 924111 edges in the graph.
The average clustering coefficient is 0.19915676897676993.

output_file:


``$ python3 graph_info.py --graph_name unweighted_metagraph.graphml --weighted n``

output:

There are 189825 nodes in the graph.
There are 2991439 edges in the graph.

output_file:

in_degree_frequency.png
out_degree_frequency.png


``$ python3 pagerank.py --graph_name weighted_metagraph.graphml``

output_file:

unweighted_degree_frequency.png

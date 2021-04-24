# EECS476-final-project

``python3 graph.py --input_file post_comments_info_total.csv --graph_name weighted_metagraph.graphml --weighted y``

output:

There are 924111 edges in the weighted graph.

``python3 graph.py --input_file post_comments_info_total.csv --graph_name unweighted_metagraph.graphml --weighted n``

output:

There are 2991439 edges in the unweighted graph.

``python3 kmeans_computation.py --input_file testgraph.graphml``

``python3 graph_info.py --graph_name weighted_metagraph.graphml --weighted y``

output:

There are 189825 nodes in the graph.
There are 924111 edges in the graph.

``python3 graph_info.py --graph_name unweighted_metagraph.graphml --weighted n``

output:

There are 189825 nodes in the graph.
There are 2991439 edges in the graph.

``python3 pagerank.py --graph_name weighted_metagraph.graphml``
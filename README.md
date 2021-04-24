# EECS476-final-project

## Generate Graph
Please use post_comments_info_test.csv to get a quickly generated graph.
Parameters:
- ``input_file``: The input csv file
- ``graph_name``: The output graph name
- ``weighted``: Whether this graph is weighted or unweighted

``python3 graph.py --input_file post_comments_info_total.csv --graph_name weighted_metagraph.graphml --weighted y``

output:

There are 924111 edges in the weighted graph
There are 189825 nodes in the weighted graph

output_file:

weighted_metagraph.graphml

``$ python3 graph.py --input_file post_comments_info_total.csv --graph_name unweighted_metagraph.graphml --weighted n``

output:

There are 2991439 edges in the unweighted graph
There are 189825 nodes in the unweighted graph

output_file:

unweighted_metagraph.graphml

## Get Graph info 
parameters:
- ``graph_name``: The input graph name
- ``weighted``: Whether this graph is weighted or unweighted


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

## Centrality Measures


Parameters:
- ``graph_name``: The input graph name
- ``measure``: The measurements, you can choose pagerank/degree/closeness/beteeness/katz
- ``graph_size``: You can create graph with customed graph size, for example 100/1000
- ``output_path``: The output csv file name

### PageRank Centrality

``$ python3 centrality.py --graph_name test_metagraph.graphml --measure pagerank --graph_size 100 --output_path test_pagerank.csv``

``$ python3 centrality.py --graph_name weighted_metagraph.graphml --measure pagerank --graph_size 2000 --output_path pagerank.csv --output_graph_name pagerank.png``

### Degree Centrality

``$ python3 centrality.py --graph_name weighted_metagraph.graphml --measure degree --graph_size 1000 --output_path degree_centrality.csv --output_graph_name degree_centrality.png``

### Closeness Centrality

``$ python3 centrality.py --graph_name weighted_metagraph.graphml --measure closeness --graph_size 1000 --output_path closeness_centrality.csv --output_graph_name closeness_centrality.png``

### Betweeness Centrality
``$ python3 centrality.py --graph_name weighted_metagraph.graphml --measure betweeness --graph_size 1000 --output_path betweeness_centrality.csv --output_graph_name betweeness_centrality.png``

### Katz Centrality
``$ python3 centrality.py --graph_name weighted_metagraph.graphml --measure katz --graph_size 1000 --output_path katz_centrality.csv --output_graph_name katz_centrality.png``


## Acknowledgements

This project was built as a final project for EECS 476 at the University of Michigan -- Ann Arbor.

Authors - Xinyun Shen/ Xueming Xu
# EECS476-final-project

## Crawl Datat
We use reddit api and pushshift api, this is not necessary to run because it is only the preparation for our project
``$ python3 get_data.py``

## Combine all dataset
This is not necessary to run because it is only the preparation for our project
``$ python3 combine_file.py``

## Generate Graph
You can start run and test our code from here!!!

Parameters:
- ``input_file``: The input csv file
- ``graph_name``: The output graph name
- ``weighted``: Whether this graph is weighted or unweighted

Please use post_comments_info_test.csv to get a quickly generated graph.
For test: 
Generate a weighted graph:
``$ python3 graph.py --input_file post_comments_info_test.csv --graph_name weighted_metagraph.graphml --weighted y``

Generate an unweighted graph:
``$ python3 graph.py --input_file post_comments_info_test.csv --graph_name unweighted_metagraph.graphml --weighted n``


## Get Graph info 

parameters:
- ``graph_name``: The input graph name
- ``weighted``: Whether this graph is weighted or unweighted

``$ python3 graph_info.py --graph_name weighted_metagraph.graphml --weighted y``

``$ python3 graph_info.py --graph_name unweighted_metagraph.graphml --weighted n``

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

Following are pretty much similar so you don't need to test all of them.

### Closeness Centrality

``$ python3 centrality.py --graph_name weighted_metagraph.graphml --measure closeness --graph_size 1000 --output_path closeness_centrality.csv --output_graph_name closeness_centrality.png``

### Betweeness Centrality
``$ python3 centrality.py --graph_name weighted_metagraph.graphml --measure betweeness --graph_size 1000 --output_path betweeness_centrality.csv --output_graph_name betweeness_centrality.png``

### Katz Centrality
``$ python3 centrality.py --graph_name weighted_metagraph.graphml --measure katz --graph_size 1000 --output_path katz_centrality.csv --output_graph_name katz_centrality.png``


## Acknowledgements

This project was built as a final project for EECS 476 at the University of Michigan -- Ann Arbor.

Authors - Xinyun Shen/ Xueming Xu
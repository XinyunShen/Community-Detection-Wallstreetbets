#!/bin/bash
python3 graph.py --input_file post_comments_info_test.csv --graph_name test_metagraph.graphml --weighted y

python3 graph_info.py --graph_name test_metagraph.graphml --weighted y

python3 centrality.py --graph_name test_metagraph.graphml --measure pagerank --graph_size 100 --output_path test_pagerank.csv --output_graph_name test_pagerank.png

python3 centrality.py --graph_name test_metagraph.graphml --measure degree --graph_size 100 --output_path test_degree_centrality.csv --output_graph_name test_degree_centrality.png

python3 centrality.py --graph_name test_metagraph.graphml --measure hits --graph_size 100 --output_path test_hits.csv --output_graph_name test_hits.png
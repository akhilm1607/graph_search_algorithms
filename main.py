import graph_search_algo
import netlist_graph
import numpy as np

# Taking the inputs from user
inputs, outputs, gate_io = netlist_graph.extract_gate_io(r"C:\Users\akhil\OneDrive\Documents\SEMESTER_2\VDA\Assignment_1\ISCAS89\s208.bench")
dir_or_undir = input("Choose one of the following: \n1. Directed Graph\n2. Undirected Graph\nEnter your option: ")

# Creating the list of nodes from netlist
node_list = []
node_list.append('src')
node_list.extend(gate_io.keys())
node_list.append('snk')
print('Node List: \n', node_list)

# To extract the edges from the netlist by considering the nodes as Gates and edges as interconnects
edge_list = netlist_graph.gate_io_edges(gate_io, inputs, outputs, node_list)
adjacency_matrix_inf = netlist_graph.edge_list_adj_mat(edge_list, node_list, dir_or_undir)
adjacency_matrix_inf = np.array(adjacency_matrix_inf)

# Mapping the nodes to numerical indeces to form adjacency matrix
nodes_dict = {}
for i in range(len(node_list)):
    nodes_dict[i] = node_list[i]
adjacency_matrix = graph_search_algo.convert_inf_zero(adjacency_matrix_inf)

# print("Adjacency Matrix: \n", adjacency_matrix)

# Initializing the data structures needed for DFS as it works on recursion
visited_list = [False] * len(adjacency_matrix_inf)
stack_nodes = []
path_of_dfs = []

# Calling the plotting and searching functions
graph_search_algo.graph_plotter(adjacency_matrix, dir_or_undir, visited_list, nodes_dict, node_list)
graph_search_algo.depth_first_search(adjacency_matrix, 'src', node_list, nodes_dict, visited_list, stack_nodes, path_of_dfs)
graph_search_algo.breadth_first_search(adjacency_matrix, 'src', nodes_dict, node_list)
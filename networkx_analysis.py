import networkx as nx
import matplotlib.pyplot as plt
import time

def print_basic_graph_info(gr):
    print(f'Number of nodes:\t{gr.number_of_nodes()}')
    print(f'Number of edges:\t{gr.number_of_edges()}')

def main():
    print('\nLoading network from .gml file...')
    G_raw = nx.read_gml('network/lesmis.gml')   # read graph to networkx
    print('DONE\n')
    print_basic_graph_info(G_raw)

    print('\nRemoveing duplicated edges...')
    G = nx.Graph(G_raw)                         # delete duplicated edges 
    print('DONE\n')
    print_basic_graph_info(G)

    print('\nConverting graph to undirected...')
    GU = G.to_undirected()                      # convert to undirected graph
    print_basic_graph_info(GU)
    print('DONE\n')

    print('\nConverting graph to .net file for Pajek usage...')
    nx.write_pajek(G, 'network/lasmis.net')     # convert graph to .net file for Pajek usage
    print('DONE\n')

    print('\nGenerating connected components as subgraphs...')
    start = time.time() # start measuring time for the operation
    GU_connected_components = list(nx.connected_component_subgraphs(GU))         # generate connected components as subgraphs
    end = time.time()   # end measuring time for the operation
    print(f'DONE\t Generation time:\t{(end - start):.5f} seconds\n')

    print(f'\nNumber of connected components:\t{len(GU_connected_components)}\n') # count number of connected subgraphs
    
    print('\nExtracting largest connected component...')
    GUc = max(GU_connected_components, key=len) # extract largest connected component as subgraph
    print_basic_graph_info(GUc)
    print('DONE\n')

    print('\nPrinting largest connected component...')
    nx.draw(GUc)
    plt.show()
    print('DONE\n')

if __name__ == '__main__':
    main()
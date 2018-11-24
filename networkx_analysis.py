import networkx as nx
import matplotlib.pyplot as plt

def main():
    print('\nLoading network from .gml file...')
    G_temp = nx.read_gml('network/lesmis.gml')  # read graph to networkx
    print('DONE\n')
    print(f'Number of nodes:\t{G_temp.number_of_nodes()}')
    print(f'Number of edges:\t{G_temp.number_of_edges()}')

    print('\nRemove duplicated edges...')
    G = nx.Graph(G_temp)                        # delete duplicated edges 
    print('DONE\n')
    print(f'Number of nodes:\t{G.number_of_nodes()}')
    print(f'Number of edges:\t{G.number_of_edges()}') 

    print('\nConvert graph to undirected...')
    GU = G.to_undirected()                      # convert to undirected graph
    print('DONE\n')

    print('\nConvert graph to .net file for Pajek usage...')
    nx.write_pajek(G, 'network/lasmis.net')     # convert graph to .net file for Pajek usage
    print('DONE\n')

if __name__ == '__main__':
    main()
import networkx as nx
import matplotlib.pyplot as plt

def main():
    G = nx.read_gml("network/lesmis.gml")
    nx.write_pajek(G, "network/lasmis.net")

if __name__ == "__main__":
    main()
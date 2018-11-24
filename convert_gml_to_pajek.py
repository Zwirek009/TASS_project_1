import networkx as nx
import matplotlib.pyplot as plt

def main():
    G = nx.read_gml("network/lesmis.gml")
    GU = G.to_undirected()
    nx.draw(GU)
    plt.show()

if __name__ == "__main__":
    main()
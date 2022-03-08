import networkx as nx
import matplotlib.pyplot as plt

def sim_wup(G, i, j):
    #definir root
    #root='Thing'

    print('i, j: ',end='')
    print(i,j)

    if i == j:
        res = 1.0
        return res

    # definindo o no raiz da arvore
    for i in G.nodes():
        if (G.in_degree(i) == 0):
            root = i
            print('root: ',end='')
            print(root)

    # calculando o Least Common Subsumer (Ancestor)
    LCS = nx.lowest_common_ancestor(G, i, j, default=None)

    print('LCS: '+str(LCS))

    H = G.to_directed()
    # calculando a profundidade dos nos =  menor caminho do no até a raiz
    depth_lcs   = nx.shortest_path_length(H, root, LCS)
    print('depth_lcs: ',end='')
    print(depth_lcs)
    depth_node1 = nx.shortest_path_length(H, root, i)
    print('depth_node1: ',end='')
    print(depth_node1)
    depth_node2 = nx.shortest_path_length(H, root, j)
    print('depth_node2: ',end='')
    print(depth_node2)

    try:
        res = (2 * depth_lcs) / (depth_node1 + depth_node2)
    except ZeroDivisionError:
        res = 0

    print(res)
    return(res)


G = nx.DiGraph()

G.add_edges_from([(1, 2), (1, 3),(1, 5), (2, 4),(3,4),(3,6)])

sim_wup(G, 2, 3)

nx.draw(G, with_labels=True, font_weight='bold')
plt.show()



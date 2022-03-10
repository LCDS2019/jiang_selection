import networkx as nx

###################################################################
# Medida de similaridade Spath

def sim_spath(G,i,j):

    if i == j:
        res = 1.0

    else:
        try:
            res=1/nx.shortest_path_length(G,i,j)
        except:
            res=0

    return(res)


def sim_spath2(vetor,l, zarq_i, G, i, j):
    res=sim_spath(G, i, j)

    if res >0:
        u=[zarq_i.split('.')[0], i, j,"{:.4f}".format(float(res))]
        #print(l,'|',u[0],'|',u[2],'|',u[1],'|',u[3])
        u=[u[0],u[2],u[3]]
        vetor.append(u[2])


        return (vetor)


###################################################################
# Medida de similaridade Spath

def sim_wup(G, i, j):
    #definir root
    root='Thing'

    # no raiz da snomed-ct:
    #root = "C3531735"

    if i == j:
        res = 1.0
        return res

    # definindo o no raiz da arvore
    #for i in G.nodes():
        #if (G.in_degree(i) == 0):
            #root = i

    # calculando o Least Common Subsumer (Ancestor)
    LCS = nx.lowest_common_ancestor(G, i, j)

    print('LCS: '+str(LCS))

    H = G.to_undirected()
    # calculando a profundidade dos nos =  menor caminho do no até a raiz
    depth_lcs   = nx.shortest_path_length(H, root, LCS)
    depth_node1 = nx.shortest_path_length(H, root, i)
    depth_node2 = nx.shortest_path_length(H, root, j)

    try:
        res = (2 * depth_lcs) / (depth_node1 + depth_node2)
    except ZeroDivisionError:
        res = 0

    return(res)

def sim_wup2(vetor,l, zarq_i, G, i, j):
    res=sim_wup(G, i, j)

    if res >0:
        u=[zarq_i.split('.')[0], i, j,"{:.4f}".format(float(res))]
        #print(l,'|',u[0],'|',u[2],'|',u[1],'|',u[3])
        u=[u[0],u[2],u[3]]
        vetor.append(u[2])

        return (vetor)
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

    return("{:.2f}".format(float(res)))
    #return(res)



def sim_spath2(zarq_i,G,i,j):

    if i == j:
        res = 1.0

    else:
        try:
            res=1/nx.shortest_path_length(G,i,j.lower())
        except:
            res=0
        if res >0:
            print(zarq_i.split('.')[0],'***', i, '***', j, '***',"{:.2f}".format(float(res)))
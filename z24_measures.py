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

    u="{:.2f}".format(float(res))
    return(u)
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
            u=[zarq_i.split('.')[0], i, j,"{:.2f}".format(float(res))]
            print(u[0],u[1],u[2],u[3])
            u=[u[0],u[2],u[3]]

    return (u)

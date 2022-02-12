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






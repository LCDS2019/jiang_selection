##########################################################################################
#Algorithm 2 - Pseudo code for ”compute similarity score”
##########################################################################################
'''
for each term T_d extracted from dataset D_t do
    Compute the lexical similarity scores Sim_t of T_d and the
    labels of concepts C_l in the ontology using Wu and Palmer algorithm
    Build the similarity graph (D_t , C_l , Sim_t)
    CDSV[D_t][C_l]=Sim_t
end for

let D_i =dataset, C_j =concept, S ij=similarity score for C_j
and D_i , CCSM[C_t][C_j]=similarity score of concepts C_t and C_j

for each (D_i , C_j , S_ij) in the similarity graph do
    for each concept C_c in the ontology do
        similarity score = CCSM[C_c][C_j]*S_ij
        CDSV[D_i ][C_c ]=max(similarity score, CDSV[D_i][C_c])
    end for
end for
'''
##########################################################################################
import z28_nlp02 as z28
import z24_measures as z24
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def td_similarity_scores(zarq_i,data, TD):

    similarity_graph= nx.Graph()

    ulist=[]

    #print(TD)
    #print(zarq_i)

    for i in TD:

        for j in data.nodes():
            j=str(j).replace("_", " ")
            #print(j)

            try:
                #print(i,'************************',j)
                z24.sim_spath2(zarq_i,data,i,j)

                #ulist.append((zarq_i,j,u))
                #similarity_graph.add_weighted_edges_from([(zarq_i,j,u)])
                #print((zarq_i,j,u))
            except:
                'n/a'

    #return ([zarq_i, j, u])





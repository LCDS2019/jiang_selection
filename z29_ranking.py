import matplotlib.pyplot as plt
import numpy as np
import math
from numpy import dot
from numpy.linalg import norm
import pandas as pd
from random import randint

def ranking(db_system,ontologia,df_cdsv_vf):
    #print(df_cdsv_vf.head(10))
    print('')

    rank_list=[]
    rank = df_cdsv_vf.values.tolist()

    res_lista = []

    j=0

    #ref = rank[0]
    #ref = [float(item) for item in ref]

    ref=[]
    for i in range(len(rank[0])):
        ref.append(1.0)

    print('Ref: ',end='')
    print(ref)
    print(len(ref))

    print('************************************')
    for i in df_cdsv_vf.index:
        list_of_floats = [float(item) for item in rank[j]]

        rank_list.append([i, list_of_floats])

        vec=rank_list[j]
        print(vec[0])
        print(vec[1])
        print(len(vec[1]))

        print('Result: ',end='')

        result = dot(ref, vec[1]) / (norm(ref) * norm(vec[1]))
        print(result)

        #res_lista.append([vec[0],vec[1],result])
        res_lista.append([vec[0], result])

        j=j+1
        print('************************************')

    from operator import itemgetter
    ranking = sorted(res_lista, key=itemgetter(1), reverse=True)

    print('Ranking')
    ranking_output=[]
    j=0
    for i in ranking:
        print(j,' | ',i[0],' | ',i[1])
        ranking_output.append([j,i[0],i[1]])
        j=j+1

    df_ranking_output=pd.DataFrame(ranking_output, columns=['Ranking', 'DataSet', 'Max_Sim'])
    df_ranking_output.to_csv(db_system + str(ontologia.split('.')[0]) + '_ranking.csv', sep='|',index=False)

'''

res_lista=[]

u=0
for i in vectors:
    vec=i[2:4]
    result = dot(ref, vec) / (norm(ref) * norm(vec))
    res_lista.append([u,vec, result])
    u=u+1


#for i in res_lista:
    #print(i)

from operator import itemgetter
ranking=sorted(res_lista, key=itemgetter(2), reverse=True)

print('*****************************')
for i in ranking:
    print(i)
print('*****************************')


'''
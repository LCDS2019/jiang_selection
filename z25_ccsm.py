##########################################################################################
# CCSM
##########################################################################################
import os
import pickle
import pandas as pd
import numpy as np
import z24_measures as z24

def ccsm(data,nodes,db_system,ontologia):


    #print(80 * '-')
    print(' CCSM matrix '.center(80, '#'))
    print('')

    M=[]
    C=[]

    for i in data:
        for j in data:

            ans=z24.sim_spath(data,i,j)
            #ans = z24.sim_wup(data, i, j)
            #print(i,j,ans)
            M.append((i,j,"{:.4f}".format(float(ans))))
            #C.append((i,j,ans))

    #M=np.array(M)
    #M=np.resize(M, (nodes,nodes))

    df = pd.DataFrame(M, columns=['C1', 'C2', 'Ans'])
    #ccsm=df

    df = df.pivot(values='Ans', index='C1', columns='C2')
    #print(df)
    df.to_csv(db_system + str(ontologia.split('.')[0]) + '_ccsm.csv', sep='|')

    #dfC = pd.DataFrame(C)
    #dfC.to_csv(db_system+str(ontologia.split('.')[0])+'_ccsm_concepts.csv',sep='|')

    #print(M)

    return(df)
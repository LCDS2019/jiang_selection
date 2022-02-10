##########################################################################################
# CCSM
##########################################################################################
import os
import pickle
import pandas as pd
import numpy as np
from z24_measures import *

def ccsm(data,nodes,db_system,ontologia):


    #print(80 * '-')
    print(' CCSM matrix '.center(80, '#'))
    print('')


    M=[]
    C=[]
    for i in data:
        for j in data:
            ans=sim_spath(data,i,j)
            #print(i,j,ans)
            M.append(ans)
            C.append((i,j,ans))

    M=np.array(M)
    M=np.resize(M, (nodes,nodes))

    df = pd.DataFrame(M)
    df.to_csv(db_system+str(ontologia.split('.')[0])+'_ccsm.csv',sep='|')

    dfC = pd.DataFrame(C)
    dfC.to_csv(db_system+str(ontologia.split('.')[0])+'_ccsm_concepts.csv',sep='|')

    #print(M)


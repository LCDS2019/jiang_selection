##########################################################################################
# CCSM
##########################################################################################
import os
import pickle

def ccsm():
    #print(80 * '-')
    print(' CCSM matrix '.center(80, '#'))
    print('')


    M=[]
    for i in data:
        for j in data:
            ans=sim_spath(data,i,j)
            #print(i,j,ans)
            M.append(ans)
    '''
    M=np.array(M)
    M=np.resize(M, (nodes,nodes))

    df = pd.DataFrame(M)
    df.to_csv(db_out+str(ontology_selected.split('.')[0])+'_ccsm.csv',sep='|')

    print(M)
    print('')

'''
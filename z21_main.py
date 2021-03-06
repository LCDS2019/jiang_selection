##########################################################################################
print(''.ljust(81, '#'))
print('# PPGSI - USP/EACH 2022')
print('# Jiang_Selection')
print('# Version 2.1')
print('# Author: lcds2019')
print(''.ljust(81, '#'))

##########################################################################################
# libraries and modules
import os
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

from datetime import datetime
start_time = datetime.now()

import z22_functions as z22
import z23_ontology as z23
import z24_measures as z24
import z25_ccsm as z25
import z26_nlp01 as z26
import z27_ngram as z27
import z28_nlp02 as z28
import z29_ranking as z29


##########################################################################################
#Setup

onto_path = './ontology/'
db_in = './db_in/'
db_out = './db_out/'
db_system = './db_system/'

print('')

##########################################################################################
print(''.center(81, '#'))
print('#'+' Seleção de ontologias '.center(80, '#'))
print(''.center(81, '#'))

#print('onto_path: '+ str(onto_path))

ontologia=z22.create_ontology_menu(onto_path)

print('')

##########################################################################################
print(''.center(81, '#'))
print('#'+' Criação do Grafo de conceitos '.center(80, '#'))
print(''.center(81, '#'))

#print('')
#print('Dir: '+onto_path)
#print('Ontologia selecionada: '+ontologia)

data,nodes=z23.load_ontology(db_system,onto_path,ontologia)

print('')

##########################################################################################
print(''.center(81, '#'))
print('#'+' Seleção de arquivo disponíveis '.center(80, '#'))
print(''.center(81, '#'))

print('')
print('Dir: '+db_in)
dados=z22.arquivos_disponiveis(db_in)
#df_feature, df_description,filename_feature,filename_description

df_feature=dados[0]
print(df_feature.head(3))

print('----------------')

df_description=dados[1]
print(df_description.head(3))

print('----------------')

filename_feature=dados[2]
print(filename_feature)

filename_description=dados[3]
print(filename_description)

print('')

##########################################################################################
print(''.center(81, '#'))
print('#'+' Criação de arquivos sintéticos '.center(80, '#'))
print(''.center(81, '#'))

z22.apaga_arquivo_sintetico(db_in)

num_arquivos = 5 # quantidade de arquivos
colunas_arquivos = 10  # quantidade de colunas de saída
coluna_molecula = 'molecula'
coluna_alvo = 'IC50'
frac = 1  # fração do arquivo alvo
frac_aleatorio = 0 # 1-sim / 0-não - permite # diferente de linhas nos arquivos
repetition = 1 #1 - diferentes # de colunas / 2 - iguais # de colunas

z22.arquivos_sinteticos(db_in,repetition,num_arquivos,df_feature,colunas_arquivos,frac,frac_aleatorio)

print('')

##########################################################################################
print(''.center(81, '#'))
print('#'+' Medidas de similiaridade em processamento '.center(80, '#'))
print(''.center(81, '#'))

print('')
print('* - '+'sim_spath')
print('')

df_ccsm=z25.ccsm(data,nodes,db_system,ontologia)

print('')

##########################################################################################
print(''.center(81, '#'))
print('#'+' NLP - Algoritmo 01 '.center(80, '#'))
print(' NLP ”extract terms through NLP” & ”compute similarity score” '.center(81, '#'))
print(''.center(81, '#'))

path_descriptions = str(filename_description)

print(''.center(80, '-'))
print(' Datasets disponíveis para seleção '.center(80, '-'))
print(' path_descriptions '.center(80, '-'))
print(''.center(80, '-'))

print(path_descriptions)

#####################################################
print(80 * '-')

print('Stopwords:')
english_stops=z26.english_stops()

print('Punctuations:')
punctuations=z26.punctuations()

print(80 * '-')
#####################################################

path = db_in
arr = os.listdir(path)

lista = [arq for arq in arr if (arq.startswith("zarq_"))]
#lista.sort(reverse=False)

#print('')

try:
    descriptions = pd.read_csv(path_descriptions, sep='|')
    print("Arquivo de descrições localizado!")
except:
    print("Arquivo de descrições não localizado!")

#print(80 * '-')

graph=nx.Graph()
graph.add_node('root')

print('')
lista.sort()
for zarq_i in lista:
    graph.add_edge('root',zarq_i.split('.')[0])
    print(zarq_i)
print('')


#print('')
print(80 * '-')

lista_pivot=[]
lista_mean=[]

for zarq_i in lista:

    print(''.center(80, '*'))
    print('Arquivo zarq: '+zarq_i)

    zarq = pd.read_csv(db_in+zarq_i, sep='|')

    l=[]
    for i in zarq.columns:
        l.append(i)

    df = pd.DataFrame(l, columns=['Atribute'])

    dfl=pd.merge(df, descriptions, on=['Atribute'], how='left')
    print(dfl)

    M = []
    lista_n_grams = []

    for index, row in dfl.iterrows() :
        #print(''.center(40, '*'))
        atributo=str(row[0])
        #print('Atributo: '+ str(atributo))

        descricao=str(row[1])
        #print('Descrição: '+str(descricao))

        # ngram ****************************************************************
        # n = 5

        td_gram=z27.get_ngrams_01(descricao)

        td = z26.tokenize_descriptions(index, atributo, descricao, english_stops, punctuations)
        #print('Td: '+str(td))

        for i in td:
            lista_n_grams.append(i)

        for i in td_gram:
            lista_n_grams.append(i)

        #print(''.center(40, '*'))

    #print(zarq_i.split('.')[0],td)

    TD = lista_n_grams
    TD = set(TD)
    TD = list(TD)
    print('TD: '+str(TD))

    vetores_lista=[]
    ulist = []

    for j in TD:
        l = 0
        vetor=[]
        for i in data.nodes():
            u=z24.sim_spath2(vetor,l, zarq_i, data, i, j)
            #u = z24.sim_wup2(vetor, l, zarq_i, data, i, j)

            l=l+1

        if len(vetor)>0:
            vetor = [float(item) for item in vetor]

            #print(str(j)+': '+str(vetor))
            vetores_lista.append([j,vetor])

            #vetor_mean=np.mean(vetor)
            vetor_sum=np.sum(vetor)

            #ulist.append([zarq_i.split('.')[0],j,"{:.4f}".format(float(vetor_mean))])
            ulist.append([zarq_i.split('.')[0], j, "{:.4f}".format(float(vetor_sum))])
    #print('**************************')

    #print('')

    #for i in vetores_lista:
        #print(i)
    #print('')

    for i in data.nodes():
        #print(zarq_i.split('.')[0],'|',i,'|',"{:.4f}".format(float(0)))
        lista_pivot.append([zarq_i.split('.')[0],i,"{:.4f}".format(float(0))])

    #print('')
    for i in ulist:
        print(i[0].split('.')[0],'|',i[1],'|',"{:.4f}".format(float(i[2])))
        lista_mean.append(i)

        graph.add_weighted_edges_from([(i[0].split('.')[0],i[1],i[2])])

    #print('')
    #print(''.center(80, '*'))

plt.clf()
nx.draw(graph, with_labels=True, node_size=0.5,verticalalignment='bottom')
plt.savefig('./db_out/graph_datasets.png', dpi=300)

print('')

print('*****************************')
print('Arquivo CDSV')
print('*****************************')

print('')
#print('lista pivot')
df=pd.DataFrame(lista_pivot, columns=['DataSet','Concept','Sim_t'])
#print('lista mean')
df_mean=pd.DataFrame(lista_mean, columns=['DataSet','Concept','Sim_t'])
#print('*****************************')

for i in df.values:
    #print(i)
    for j in df_mean.values:
        #print(j)
        if i[0]==j[0] and i[1]==j[1]:
            i[2] = j[2]
print(df)


df=df.pivot(values = 'Sim_t', index = 'DataSet', columns = 'Concept')
#df.sort_values(by=['DataSet'], inplace=True)
df.to_csv(db_system + str(ontologia.split('.')[0]) + '_cdsv.csv', sep='|')
df_cdsv=df
df_cdsv_vf=df
#print(df)

pos = graphviz_layout(graph, prog="dot")
#nx.draw(graph, pos,with_labels=True)
#plt.show()

print(''.ljust(81, '#'))
print('')

##########################################################################################
print(''.ljust(81, '#'))
print('#'+' Máx. Similarity '.ljust(80, '#'))
print(''.ljust(81, '#'))

print('')

for i_graph in lista_mean:
    di=i_graph[0]
    cj=i_graph[1]
    sij=float(i_graph[2])

    #print(i_graph[0:3])
    #print(i_graph[1])
    #print('----------------')

    for cc in data:
        print('----------------')
        sim_score=float(df_ccsm.at[cc,cj])*sij
        #print('{:.4f}'.format(float(sim_score)))

        print(di,'|',cc)

        #print(df_cdsv.at[di,cc])

        print('max')
        print(sim_score,df_cdsv.at[di,cc])
        max=np.max([float(sim_score),float(df_cdsv.at[di,cc])])
        print('{:.4f}'.format(float(max)))
        #print('')
        df_cdsv_vf.at[di,cc]='{:.4f}'.format(float(max))
        #print(df_cdsv_vf)

print('*****************************')
print('Arquivo CDSV_vf')
print('*****************************')

df_cdsv_vf.to_csv(db_system + str(ontologia.split('.')[0]) + '_df_cdsm_vf.csv', sep='|')

print('')

##########################################################################################
print(''.ljust(81, '#'))
print('#'+' NLP - Algoritmo 03 '.ljust(80, '#'))
print(''.ljust(81, '#'))

z29.ranking(db_system,ontologia,df_cdsv_vf)

print('')

##########################################################################################
print(''.ljust(81, '-'))

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

print('#'+' End '.center(80, '#'))


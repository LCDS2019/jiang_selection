##########################################################################################
print(''.ljust(81, '#'))
print('# PPGSI - USP/EACH 2022')
print('# Jiang_Selection')
print('# Version 2.0')
print('# Author: lcds2019')
print(''.ljust(81, '#'))

##########################################################################################
# libraries and modules
import os
import numpy as np
import pandas as pd

from datetime import datetime
start_time = datetime.now()

import z22_functions as z22
import z23_ontology as z23
import z24_measures as z24
import z25_ccsm as z25


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

z23.load_ontology(db_system,onto_path,ontologia)

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

df_description=dados[1]
print(df_description.head(3))

filename_feature=dados[2]
#print(filename_feature)

filename_description=dados[3]
#print(filename_description)

print('')

##########################################################################################
print(''.center(81, '#'))
print('#'+' Criação de arquivos sintéticos '.center(80, '#'))
print(''.center(81, '#'))

z22.apaga_arquivo_sintetico(db_in)

num_arquivos = 2  # quantidade de arquivos
colunas_arquivos = 25  # quantidade de colunas de saída
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


z25.ccsm()
'''
print('')


print('')

##########################################################################################
print(''.ljust(81, '#'))
print('#'+' NLP - Algoritmo 01 '.ljust(80, '#'))
print(''.ljust(81, '#'))

print('')

##########################################################################################
print(''.ljust(81, '#'))
print('#'+' NLP - Algoritmo 02 '.ljust(80, '#'))
print(''.ljust(81, '#'))

print('')

##########################################################################################
print(''.ljust(81, '#'))
print('#'+' NLP - Algoritmo 03 '.ljust(80, '#'))
print(''.ljust(81, '#'))

print('')

##########################################################################################
print(''.ljust(81, '#'))
print('#'+' Apresentação do ranking '.ljust(80, '#'))
print(''.ljust(81, '#'))

print('')

##########################################################################################
print(''.ljust(81, '#'))
print('#'+' Registro de estatísticas '.ljust(80, '#'))
print(''.ljust(81, '#'))



print('')
'''
##########################################################################################
print(''.ljust(81, '-'))

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

print('#'+' End '.center(80, '#'))


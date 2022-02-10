import os
import pandas as pd
import numpy as np
import random
from random import sample

##########################################################################################
def create_ontology_menu(onto_path):
    path = onto_path
    arr = os.listdir(path)

    print('')
    print('Ontologias disponíveis:')

    lista = [arq for arq in arr if (arq.endswith(".owl"))]

    menu_list = []
    n = 1
    for i in lista:
        print(n, i)
        menu_list.append((n,i))
        n = n + 1

    dic_onto=dict(menu_list)

    print('')
    ontology_selection = 1
    #ontology_selection = input('Qual ontologia deseja analisar?')

    ontology_selected = dic_onto[int(ontology_selection)]
    print('Ontologia selecionada: ')
    ontology_selected=str(ontology_selected)
    print(ontology_selected)

    return (ontology_selected)


##########################################################################################

def create_feature_arq_menu(db_in):
    path = db_in
    arr = os.listdir(path)

    lista = [arq for arq in arr if (arq.endswith("features.csv"))]

    menu_list = []
    n = 1
    for i in lista:
        print(n, i)
        menu_list.append((n,i))
        n = n + 1

    dic_feature_arq=dict(menu_list)
    return (dic_feature_arq)

##########################################################################################

def create_desc_arq_menu(db_in):
    path = db_in
    arr = os.listdir(path)

    lista = [arq for arq in arr if (arq.endswith("_desc.csv"))]

    menu_list = []
    n = 1
    for i in lista:
        print(n, i)
        menu_list.append((n,i))
        n = n + 1

    dic_description_arq=dict(menu_list)
    return (dic_description_arq)

##########################################################################################
def arquivos_disponiveis(db_in):
    #*************************************************************************
    print(80 * '-')
    print('Arquivos de variáveis disponíveis:')
    print('')
    dic_feature_arq_menu = create_feature_arq_menu(db_in)
    print('')
    feature_selection = 1
    # feature_selection = input('Qual arquivo de variáveis deseja analisar?')
    feature_selected = dic_feature_arq_menu[int(feature_selection)]
    print('Arquivo de variáveis selecionado: ' + str(feature_selected))

    #*************************************************************************

    print(80 * '-')
    print('Arquivos de descrições disponíveis:')
    print('')
    dic_description_arq_menu=create_desc_arq_menu(db_in)
    print('')
    description_selection = feature_selection
    # description_selection = input('Qual arquivo de descrição deseja analisar?')
    description_selected = dic_description_arq_menu[int(description_selection)]
    print('Arquivo de descrições selecionado: ' + str(description_selected))
    print(80 * '-')

    #*************************************************************************

    filename_feature=db_in+str(feature_selected)
    #print(filename_feature)

    filename_description=db_in+str(description_selected)
    #print(filename_description)
    print('')

    # *************************************************************************

    df_feature = pd.read_csv(filename_feature, sep='|')
    #print(df_feature)

    df_description = pd.read_csv(filename_description, sep='|')
    #print(df_description)

    return (df_feature, df_description,filename_feature,filename_description)

##########################################################################################
def apaga_arquivo_sintetico(db_in):

    for file in os.listdir(db_in):
        #print(db_in+file)
        if os.path.isfile(db_in+file) and file.startswith('zarq_'):
            try:
                os.remove(db_in+file)
                #print('excluído')

            except Exception:
                print('Exception')


##########################################################################################

def arquivos_sinteticos(db_in,repetition,num_arquivos,df_feature,colunas_arquivos,frac,frac_aleatorio):
    np.random.seed(10)

    arquivos=[]

    if repetition==1:
        print('')
        print('Arquivos com diferentes quantidades de colunas')
        print('')

        colunas = list(df_feature.columns)
        print(colunas)
        print('Quantidade de colunas no dataframe de características: '+str(len(colunas)))
        linhas = df_feature.shape[0]
        print('Quantidade de linhas no dataframe de características: '+str(linhas))
        print('')

        for i in range(num_arquivos):

            print(''.center(70, '*'))
            x = np.random.randint(low=0, high=len(colunas), size=(1, colunas_arquivos-2))
            lista=x[0]
            my_set={*lista}
            vector=[*my_set]
            vector.insert(0, 0)
            vector={*vector}
            vector = [*vector]
            vector.append(len(colunas) - 1)


            print('Arquivo:' + str(i), ' - ', 'colunas:', len(vector), ' - ', vector)

            zarq=list()

            print('')
            for z in vector:
                print(colunas[z])
                zarq.append(colunas[z])
            print('')

            print('Layout')
            print(df_feature[zarq].head(3))

            l = str(i).zfill(2)
            #print(l)
            nome_arquivo = str(db_in) + 'zarq_' + str(l)+'_repetition_'+ str(repetition) + '.csv'

            #nome_arquivo = str(db_in) + 'zarq_' +'repetition_'+ str(i) + '.csv'
            print(nome_arquivo)

            if frac_aleatorio == 1:
                frac = np.random.rand(1,1)[0][0] # fração do arquivo alvo

            df=df_feature[zarq].sample(frac=frac)
            df.to_csv(nome_arquivo, sep='|', encoding='utf-8', index=False)
            #print(df.shape)

            arquivos.append((str(nome_arquivo) + ' - ' +'shape:' + str(df.shape)))

        print(''.center(70, '*'))

        print('')
        print('Arquivos gerados:')
        for arq in arquivos:
            print(arq)
        print('')

        print(''.center(70, '*'))

    ####################################################################################################

    elif repetition==2:
        print('')
        print('Arquivos quantidades de colunas iguais')
        print('')

        colunas = list(df_feature.columns)
        #print(colunas)
        print('Quantidade de colunas no dataframe de características: '+str(len(colunas)))
        linhas = df_feature.shape[0]
        print('Quantidade de colunas no dataframe de características: '+str(linhas))
        print('')

        for i in range(num_arquivos):

            #print(''.center(70, '*'))
            x = np.random.choice(np.arange(0, len(colunas)), size=(1, colunas_arquivos - 2), replace=False)

            lista=x[0]
            my_set={*lista}
            vector=[*my_set]
            vector.insert(0, 0)
            vector.append(len(colunas)-1)
            #print('Arquivo:' + str(i), ' - ', 'colunas:', len(vector), ' - ', vector)

            zarq=list()

            #print('')
            for z in vector:
                #print(colunas[z])
                zarq.append(colunas[z])
            #print('')

            #print('Layout')
            #print(df_feature[zarq].head(3))

            l = str(i).zfill(2)
            #print(l)
            nome_arquivo = str(db_in) + 'zarq_' + str(l)+'_repetition_'+ str(repetition) + '.csv'
            #print(nome_arquivo)

            df=df_feature[zarq].sample(frac=frac)
            df.to_csv(nome_arquivo, sep='|', encoding='utf-8', index=False)
            #print(df.shape)

            arquivos.append((str(nome_arquivo) + ' - ' +'shape:' + str(df.shape)))

        #print(''.center(70, '*'))

        #print('')
        #print('Arquivos gerados:')
        #for arq in arquivos:
            #print(arq)
        print('')

        print(''.center(70, '*'))
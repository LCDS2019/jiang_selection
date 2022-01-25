##########################################################################################
#load ontology
##########################################################################################
from owlready2 import *
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import pickle

def load_ontology(db_system,onto_path,ontologia):
    print('')
    print(' Ontology load '.center(80, '#'))
    print('')

    path = db_system + ontologia.split('.')[0]+'.graph'
    #print(path)

    if os.path.exists(path)==False:
        create_ontology(ontologia,onto_path)
        data = pickle.load(open(path, "rb"))
        print('Grafo criado: ' + path)
        print('Grafo carregado: ' + path)

    else:
        print('Grafo disponível: ' + path)
        data = pickle.load(open(path, "rb"))
        print('Grafo carregado: ' + path)

    print(nx.info(data, n=None))
    nodes=len(data.nodes())
    print('')


def create_ontology(ontologia,onto_path):
    print(onto_path+onto_path)
    onto = get_ontology(str(onto_path+ontologia)).load()
    print(onto)
    print('******************************')

    G = nx.Graph()

    class root(Thing):
        namespace = onto

    # Apresentação das classes
    classes = list(onto.classes())

    x = []
    s=0
    u=0
    for i in classes:
        s=s+1
        for l in i.is_a:
            u=u+1
            b=str(l).split('.')[-1]
            #print(u,s,i.name,'---------',b)
            G.add_edge(b,i.name)

    #print([e for e in G.edges])

    plt.clf()
    nx.draw(G, with_labels=False, node_size=1,verticalalignment='bottom')
    plt.savefig('./db_out/G_ontologia.png', dpi=300)

    #print(nx.shortest_path(G, source='Algorithm', target='tumor_size'))


    graph_file = './db_system/'+str(ontologia.split('.')[0])+'.graph'

    print('')
    print('Arquivo pikle:')
    print(graph_file)

    nx.write_gpickle(G, graph_file)



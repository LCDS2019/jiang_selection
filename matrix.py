import numpy as np

def arquivos(repetition,lines,colunas_arquivos):
    np.random.seed(10)
    if repetition==1:
        print('')
        print('Lines with repetition')
        print('')

        for i in range(lines):

            x = np.random.randint(low=0, high=150, size=(1, colunas_arquivos))
            lista=x[0]
            my_set={*lista}
            my_list=[*my_set]
            print(i,'-',my_list,'-',len(my_list))

    else:
        print('')
        print('Lines without repetitions')
        print('')

        for i in range(lines):
            your_list = list(np.random.choice(np.arange(0, 150),colunas_arquivos, replace=False))
            print(i,'-',your_list,'-',len(your_list))





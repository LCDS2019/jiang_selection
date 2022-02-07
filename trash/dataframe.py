import pandas as pd

df=pd.DataFrame()


lista=[]
for i in range(1,11):
    lista.append([i,i+1])
    print(i)


print('')
df=pd.DataFrame(lista)
print(df)
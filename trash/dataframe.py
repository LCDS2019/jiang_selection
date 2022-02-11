import pandas as pd

lista=[]
for i in range(1,4):
    lista.append([i,i+1])

print('')
df1=pd.DataFrame(lista)
df1.reset_index(drop=True, inplace=True)
df1.index.names = ['indice']
df1.columns = ['a', 'b']

df2=pd.DataFrame([[3,1],[2,2]])
df2.reset_index(drop=True, inplace=True)
df2.index.names = ['indice']
df2.columns = ['a', 'b']


print('')
print(df1)

print('')
print(df2)

print('')

u=0
for i in df1.values:
    l=str(u).zfill(2)
    print(l)
    print(i)

    for j in df2.values:
        print(j)
        if i[0]==j[0]:
            i[1] = j[1]
    u=u+1
    print('---------------')

print(df1)

df1.reset_index()
print(df1.index.values)
print(df1.at[0,'a'])




'''
data = []
for i in df.values:
    tmp = i
     if 'leo' in i[0] :
        tmp[2] = 'GRU'
     data.append(tmp)
'''


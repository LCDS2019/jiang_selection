import matplotlib.pyplot as plt
import numpy as np
import math
from numpy import dot
from numpy.linalg import norm
import pandas as pd
from random import randint

ax = plt.axes()

vref=[0,0,1,1]
ref=[1,1]

vectors=[
[0,0,.1,.2],
[0,0,.1,.5],
[0,0,.4,.4],
[0,0,.9,.5],
[0,0,.9,.8],
[0,0,.9,.9],
[0,0,.3,.9]

]

res_lista=[]
df=pd.DataFrame()

u=0
for i in vectors:
    vec=i[2:4]
    result = dot(ref, vec) / (norm(ref) * norm(vec))
    res_lista.append([u,vec, result])
    u=u+1


#for i in res_lista:
    #print(i)

from operator import itemgetter
ranking=sorted(res_lista, key=itemgetter(2), reverse=True)

print('*****************************')
for i in ranking:
    print(i)
print('*****************************')


color = []
n = len(vectors)
for i in range(n):
    color.append('#%06X' % randint(0, 0xFFFFFF))


ax.arrow(vref[0], vref[1], vref[2], vref[3], head_width = 0.01,head_length = 0.0 , color='black')
ax.text(vref[2], vref[3], "Ref", fontsize=12, rotation=0)
j=0
for i in res_lista:
    ax.arrow(0, 0, i[1][0], i[1][1], head_width=0.01, head_length=0.0, color=color[j])
    ax.text(i[1][0], i[1][1], ' '+str(j), fontsize=12, rotation=0)
    j=j+1

plt.grid()
plt.xlim(0,1.2)
plt.ylim(0,1.2)
plt.show()
plt.close()

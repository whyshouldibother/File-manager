import matplotlib.pyplot as plt
import os
import sys
import numpy as np

path=sys.argv[1]
if (path=='.'): path = os.getcwd()
path=path.replace('~','C:/Users/HP')
files=os.listdir(path)
path_=path+'/'

f=[i for i in files if i.startswith('file-')]

x=[len(os.listdir(path_+i)) for i in f]
plt.subplot(2,2,1)
plt.pie(x,labels=f)
plt.subplot(2,2,2)
plt.bar(f,x)

x=[]
for i in f:
    size=0
    for j in os.listdir(path_+i):
        size+=os.path.getsize(path_+i+'/'+j)
    x.append(size)
plt.subplot(2,2,3)
if(np.any(x)):plt.pie(x, labels=f)

plt.subplot(2,2,4)
plt.bar(f,x)
plt.show()
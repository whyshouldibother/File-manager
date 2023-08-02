import os 
import sys

path=sys.argv[1]
path=path.replace('~','C:/Users/HP')
files=os.listdir(path)
path_=path+'/'
folder=path_+'file-'

f=[i for i in files if os.path.isfile(path_+i)]

def sn(path):
    return len(os.listdir(path))

for i in f:
    try:
        try:
            os.rename(path_+i,f"{folder}{i[i.rindex('.')+1:len(i)]}/{sn(folder+i[i.rindex('.')+1:len(i)])}-{i}")
        except:
            os.mkdir(folder+i[i.rindex('.')+1:len(i)])
            os.rename(path_+i,f"{folder}{i[i.rindex('.')+1:len(i)]}/{sn(folder+i[i.rindex('.')+1:len(i)])}-{i}")
    except:
        try:
            os.rename(path_+i,f"{folder}/others/{sn(folder+'/others/')}-{i}")
        except:
            os.mkdir(folder+'others')
            os.rename(path_+i,f"{folder}/others/{sn(folder+'/others/')}-{i}")

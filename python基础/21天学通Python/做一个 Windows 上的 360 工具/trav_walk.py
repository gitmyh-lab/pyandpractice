#
# file:trav_walk.py
import os,os.path
def trav_walk(pathname):
    #返回一个元组（root, dirs, files），其中的root表示当前目录，dirs是当前目录下的所有子
    #目录，而files则表示当前目录下的所有文件
    for root,dirs,files in os.walk(pathname):
        for fil in files:
            fname=os.path.abspath(os.path.join(root,fil))
            print(fname)
trav_walk("d:/python34")
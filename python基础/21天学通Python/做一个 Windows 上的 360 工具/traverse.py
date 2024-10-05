# coding:utf-8 #
# file:traverse.py
import os,os.path
def traverse(pathname):#对目录进行遍历
    for item in os.listdir(pathname):
        fullitem = os.path.join(pathname,item)
        print(fullitem)
        if os.path.isdir(fullitem): #判断是否为目录
            traverse(fullitem)
traverse("d:/python34")
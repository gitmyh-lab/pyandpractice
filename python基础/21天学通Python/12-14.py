# -*- coding:utf-8 -*- #
import tkinter # 导入 tkinter 模块
import tkinter.filedialog # 导入 tkFileDialog 模块
def FileOpen(): # 按钮事件处理函数
    r = tkinter.filedialog.askopenfilename(title = 'Python tkinter',# 创建打开文件对话框
            filetypes=[('Python', '*.py *.pyw'),('All files', '*')] )
    # 指定文件类型为 Python 程序
    print(r) # 输出返回值
def FileSave(): # 按钮事件处理函数
    r = tkinter.filedialog.asksaveasfilename(title = 'Python tkinter',
            # 创建保存文件对话框
            initialdir=r'E:\Python\code', # 指定初始化目录
            initialfile = 'test.py') # 指定初始化文件
    print(r)
root = tkinter.Tk()
button1 = tkinter.Button(root,text = 'File Open',# 创建按钮
            command = FileOpen) # 指定按钮事件处理函数
button1.pack(side='left')
button2 = tkinter.Button(root,text = 'File Save',
            command = FileSave) # 指定按钮事件处理函数
button2.pack(side='left')
root.mainloop() # 进入消息循环
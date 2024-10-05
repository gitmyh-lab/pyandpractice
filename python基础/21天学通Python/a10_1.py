#导入 foo 模块函数
from foo import foo_fun #导入 foo 模块中的函数 foo_fun
name = 'Current module' #定义全局变量 name
def bar(): #定义普通函数 bar()
    print('当前模块中函数 bar:')
    print('变量 name：',name) #输出全局变量 name
def call_foo_fun(fun): #定义调用传入函数作为参数的函数
    fun() #调用传入的函数

if __name__ == '__main__':
    bar() #调用本模块中定义的函数 bar()
    print()
    foo_fun() #调用从模块 foo 中导入的函数 foo_fun()
    print()
    call_foo_fun(foo_fun)
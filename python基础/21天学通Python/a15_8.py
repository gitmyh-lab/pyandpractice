#使用 Popen 产生子进程的方式执行了 python 源代码
import subprocess
prcs = subprocess.Popen(['python','protest.py'],
                    stdout=subprocess.PIPE,
                    stdin=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    universal_newlines=True,
                    shell=True)
#用于和子进程交互；发送标准输入数据；返回由标准输出和错误输出构成的元组。
prcs.communicate('These strings are from stdin.')
print("subprocess pid:",prcs.pid)#子进程的 pid；
print('\nSTDOUT:')
print(str(prcs.communicate()[0]))
print('STDERR:')
print(prcs.communicate()[1])
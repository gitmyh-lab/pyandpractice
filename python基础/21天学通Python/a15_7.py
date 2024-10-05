import subprocess
##创建新进程运行程序，输入和输出绑定到父进程，返回新进程退出码
print('call() test:',subprocess.call(['python','protest.py']))
print('')
#创建新进程运行程序，输入和输出绑定到父进程，退出码为 0 正常返回，否则，引发
#CalledProcessError
print('check_call() test:',subprocess.check_call(['python','protest.py']))
print('')
#创建新进程运行程序，元组形式返回新进程退出码和输出
print('getstatusoutput() test:',subprocess.getstatusoutput(['python','protest.py']))
print('')
#创建新进程运行程序，返回新进程的输出（字符串）
print('getoutput() test:',subprocess.getoutput(['python','protest.py']))
print('')
#创建新进程运行程序，返回新进程的输出（bytesarray）
print('check_output() test:',subprocess.check_output(['python','protest.py']))
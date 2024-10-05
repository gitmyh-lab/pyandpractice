#communicate()方法在子进程间传递信息（类似传递上交花束）
import subprocess
processes = []
psum = 5
for i in range(psum):
    processes.append(subprocess.Popen(['python','protest9.py'],
                    stdout=subprocess.PIPE,
                    stdin=subprocess.PIPE,
                    universal_newlines=True,
                    shell=True))
processes[0].communicate('0 bouquet of flowers!')
for before,after in zip(processes[:psum],processes[1:]):
    after.communicate(before.communicate()[0])
print('\nSum of Processes :%d' % psum)
print()
for item in processes:
    print(item.communicate()[0])
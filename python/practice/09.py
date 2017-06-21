'''
题目：暂停一秒输出。

注：sublime text 编译执行无法看出边输出边等待效果，后面会一次性输出
	当放到python idle后，就能得到效果了
'''

#方法1：
import time
def func1():
	print("start")
	time.sleep(1)
	print("end")

	for x in range(1, 30):
		print(x)
		time.sleep(1)

func1()
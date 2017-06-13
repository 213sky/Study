'''
输出 9*9 乘法口诀表。
'''

def func1():
	for i in range(1, 10):
		for j in range(i, 10):
			print("%2d * %2d = %2d" %(i, j, i*j), end = " ")

		print()

func1()


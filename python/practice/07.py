'''
题目：将一个列表的数据复制到另一个列表中。
'''

#方法1：通过循环队列，将数据依次插入新队列中
def func1():
	l = [1, 2, 3, 4, 5, 7]
	newL = []
	for x in l:
		newL.append(x)

	print(l)

#方法2：通过[:]方式
def func2():
	l = [1, 2, 3, 4, 5, 7]
	newL = l[:]

	print(newL)

#方法3：列表生成式:
def func3():
	l = [1, 2, 3, 4, 4,5,9 ,5]

	newL = [x for x in l]
	print(newL)

func3()
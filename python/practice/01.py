#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

#方法1：三个循环，并且判断3个值不相等
def func1():
	for x in range(1,5):
		for y in range(1,5):
			for z in range(1,5):
				if x != y and y != z and x != z:
					print("%d %d %d" %(x, y, z))


#方法2：基本逻辑跟方法1一致，实现上通过一句写出
def func2():
	d = [str(x) + " " + str(y) + " " + str(z) for x in range(1,5) for y in range(1, 5) for z in range(1, 5) if x != y and x != z and y !=z]
	for t in d:
		print(t)

#方法3：通过系统自带函数permutations完成
from itertools import permutations
def func3():
	for i in permutations(range(1, 5), 3):
	    for x in i:
	    	print(x, end=" ") #print输出不换行
	    print()
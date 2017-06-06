#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

#方法1：三个循环，并且判断3个值不相等
def func1():
	for x in range(1,5):
		for y in range(1,5):
			for z in range(1,5):
				if x != y and y != z and x != z:
					print("%d %d %d" %(x, y, z))


def func2():
	d = []
	for x in range(1,5):
		for y in range(1,5):
			for z in range(1,5):
				d.append(x*100 + y *10+z)

	for t in d:
		print(t)


from itertools import permutations

for i in permutations([1, 2, 3, 4], 3):
    print(i)
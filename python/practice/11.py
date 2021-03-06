'''
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
'''

'''
最后通过结果观察，符合
Python 练习实例-(06)
题目：斐波那契数列。
'''

d1 = 0
d2 = 0
d3 = 0

for x in range(1, 100):
	if x == 1:
		d1 = 1
		continue
	
	d1, d2, d3 = d3+d2, d1, d3+d2

	print("month %d --> %d"% (x, (d1+d2+d3)))



'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
'''

#方法1：直接对3个数做大小比对
#单整数越多，需要大量的判断逻辑，比较麻烦
def func1(a, b, c):
	#我们最后结果 a < b < c
	if a > b:
		a, b = b, a

	if a > c:
		a, c = c, a

	if b > c:
		b, c = c, b

	print("%s %s %s" % (a, b, c))

#方法2：将3位数写入数组中，并调用内置排序或自己写排序方法
#缺点当数值越多，变量写的越多
def func2(a, b, c):
	val = []
	val.append(a)
	val.append(b)
	val.append(c)

	val.sort()

	for x in val:
		print(x)

#方法3：使用可变参数传值
def func3(*a):
	val = []
	for y in a:
		val.append(y)

	val.sort()
	for x in val:
		print(x, end = " ")

	print()



func3(12, 123, 11)

'''
题目：斐波那契数列。

斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
'''

#方法1：通过不断循环的方式
def func1(n):
	if n == 0:
		print(0)
		return

	if n == 1:
		print(1)
		return

	last2 = 0
	last1 = 1

	for x in range(2, n):
		last1, last2 = last1 + last2, last1	

	print(last1 + last2)

#方法2：使用递归方式
def func2(n):
	if n == 0:
		return 0

	if n == 1:
		return 1
	
	return func2(n - 1) + func2(n - 2)

#方法3：使用yield方式
def func3(n):
	if n == 0:
		yield 0

	if n == 1:
		yield 1

	last2 = 0
	last1 = 1

	for x in range(2, n + 2):
		last1, last2 = last1 + last2, last1	
		yield last1



#show func1
#for x in range(100):
#	func1(x)	
#func1(10)
#print(func2(10))

#t = func3(10)

for x in func3(1000):
	print(x)



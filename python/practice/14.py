'''
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。


程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
'''

#方法1:可以使用递归方式
def func11(num, n, l=[]):
	if n < 2:
		n = 2

	isEnd = True
	for x in range(n, num):
		if num % x == 0:
			#print(num, " --> ", x)
			l.append(x)
			func11(int(num / x), x, l)
			isEnd = False
			break;

	if isEnd:
		l.append(int(num))

l = []
num = 1000
func11(num, 2, l)
if l[0] == num:
	print("%d 不能分解因数" % num)
else:
	print(num, end="=")
	for x in range(0, len(l)):
		if x != len(l) - 1:
			print(l[x], end="*")
		else:
			print(l[x])
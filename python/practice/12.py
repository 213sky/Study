'''
题目：判断101-200之间有多少个素数，并输出所有素数。

判断素数的方法：
1.用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 
2.质数又称素数。一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数；否则称为合数
'''



def IsSuShu(num):
	for x in range(2, num):
		if num % x == 0:
			#print(num, " ---> ", x)
			return False

	return True

for x in range(101, 201):
	if IsSuShu(x):
		print(x, end= " ")

print()


'''
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
'''

import math

for  x in range(0,10):
	for y in range(0, 10):
		for z in range(0, 10):
			xyz = x * 100 + y * 10 + z
			#xyz3 = x*x*x + y*y*y + z*z*z
			xyz3 = math.pow(x, 3) + math.pow(y, 3) + math.pow(z, 3)
			if xyz == xyz3 and xyz / 100 >= 1: #确保是3位数
				print(xyz, end= " ")

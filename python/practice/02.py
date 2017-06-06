#
'''
题目：企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%;
高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？
'''
#单位：万元

#通过if一个一个判断取值
def func1(val):
	money = 0

	if val <= 10:
		money += val * 0.1
		print(money)
		return
	else:
		money += (10-0) * 0.1

	if val > 10 and val <= 20:
		money += (val - 10) * 0.075
		print(money)
		return
	else:
		money += (20 - 10) * 0.075

	if val > 20 and val <= 40:
		money += (val - 20) * 0.05
		print(money)
		return
	else:
		money += (40 - 20) * 0.05

	if val > 40 and val <=60:
		money += (val - 40) * 0.03
		print(money)
		return
	else:
		money += (60 - 40) * 0.03

	if val > 60 and val <=100:
		money += (val - 60) * 0.015
		print(money)
		return
	else:
		money += (100 - 60) * 0.015

	if val > 100:
		money += (val - 100) * 0.01
		print(money)
		return



#方法2：通过数组方式安装
import sys

def func2(val):
	profits = [0, 10, 20, 40, 60, 100, sys.maxsize]  #此处增加一个sys.maxsize可以在后期逻辑上的得到简化
	ratio = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]

	money = 0
	for pro in range(0, 6):
		if val > profits[pro] and val <= profits[pro + 1]:
			money += (val - profits[pro]) * ratio[pro]
		elif val > profits[pro + 1]:
			money += (profits[pro + 1] - profits[pro]) * ratio[pro]

	print(money)

#-------------------------------------------------------------
#正序的判断比较麻烦，更加推荐逆序的方式进行。以下将进行逆序方式
#-------------------------------------------------------------

#方法3：通过if一个一个判断取值
def func3(val):
	i = val 
	money = 0

	if i > 100:
		money += (i - 100) * 0.01
		i = 100

	if i > 60:
		money += (i - 60) * 0.015
		i = 60

	if i > 40:
		money += (i - 40) * 0.03
		i = 40

	if i > 20:
		money += (i - 20) * 0.05
		i = 20

	if i > 10:
		money += (i - 10) * 0.075
		i = 10

	money  += i * 0.1

	print(money)

#方法4：通过数组方式安装
def func4(val):
	i = val
	arr = [100,60,40,20,10,0]
	rat = [0.01,0.015,0.03,0.05,0.075,0.1]
	r = 0
	for idx in range(0,6):
	    if i>arr[idx]:
	        r+=(i-arr[idx])*rat[idx]
	        i=arr[idx]
	print(r)


func1(100)
func2(100)
func3(100)
func4(100)
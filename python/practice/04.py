# encoding=utf8

'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
'''

#方法1：通过数组的方式记录每个月天数，闰年另外计算
#也可以拿dict来记录每个月天数
def func1(year, month, day):
	days = [31, 28, 31,30,31,30,31,31,30,31,30,32]

#闰年判断方法，能被4整除的大多是闰年；能被100整除而不能被400整除的年份不是闰年；能被3200整除的也不是闰年
	if year % 4 == 0 and year % 100==0 and year % 400 !=0 and year % 3200 != 0:  
		days[1] = 29

	if month > len(days):
		print("月份输入有误")
		return

	if days[month - 1] < day or day <= 0:
		print("日期输入有误")
		return

	allday = 0
	for x in range(0, month - 1):
		allday += days[x]
	allday += day

	print(allday)


func1(2015, 6, 32)

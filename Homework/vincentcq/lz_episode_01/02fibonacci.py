'''
Vincent's Python 

——python知识星球02_斐波那契数列
'''

num = int(input('\n请输入需要展示的斐波那契数列个数：'))

a0 = 0
a1 = 1
sum = 1

if num == 0:
	print('\n亲，请不要开玩笑...\n')  #这是输入数字为0的情况，不计算和

else:
	if num > 1:						#排除为1的情况，通过while语句算出每个值并累加
		print('\n以下是%s个斐波那契数列：\n' % num, a1, end='、')
		while num > 1:
			num -=1
			s = a0 +a1     #s表示n位，a1表示n-2位，a2表示n-1位，n位=(n-2)位+(n-1)位
			a0 = a1			#每个n一次递进一个斐波那契数
			a1 = s
			sum =s + sum	#累加和
			print(s,end='、')
	else:
		print('\n以下是%s个斐波那契数列：\n 1' % num)  #这是输入为1的情况，单独显示

	print('\n\n这组斐波那契数列之和为：%s \n' % sum)


		
'''
Vincent's Python 

——python知识星球01_检测输入的是不是质数
'''
#输入一个整数
num =int(input('请输入一个用于判断是否是质数的整数：'))


for i in range(2,(num - 1)):			   #2开始num-1结束用于排除被1和自己整除
	s = num % i							   #对num求余，余数为零说明能够被整除，
	print('除以%s，余%s' % (i,s))		   #用来显示判断过程参数变化，不需要可注销
	if s==0: break						   #循环中如果遇到余数为0，说明该数为合数，随即弹出循环体，结束剩下判断
else: print("\n %s 是一个质数。\n" % num)  #正常循环完成没有被break，说明是质数

#如果是被Break出来的，说明S为0了，说明输入的不是质数
if s==0:
	print('\n %s 不是质数，因为它能够被%s整除' % (num, i))

	
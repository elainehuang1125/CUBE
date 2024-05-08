in_num = input('請輸入數字 :')
in_num = int(in_num)
print('輸入數字為:', in_num )

def triangle(num):
	star = 1
	for i in range(num):
		if i == 0:
			star_ = format("*"*star,"^"+str(num*2-1))
		elif i == num-1:
			star_ = format("*"+"*"*(star-2)+"*","^"+str(num*2-1))
		else:
			star_ = format("*"+" "*(star-2)+"*","^"+str(num*2-1))
		star += 2

		print(star_)

triangle(in_num)
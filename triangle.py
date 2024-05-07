in_num = input('請輸入數字 :')
print('請輸入數字'+ in_num )
in_num = int(in_num)
print('輸入數字為:', in_num )


def triangle(num):
	star = 1
	for i in range(num):
		if i == 0 :
			star_ = format("*"*star,"^"+str(num*2-1))
		elif i % 2 == 0 :
			star_ = ""
			for j in range(num+2):
				if j % 2 == 0 :
					star_ = star_ + "*"
				else :
					star_ = star_ + " "
		else:
			star_ = ""
			for j in range(num+2):
				if j % 2 != 0 :
					star_ = star_ + "*"
				else :
					star_ = star_ + " "

		print(star_)
		

triangle(in_num)
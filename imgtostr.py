from PIL import Image
f=Image.open("./test1.jpg")

for i in range(0,4): 
	f.crop((20+20*i,0,40+20*i,40)).save("test{}.jpg".format(i+1))


# f.crop((20+20*0,0,40+20*0,40)).save("./test/test1-1.jpg")
# f.crop((20+20*1,0,40+20*1,40)).save("./test/test1-2.jpg")
# f.crop((20+20*2,0,40+20*2,40)).save("./test/test1-3.jpg")
# f.crop((20+20*3,0,40+20*3,40)).save("./test/test1-4.jpg")

# def TotallyShit(im): 
# 	x,y=im.size mmltilist=list() 
# 	for i in range(x): 
# 		for j in range(y): 
# 			if im.getpixel((i,j))<200: 
# 				mmltilist.append(1) 
# 		else: mmltilist.append(0)
# 		return mmltilist

# from sklearn.neural_network
# import MLPClassifier 
# import numpy as np 
# def clf(): 
# 	clf=MLPClassifier() 
# 	mmltilist=list() 
# 	X=list() 
# 	for i in range(0,12): 
# 		for j in os.listdir("douplings/douplings-{}".format(i)): 
# 			mmltilist.append(TotallyShit(Image.open("douplings/douplings-{0}/{1}".format(i,j)).convert("L"))) 
# 			X.append(i) 
# 			clf.fit(mmltilist,X) 
# 			return clf


#  def get_captcha(self): 
#  	with open("test.jpg","wb") as f: 
#  		f.write(self.session.get(self.live_captcha_url).content) 
#  		gim=Image.open("test.jpg").convert("L") 
#  		recognize_list=list() 
#  		for i in range(0,4): 
#  			part=TotallyShit(gim.crop((20+20*i,0,40+20*i,40))) 
#  			np_part_array=np.array(part).reshape(1,-1) 
#  			predict_num=int(self.clf.predict(np_part_array)[0]) 
#  			if predict_num==11: 
#  				recognize_list.append("+") 
#  			elif predict_num==10: recognize_list.append("-") 
#  		else: recognize_list.append(str(predict_num)) 
#  		return ''.join(recognize_list)



#https://zhuanlan.zhihu.com/p/22986915
# for j in range(0,500):
#     f=Image.open("../test{}.jpg".format(j))
#     for i in range(0,4):
#         f.crop((20+20*i,0,40+20*i,40)).save("test{0}-{1}.jpg".format(j,i+1))

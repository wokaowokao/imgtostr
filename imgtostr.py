from PIL import Image
f=Image.open("./test/test1.jpg")

f.crop((20+20*0,0,40+20*0,40)).save("./test/test1-1.jpg")
f.crop((20+20*1,0,40+20*1,40)).save("./test/test1-2.jpg")
f.crop((20+20*2,0,40+20*2,40)).save("./test/test1-3.jpg")
f.crop((20+20*3,0,40+20*3,40)).save("./test/test1-4.jpg")
#https://zhuanlan.zhihu.com/p/22986915
# for j in range(0,500):
#     f=Image.open("../test{}.jpg".format(j))
#     for i in range(0,4):
#         f.crop((20+20*i,0,40+20*i,40)).save("test{0}-{1}.jpg".format(j,i+1))

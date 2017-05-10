# coding:utf-8
import itchat
import re
import matplotlib.pyplot as plt 
from pylab import *
from wordcloud import WordCloud 
import jieba 


class wechat(object):
	def __init__(self):
		# 先登录
		itchat.login()
		# 获取好友列表
		friends = itchat.get_friends(update=True)[0:]
		tList = []
		fileName = 'Signature.txt'
		with open(fileName, 'w') as fp:
			for i in friends:# 获取个性签名
				signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "")# 正则匹配过滤掉emoji表情，例如emoji1f3c3等
				rep = re.compile("1f\d.+")
				signature = rep.sub("", signature)
				tList.append(signature)
				fp.write('%s \n' % signature.encode('utf8'))	

		# 拼接字符串
		text = "".join(tList)
		# jieba分词import jieba
		wordlist_after_jieba = jieba.cut(text, cut_all = True) 
		wl_space_split = " ".join(wordlist_after_jieba) 
		backgroud_Image = plt.imread('timg.jpg')
		my_wordcloud = WordCloud(font_path='/Users/xuqidong/itChat/SimHei.ttf',background_color = 'white',mask = backgroud_Image,)
		my_wordcloud.generate(wl_space_split) 
		plt.imshow(my_wordcloud) 
		plt.axis("off") 
		plt.show()
		

	



if __name__ == '__main__':
	get = wechat()


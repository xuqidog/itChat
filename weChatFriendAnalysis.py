# -*- coding: utf-8 -*-
import itchat
from echarts import Echart, Legend, Series, Axis, Bar
from collections import Counter
import jieba.analyse
import time

# 自动登录
itchat.login()
# 获取好友列表
friends = itchat.get_friends(update=True)[0:]
fileName = 'Signature.txt'
with open(fileName, 'w') as fp:
	for i in friends:
		Province = i["Province"].encode('utf8')
		# City = i["City"].encode('utf8')
		if len(Province)!=0:
			fp.write('%s \n' % Province)


# 统计
bill_path = r'Signature.txt'
bill_result_path = r'cityCount.txt'
with open(bill_path,'r') as fr:
        data = jieba.cut(fr.read())
data = dict(Counter(data))
valueList = []
nameList = []
with open(bill_result_path,'w') as fw:
    for k,v in data.items():
    	if len(k)>=2:
    		valueList.append(v)
    		nameList.append(k)
	        fw.write("%s,%d\n" % (k.encode('utf-8'),v))


# 输出HTML
# html_path = r'outecharts.html'
# lines_path = r'echarts.html'
# lines = open(lines_path).readlines()
# html = open(html_path,'w')
# line = 0
# for s in lines:
# 	line = line + 1
# 	if line==32:
# 		html.write('data: %s\n' % valueList)
# 	if  line==26:
# 		html.write('data: [')
# 		for str in nameList:
# 			html.write('\"%s\",' % str.encode('utf-8'))
# 		html.write(']\n')
# 	else:
# 		html.write(s)

    	


# 用echart画图
chart = Echart(u'WeChat 好友省份分布图', 'data from xuqidong')
chart.use(Bar('China', valueList))
chart.use(Legend(['GDP']))
chart.use(Axis('category', 'left', data=nameList))
chart.plot()


# 获取好友列表
# friends = itchat.get_friends(update=True)[0:]
# 初始化计数器，有男有女，当然，有些人是不填的
male = female = other = 0
# 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算
# 1表示男性，2女性
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
        # 总数算上，好计算比例啊～
        total = len(friends[1:])
        # 好了，打印结果
print u"男性好友：%.2f%%" % (float(male) / total * 100)
print u"女性好友：%.2f%%" % (float(female) / total * 100)
print u"其他：%.2f%%" % (float(other) / total * 100)

# 用echart画饼图
chart = Echart(u'%s的微信好友性别比例' % (friends[0]['NickName']), 'from WeChat by xuqidong')
chart.use(Pie('WeChat',
              [{'value': male, 'name': u'男性 %.2f%%' % (float(male) / total * 100)},
               {'value': female, 'name': u'女性 %.2f%%' % (float(female) / total * 100)},
               {'value': other, 'name': u'其他 %.2f%%' % (float(other) / total * 100)}],
              radius=["50%", "70%"]))
chart.use(Legend(["male", "female", "other"]))
del chart.json["xAxis"]
del chart.json["yAxis"]
chart.plot()
		

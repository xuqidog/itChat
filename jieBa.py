#!/usr/bin/env python
#coding = utf8
from collections import Counter
import jieba.analyse
import time

bill_path = r'Signature.txt'
bill_result_path = r'cityCount.txt'
with open(bill_path,'r') as fr:
        data = jieba.cut(fr.read())
data = dict(Counter(data))
with open(bill_result_path,'w') as fw:
    for k,v in data.items():
        fw.write("%s,%d\n" % (k.encode('utf-8'),v))
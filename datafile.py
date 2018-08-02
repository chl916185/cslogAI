import os.path as path
import os
import collections
import numpy as np
import jieba
import time
import re

phonenum = []
def phonenum_extract(log):
    if log is None or len(log) == 0:
        return None

    m = re.match('[0-9]{1}',log)
    return m

# 打开文本文件
numWords = []
with open('train_log.txt', "r", encoding='gbk') as f:
    line = f.readline()
    while line:
        #print('line=',line)
        #每一行的文本分词后以list形式存储到wordlist中
        wordlist = list(jieba.cut(line, cut_all=False))
        counter = len(wordlist)
        #print(wordlist)
        numWords.append(counter)
        line = f.readline()

        phonenum = re.findall('/^(13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89])\d{8}$/',wordlist)
        print(phonenum)

numFiles = len(numWords)
#print(numWords)

#识别手机号
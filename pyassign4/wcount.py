"""
wcount.py:输入相应的参数后返回相应的


__author__="wengpeiyi"
__pkuid__="1800011749"
__email__="594592395@qq.com"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    
    for i in ", . : ; ? ! # / \ * _ ] [ ) ( & ":
        lines = lines.replace(i, " ")
    #与下一步有重复之嫌，但由于文中有括号等标点，直接删除非字母元素会导致误差
    for i in range(len(lines)):
        if lines[i].isalpha() == False:
            lines = lines.replace(lines[i], " ")
    lines = lines.lower()
    lines = lines.split()
    
    d = {}
    for i in range(len(lines)):
        if not lines[i] in d:
            d[lines[i]] = 1;
        if lines[i] in d:
            d[lines[i]] += 1
    #字典计数
    s = d.items()
    t = []
    for i in s:
        t.append(i)
    
    ans = quicksort(t)
    if topn <= len(ans):
        ans = ans[:topn]
    for i in ans:
        print(i[0], " ", i[1])

    # your code goes here
    pass


def y(x):
    """quicksort的一个辅助函数"""
    return x[1]


def quicksort(lst):
    """一个排序函数，给列表的列表排序"""
    return sorted(lst, key=y, reverse=True)


if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    elif len(sys.argv) == 2:
        address = ""
        address += sys.argv[1]
        try:
            doc = urlopen(address)
            docstr = doc.read()
            doc.close()
            lines = docstr.decode()
            wcount(lines, 10)
        except OSError:
            print("Sorry, 404: not Found")
            
    elif len(sys.argv) == 3:
        address = ""
        address += sys.argv[1]
        doc = urlopen(address)
        docstr = doc.read()
        doc.close()
        lines = docstr.decode()
        n = int(sys.argv[2])/2
        wcount(lines, int(n))
    else:
        print("Sorry, invalid input. ")
        print("Only 2 parameters are allowed.")
    # your code goes here
    # should anayze whether paras are right or not

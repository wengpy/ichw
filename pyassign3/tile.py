# -*- coding: utf-8 -*-
"""
Tile.py:输入相应的参数后返回可能的所有铺砖方案，并在用户选择其中一种后输出对应的图形。

__author__ = "wengpeiyi"
__pkuid__ = "1800011749"
__email__ = "594592395@qq.com"
"""

import turtle
import copy
import time
colors=['red', 'yellow', 'blue', 'green2', 'chocolate1',
        'blueviolet', 'white', 'snow4', 'violet', 'cyan3']
m = int(input("墙长： "))
n = int(input("墙宽： "))
a = int(input("砖长： "))
b = int(input("砖宽： "))
m, n = max(m, n), min(m, n)
a, b = max(a, b), min(a, b)
s = m*n
total = [0]*s        
Ans = [0]*s
Final = []


def test():
    """初步检测砖是否可铺"""
    x = (m*n)/(a*b)
    if a > m or b > n or not int(x)-x == 0:
        return False
    else:
        for i in range(int(m/a)+1):
            if (m-a*i)%b == 0:
                for c in range(int(n/b)+1):
                    if (n-b*c)%a == 0:
                        return True
        return False

    
def picture(num):
    """用于将铺法可视化
    num:用户输入的序列号
    """
    t = turtle.Turtle()
    listb = [0]*m*n
    li = Final[num]
    for i in range(len(li)):
        for j in li[i]:
            listb[j] = i+1
    for i in range(len(listb)):
        t.up()
        t.shape("square")
        t.shapesize(1, 1, None)
        t.fillcolor(colors[listb[i]%10])
        t.goto(20*(i%m)-10*m, 20*int(i/m)-10*m)
        t.stamp()


def h(num):
    """砖的一个状态函数，用于检测某一区域能否横铺或竖铺并反馈相应的状态
    num:区域的序列号
    """
    global total
    global Ans
    f = m - num%m
    g = n-int(num/m)
    
    if Ans[num] > 0:
        return 0;
    else:
        if f < b or g < b :
            return -1;
        if f < a and g < a:
            return -1;
        if b <= f < a and g >= a:
            total[num] = 1
            return 1;
        if f >= a  and b <= g < a:
            for i in range(b, f):
                if Ans[num+i] > 0:
                    return -1;
                else:
                    total[num] = 3
                    return 3;
        if f >= a and g >= a:
            for i in range(b, f):
                if Ans[num+i] > 0:
                    total[num] = 1
                    return 1;
                else:
                    total[num] = 2
                    return 2;
        
        
def markB(k, num, summary):
    """竖铺，通过全局变量记录已铺的区域
    k:砖的序列号
    num:区域的序列号
    summary:记录铺法
    """
    global Ans
    ans = ()
    for i in range(int(a)):
        for j in range(int(b)):
            Ans[num + j + i*m] = k
            ans += (num + j + i*m,)
    summary.append(ans)
    return Ans


def markA(k, num, summary):
    """横铺，通过全局变量记录已铺的区域
    k:砖的序列号
    num:区域的序列号
    summary:记录铺法
    """
    global Ans
    ans = ()
    for i in range(int(b)):
        for j in range(int(a)):
            Ans[num + j + i*m] = k
            ans += (num + j + i*m,)
    summary.append(ans)
    return Ans


def g(x,summary):
    """通过状态函数的反馈实现铺满，在可横铺可竖铺的区域优先横铺
    x:区域的序列号
    summary:记录铺法
    """
    global total
    global Ans
    global Final
    while x < m*n:
        l = h(x)
        if l == -1:
            if 2 in total:
                total.reverse()
                t = m*n - total.index(2) - 1
                total.reverse()
                for i in range(len(summary)):
                    if t in summary[i]:
                        v = i
                for i in summary[v:]:
                    for j in i:
                        Ans[j] = 0
                del summary[v:]
                total[t] = 1
                for i in range(t + 1, m*n):
                    total[i] = 0;
                markB(len(summary) + 1, t, summary)
                x = t + 1;
            else:
                print("Done")
                return
        if l == 0:
            x += 1
        if l == 1:
            markB(len(summary) + 1, x, summary)
            x += 1
        if l == 2:
            markA(len(summary) + 1, x, summary)
            x += 1
        if l == 3:
            markA(len(summary) + 1, x, summary)
            x += 1
    list1 = copy.deepcopy(summary)
    Final.append(list1)
    return Final


def tile(m, n, a, b, total, Final):
    """通过枚举实现全排，出现错误铺法或铺满即返回最后一块可横铺可竖铺的砖，改变其状态进行重排，如无这样的砖，函数结束。
    total:全局变量，记录区域是否可改变铺法
    Final:铺法集合
    """

    global Ans
    summary = []
    if a == b:
        assert(m%a == n%a == 0)
        print(1)
        c = int(m/a)
        d = int(n/a)
        for i in range(c*d):
            markA(i, (i%c)*a + a*m*int(i/c), summary)
        Final.append(summary)
        return Final
    
    g(0, summary)
    while 2 in total:
        total.reverse()
        e = m*n - total.index(2) - 1
        total.reverse()
        for i in range(len(summary)):
            if e in summary[i]:
                r = copy.deepcopy(i)
                break
        for i in summary[r:]:
            for j in i:
                Ans[j] = 0
        total[e] = 1
        for i in range(e+1, m*n):
            total[i] = 0
        del summary[r:]
        markB(r+1, e, summary)
        g(e+1, summary)
        

def main():
    """main module
    """
    assert(test()==True)
    t0 = time.process_time()
    tile(m, n, a, b, total, Final)
    for i in range(len(Final)):
        print(i+1, ":", Final[i])
    t1 = time.process_time()
    print(len(Final), " ", t1-t0, "s")
    
    h = int(turtle.numinput(None, "请输入一个序数", minval = 1, maxval = len(Final)+1))  
    picture(h-1)
    
    
if __name__ == '__main__':
    main()    

# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 00:55:55 2018

@author: 59459
"""

"""currency.py:该程序在用户输入原始货币及其数额、目标货币后，通过访问对应的网址反馈相应的兑换额.

__author__ = "Wengpeiyi"
__pkuid__  = "1800011749"
__email__  = "1800011749@pku.edu.cn"
"""

from urllib.request import urlopen
currency_from=input("请输入原始货币的英文代码：")
currency_to=input("请输入目标货币的英文代码：")
amount_from=input("数额：")
        
    
def exchange(a, b, c):
    """description: 
    a:原始货币的英文代码
    b:目标货币的英文代码
    c:数额
    return:兑换额
    """
    url = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=&to=&amt='
    a = a.upper()
    b = b.upper()
    url = url[0:54] + a + url[54:58] + b + url[58:63] + c
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    if  'true' in jstr:
        for i in ", : { } ": 
            jstr = jstr.replace(i, "")
        jstr = jstr.replace("true", "")
        jstr = jstr.replace("from", "")
        jstr = jstr.replace("to", "")
        jstr = jstr.replace("error", "")
        jstr = jstr.replace("success", "")
        jstr = jstr.replace('""', " ")
        jstr = jstr.split()
        return jstr[1]
    else:
        print("sorry, invalid input")
        
        
def test_exchange():
    assert(exchange('USD','CNY','1') == "6.8521ChineseYuan")
    assert(exchange('BTC','EUR','10') == "63628.783249544Euros")
    assert(exchange('GBP','JPY','2.5') == "357.96915910554JapaneseYen")
    

def testAll():
    """test all cases"""
    test_exchange()
    print("All tests passed!")
    
     
def main():
    """main module
    """
    
    testAll() 
    print("兑换额：", exchange(currency_from, currency_to, amount_from))
   
    
if __name__ == "__main__":
    main()
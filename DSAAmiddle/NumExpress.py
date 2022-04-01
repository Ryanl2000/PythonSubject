# 中文、英文数字表达
def ENExpress(num):  # 英文数字表达
    def Num1to19(num):  #1-19
        if num < 1:
            return ''
        names = ['One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ', 'Eight ', 'Nine ', 'Ten ',
                 'Eleven ', 'Twelve ', 'Thirteen ', 'Fourteen ', 'Fifteen ', 'Sixteen ', 'Seventeen ',
                 'Eighteen ', 'Nineteen ']
        return names[num-1]
    
    def Num1to99(num):  #1-99
        if num < 20:
            return Num1to19(num)
        names = ['Twenty ','Thirty ','Forty ','Fifty ','Sixty ','Seventy ','Eighty ','Ninety ']
        temp = num // 10
        return names[temp-2] + Num1to19(num % 10)
    
    def Num1to999(num):  #1-999
        if num < 100:
            return Num1to99(num)
        temp = num // 100
        return Num1to19(temp) + 'Hundred and ' + Num1to99(num % 100)
        
    if num == 0:
        return 'Zero'
    res = ''
    if num < 0:
        res += 'Negative, '
    num = abs(num)
    high = 1000000000
    index = 0
    names = ['Billion','Million','Thousand','']
    while num:
        cur = num // high
        num %= high
        if cur:
            res += Num1to999(cur)
            res += names[index] 
            res += ', ' if num != 0 else ''
        high //= 1000
        index += 1
    print(res)
    
def CNExpress(num):  #中文数字表达
    def Num1to9(num):
        if num < 1:
            return ''
        names = ['一','二','三','四','五','六','七','八','九']
        return names[num-1]
    
    def Num1to19(num):
        if num < 9:
            return Num1to9(num)
        return '十' + Num1to9(num % 10)
    
    def Num1to99(num):
        if num < 20:
            return Num1to19(num)
        temp = num // 10
        return Num1to9(temp) + '十' + Num1to9(num % 10)
    
    def Num1to999(num):
        if num < 100:
            return Num1to99(num)
        temp = num // 100
        if num % 100 > 9:
            return Num1to9(temp) + '百' + Num1to99(num % 100)
        else:
            return Num1to9(temp) + '百零' + Num1to99(num % 100)
    
    def Num1to9999(num):
        if num < 1000:
            return Num1to999(num)
        temp = num // 1000
        if num % 1000 > 99:
            return Num1to9(temp) + '千' + Num1to999(num % 1000)
        else:
            return Num1to9(temp) + '千零' + Num1to999(num % 1000)
    
    if num == 0:
        return '零'
    res = ''
    if num < 0:
        res += '负'
    num = abs(num)
    names = ['京','亿','万','']
    index = 0
    high = 1000000000000
    while num:
        cur = num // high
        num %= high
        if cur:
            res += Num1to9999(cur)
            res += names[index]
        high //= 10000
        index += 1
    print(res)


ENExpress(-1505648454001)
CNExpress(-1505640054010)

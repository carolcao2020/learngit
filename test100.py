#!/usr/bin/python
import json
data =[{'a':1,'b':2,'c':3,'d':4}]
json = json.dumps(data)
print(json)

def test_1():
    listNum = []
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if(i!=k) and (i!=j) and (j!=k):
                    listNum.append(i+j+k)
                    print(i,j,k)
    print("The total number is: " + str(len(listNum)))

def test_2():
    i = int(input("Please input the profit:"))
    profit = [1000000,600000,400000,200000,100000,0]
    rate = [0.01,0.015,0.03,0.05,0.075,0.1]
    bonus = 0
    for idx in range(0,6):
        if(i>profit[idx]):
            bonus = bonus + (i-profit[idx])*rate[idx]
            print((i-profit[idx])*rate[idx])
            i = profit[idx]
    print(bonus)

def test_3():
    for i in range(1,85):
        if 168%i == 0:
            j = 168/i
            if i> j and (i+j)%2==0 and (i-j)%2==0:
                m =(i+j)/2
                n =(i-j)/2
                x = n*n -100
                print(x)

def test_4():
    year = int(input("year:"))
    month = int(input("month:"))
    day = int(input("day:"))
    monthday = [0,31,59,90,120,151,181,212,243,273,304,334]
    if 0 <month <=12:
        sum = monthday[month-1]
    else:
        print("wrong month")
    sum = sum + day
    leap = 0
    if(year%400 == 0) or (year %4==0) and (year%100!=0):
        leap =1
    if (leap ==1) and (month>2):
        sum = sum + 1
    print(str(year)+str(month)+str(day)+ " is the %dth day."%sum)

def test_5():
    x = int(input("x:"))
    y = int(input("y:"))
    z = int(input("z:"))
    lista = []
    lista.append(x)
    lista.append(y)
    lista.append(z)
    lista.sort()
    print(lista)

def test_6(n):
    if n==1 or n==2:
        return 1
    else:
        return test_6(n-1)+test_6(n-2)

def test_6_1(n):
    listfib = [1,1]
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    for i in range(2,n):
        listfib.append(listfib[-1]+listfib[-2])
    return listfib

def test_7():
    a = [1,2,3]
    b = a[:]
    print(b)
def test_8():
    for i in range(1,10):
        for j in range(1,i+1):
            print(str(i)+"*"+str(j)+"=" + str(i*j),end = " ")
        print("\n")

def test_9():
    '''
    sleep 1s
    :return:
    '''
    import time
    myD ={1:"A",2:"B",3:"C"}
    for key,value in dict.items(myD):
        print(key,value)
        time.sleep(1)

def test_10():
    import time
    import datetime
    for i in range(5):
        # print(time.strftime('%Y-%m-%d %H:%M:%S'),time.localtime(time.time()))
        print(time.strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(1)
def  test_11(n):
    f1 = 1
    f2 = 1
    if n ==1 or n ==2:
        return 1
    else:
        for i in range(2,n):
            f1,f2 = f2,f1+f2
    return f2
def test_12():
    '''
    判断101-200之间有多少个素数，并输出所有素数。
    :return:
    '''
    import math
    count = 0
    leap =1
    for i in range(101,201):
        for j in range(2,math.ceil(math.sqrt(i+1))):
            if i%j ==0:
                leap = 0
                break
        if leap ==1:
            count = count + 1
            print("%d:%d"%(count,i))
        leap =1

def test_13():
    '''
    打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
    例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方
    利用for循环控制100-999个数，每个数分解出个位，十位，百位。
    :return:
    '''
    for i in range(100,1000):
        x = int(i/100)
        y = int(i/10%10)
        z = int(i %10)
        if i == x**3+y**3+z**3:
            print("%d: %d %d %d"%(i,x,y,z))
def test_14():
    '''
    将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
    :return:
    '''
    n = int(input("input a number:"))
    number = n
    l = []
    while n > 1:
        for i in range(2,n+1):
            if n%i==0:
                n = n//i
                l.append(str(i))
                break
    print('%d='%number+'*'.join(l))

def test_15():
    '''
    利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
    :return:
    '''
    score = int(input("input the score:"))
    if score >=90:
        grade = 'A'
    elif score >=60:
        grade = 'B'
    else:
        grade = 'C'
    print('%d belong to grade %s'%(score,grade))

def test_16():
    '''
    输出指定格式的日期。
    :return:
    '''
    import datetime
    print(datetime.date.today())
    print(datetime.date.today().strftime('%d/%m/%Y'))
    # 2018 - 12 - 05
    # 05 / 12 / 2018

    birthday = datetime.date(1988,8,7)
    print(birthday)
    print(birthday.strftime('%m/%d/%Y'))
    # 1988 - 08 - 07
    # 08 / 07 / 1988

    nextday = birthday + datetime.timedelta(days=1)
    print(nextday)
    previousday = birthday + datetime.timedelta(days=-1)
    print(previousday)
    # 1988 - 08 - 08
    # 1988 - 08 - 06

    firstbirthday = birthday.replace(year=1989)
    print(firstbirthday)
    secondbirthday = birthday.replace(year=birthday.year+2)
    print(secondbirthday)
    # 1989 - 08 - 07
    # 1990 - 08 - 07

def test_17():
    '''
    输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
    :return:
    '''
    str = input("please input the string")
    letters = 0
    space =0
    number =0
    others =0
    for i in range(len(str)):
        if str[i].isalpha():
            letters+=1
        elif str[i].isdigit():
            number+=1
        elif str[i] == " ":
            space+=1
        else:
            others+=1
    print("Characters is: %d"%letters)
    print("space is: %d" %space)
    print("Digital number is: %d"%number)
    print("Other character is: %d"%others)
def test_18():
    '''
    求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
    :return:
    '''
    number = input("please input number")
    time = int(input("please input time"))
    sum =0
    for i in range(1,time+1):
        sum = sum + int(number*i)
    print("The total number is %d" %sum)
def test_19():
    '''
    一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
    :return:
    '''
    for i in range(2,1001):
        sum = 0
        lista = []
        for j in range(1,i):
            if i% j == 0:
                sum+=j
                lista.append(j)
        if sum == i:
            print(i)
            print(lista)

def test_20():
    '''
    一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
    :return:
    '''
    hei = 100
    time = 10
    height = [] #height every time
    for i in range(2,time+1):
        hei = hei/2
        height.append(hei)

    print("The height is %s" %(min(height)/2))
    print("The total distance is %s"%(sum(height)*2+100))

def test_21():
    '''
    猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
    以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
    :return:
    '''
    x2 = 1
    for i in range(9,0,-1):
        x1 = (x2+1)*2
        x2 = x1
    print(x1)

def test_22():
    '''
    两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
    有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
    :return:
    '''
    lista = ['a','b','c']
    listx = []
    for i in range(3):
        if lista[i]!='a' and lista[i]!='c':
            listx.insert(i,'x')
        elif lista[i]!='c':
            listx.insert(i,'z')
        else:
            listx.insert(i,'y')
    print("a--%s,b--%s,c--%s"%(listx[0],listx[1],listx[2]))

def test_23():
    '''
   *
  ***
 *****
*******
 *****
  ***
   *
    :return:
    '''
    n = int(input("please input lines number:"))
    middle = n//2 + 1
    for i in range(middle):
        space = abs(middle - i)
        character = 2*i + 1
        print(" " *space + "*" * character + " " * space)
    for i in range(middle,0,-1):
        space = abs(middle - i)
        character = 2 * i + 1
        print(" " * space + "*" * character + " " * space)
def test_24():
    '''
    有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
    :return:
    '''
    numerator = 2
    denominator = 1
    fractions = numerator/denominator
    num = int(input("please input number"))
    listnum = []
    listnum.append(fractions)
    for i in range(2,num+1):
        temp = numerator
        numerator = denominator + numerator
        denominator = temp
        listnum.append(numerator/denominator)
        # numerator_new = denominator + numerator
        # denominator_new = numerator
        # fractions = numerator_new/denominator_new
        # listnum.append(fractions)
        # numerator = numerator_new
        # denominator = denominator_new
    print("The total sum value is: %d" % sum(listnum))

def test_25_1(x):
    factorial =1
    for i in range (1,x+1):
        factorial = factorial * i
    return factorial

def test_25():
    '''
    求1+2!+3!+...+20!的和。
    :return:
    '''
    sum = 0

    for i in range(1,21):
        factorial = 1
        for j in range(1,i+1):
            factorial = factorial*j
        sum = sum + factorial
    print("1+2!+3!+...+20!=%d" % sum)
    lrange = list(range(1,21,1))
    slist = list(map(test_25_1,lrange))
    s=0
    for i in range(len(slist)):
        s = s+ slist[i]
    print("1+2!+3!+...+20!=%d" % s)

def test_26(n):
    '''
    利用递归方法求5!
    :param n:
    :return:
    '''
    if n==1:
        return 1
    else:
        return n*test_26(n-1)

def test_27(s):
    '''
    利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
    :param s: input string
    :return:
    '''
    l = len(s)
    if l == 0:
        return
    print(s[l-1])
    test_27(s[0:-1])

def test_28(n):
    '''
    有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。
    问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
    :return:
    '''
    if n == 1:
        age = 10
    else:
        age = test_28(n-1) + 2
    return age

def test_29():
    '''
    给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
    :return:
    '''
    number = input("please input a number less than 5 digits:")
    num = int(number)
    if len(number) > 5:
        number = input("please input a number less than 5 digits:")
    else:
        print("math the condition, the number digits is less than 5")
        n1 = num // 10000
        n2 = num % 10000//1000
        n3 = num % 1000//100
        n4 = num % 100 // 10
        n5 = num % 10
        if n1 != 0:
            print("%d is 5 digits %d %d %d %d %d" %(num,n5,n4,n3,n2,n1))
        elif n2 !=0:
            print("%d is 4 digits %d %d %d %d" % (num, n5,n4, n3, n2))
        elif n3!=0:
            print("%d is 3 digits %d %d %d" % (num, n5, n4, n3))
        elif n4!=0:
            print("%d is 2 digits %d %d" % (num, n5, n4))
        else:
            print("%d is 1 digits %d" % (num, n5))

def test_30():
    '''
    一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
    :return:
    '''
    n = input("please input a number:")
    l = len(n)
    if int(n)%2 !=1 or int(n) == 1:
        print("It is a oushu or 1")
    else:
        flag = True
        for i in range(l//2):
            if n[i] != n[-i-1]:
                flag = False
                print("it is a jishu but do not match")
                break
        if flag == True:
            print("it is match the condition")
def test_31():
    '''
    请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
    :return:
    '''
    import re
    weekday = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    dictWeek = {'M':'Monday','T':{'u':'Tuesday','h':'Thursday'},'W':'Wednesday','F':'Friday','S':{'a':'Saturday','u':'Sunday'}}
    letter = input("Please input the first letter")
    letterU=letter.upper()
    listkey = list(dictWeek.keys())
    if letterU not in listkey:
        print("Do not match any day!")
    else:
        if letterU == "T" or letterU == "S":
            ele = dictWeek.get(letterU)
            second = input("Plese input the second letter")
            elelist = list(ele.keys())
            if second in elelist:
                print(ele.get(second))
            else:
                print("Do not match any day")

        else:
            print(dictWeek.get(letterU))

def test_32():
    '''
    按相反的顺序输出列表的值。
    :return:
    '''
    lista = ['a','b','c','d']
    print(lista[::])
    lista.reverse()
    print(lista)
    for i in lista[-1::-1]:
        print(i,end=' ')

def test_33():
    '''
    按逗号分隔列表
    :return:
    '''
    lista = ['a', 'b', 'c', 'd']
    s1 = ',' .join(i for i in lista)
    s2 = '*'.join(lista)
    print(s1)
    print(s2)
def test_34():
    '''
    练习函数调用。
    :return:
    '''
    for i in range(4):
        print("%d call the method"%i)
        test_33()

def test_35():
    '''
    文本颜色设置。
    :return:
    '''
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    print(bcolors.WARNING + "Warning font color is " + bcolors.ENDC)

def test_36():
    '''
    求100之内的素数。
    :return:
    '''
    for i in range(1,101):
        if i >1:
            for j in (2,i):
                if i%j == 0:
                    break
                else:
                    print(str(i),end=' ')
def test_37():
    '''
    对10个数进行排序。
    :return:
    '''
    lista = [1,5,2,9,4,7,22,45,11,44]
    import random
    listb = []
    for i in range(10):
        listb.append(random.randint(1,100))
    print(listb)
    # listb.sort()
    # print(listb)
    print(sorted(listb,reverse=True))
    print(sorted(listb))
    print(lista)
    for i in range(len(lista)):
        min = i
        for j in range(i+1,len(lista)):
            if lista[min] > lista[j]:
                min = j
        lista[i],lista[min] = lista[min],lista[i]
        print(str(i)+ " time sort order ")
        print(lista)
    print(lista)

def test_38():
    '''
    求一个3*3矩阵主对角线元素之和
    :return:
    '''
    import random
    total = []
    for i in range(3):
        line = []
        for j in range(3):
            num = random.randint(1,10)
            line.append(num)
            print(str(num),end=" ")
        print()
        total.append(line)
    sum =0
    for i in range(len(total)):
        linelist = total[i]
        for j in range(len(total[i])):
            if i == j:
                sum = sum + linelist[j]
    print("The total sum value is %d" %sum)


if __name__ =='__main__':
    # test_1()
    # test_2()
    # test_3()
    # test_4()
    # test_5()
    # print(test_6(10))
    # print(test_6_1(10))
    # test_7()
    # test_8()
    # test_9()
    # test_10()
    # print(test_11(10))
    #test_12()
    # test_13()
    #test_14()
    #test_15()
    # test_16()
    # test_17()
    # test_18()
    # test_19()
    # test_20()
    # test_21()
    # test_22()
    # test_23()
    # test_24()
    # test_25()
    # print(test_26(5))
    # test_27("abcdef")
    # print(test_28(5))
    # test_29()
    # test_30()
    # test_31()
    # test_32()
    # test_33()
    # test_34()
    # test_35()
    # test_36()
    # test_37()
    test_38()

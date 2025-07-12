a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
c=True
d=False
#and:都为True才是True，True加整形，浮点则输出数值，有False直接False
print(c and d)
print(a and d)
print(c and a)
#or:有True就True，True加整形，浮点则输出数值，有False直接False
print(c or d)
print(a and d)
print(c and a)
#not:取反,有整型，浮点均视为True，not之后就是False
print(not c)
print(not d)
str1="aaa"
str2='bbb'
str3="""666"""
print(type(a))
print(type(c))
print(type(str1))
print(str1)
print(str2)
print(str3)
str4=str1+str2#连接
print(str4)
print(str4*3)#重复三次
#获取字符长度(只能字符串），空格也算
print(len(str1))
str5="   54188  "
print(str5)
print(len(str5))
#除空白
newstr5=str5.strip()
print(str5.strip())
print(newstr5)
#改大小写
str6="AbCd"
newstr6=str6.upper()#改大写
newnewstr6=str6.lower()#改小写
print(str6)
print(newstr6)
print(newnewstr6)




# 1.strip()  用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列、剥离其值的所有组合。


# s = '   hello   '.strip()
# print(s)      # hello

# s = '###hello###'.strip()
# print(s)       # ###hello###

# s = '###hello###'.strip('#')
# print(s)       # hello

# s = '#hello##'.strip('#')
# print(s)    # hello

# s = '#hello'.strip('#')
# print(s)       # hello

# s = 'hello##'.strip('#')
# print(s)       # hello

# s = 'www.baidu.com'.strip('wcom')
# print(s)       # .baidu.


# 2.lstrip()  移除字符串左侧指定的字符（默认为空格或换行符）或字符序列, 同样的，可以移除左侧所有包含在字符集中的字符串。


# s = ' hello'.strip()
# print(s)           # hello

# s = '#hello'.strip('#')
# print(s)        # hello

# s = 'Arthur: three!'.lstrip('Arthur: ')
# print(s)           # ee

# 3.rstrip() 移除字符串右侧指定的字符（默认为空格或换行符）或字符序列。

# s = 'Arthur: three!'.rstrip('thre!')
# print(s)    # Arthur: 

# 4.removeprefix()  Python3.9中移除前缀的函数, 与strip()相比，并不会把字符集中的字符串进行逐个匹配。

# s = 'Arthur: three!'.removeprefix('Arthur: ')
# print(s)       # three!


# 5.removesuffix()  Python3.9中移除后缀的函数。

# s = 'HelloPython'.removesuffix('Python')
# print(s)    # Hello


# 6.replace() 把字符串中的内容替换成指定的内容。


# s = 'string method in python'.replace(' ', '_')
# print(s)       # string_method_in_python

# s = 'string method in python'.replace(' ', '')
# print(s)       # stringmethodinpython



# 7.re.sub() 利用正则表达式进行替换。


# import re
# s = 'string methods in python'
# s2 = re.sub("\s+", '_', s)
# print(s2)      # string_methods_in_python


# 8.split() 对字符串进行分隔处理，最终得到的结果是一个列表。


# s = 'string methods in python'.split()  # 默认为空格
# print(s)           # ['string', 'methods', 'in', 'python']

# s = 'string methods in python'.split(' ', maxsplit=1)   # 指定分割次数为1
# print(s)          # s = ['string', 'methods in python']


# 9.rsplit()   从右侧开始对字符串进行分割。


# s = 'string methods in python'.rsplit(' ', maxsplit=1)
# print(s)           # ['string methods in', 'python']


# 10.join()     string.join(seq), 以string作为分隔符，将seq中所有的元素（的字符串表示）合并为一个新的字符串。


# list_of_strings = ['string', 'methods', 'in', 'python']
# s = '_'.join(list_of_strings)
# print(s)           # string_methods_in_python

# tu_of_strings = ('string', 'methods', 'in', 'python')
# s = '_'.join(tu_of_strings)
# print(s)           # string_methods_in_python

# set_of_string = {'string', 'methods', 'in', 'python'}
# s = '_'.join( set_of_string)
# print(s)       # in_python_string_methods 由于集合是无序的

# dict_of_string = {'a':1, 'b':2, 'c':3}
# s = '_'.join(dict_of_string)
# print(s)           # a_b_c 按照键进行匹配


# 11.upper()    将字符串中的字母，全部转换为大写。


# s = 'simple is better than complex'.upper()
# print(s)           # SIMPLE IS BETTER THAN COMPLEX


# 12.lower()    将字符串中的字母，全部转为小写。


# s = 'SIMPLE IS BETTER THAN COMPLEX'.lower()
# print(s)           # simple is better than complex


# 13.capitalize()  将字符串中的首个字母转为大写, 其他字母变小写。


# s = 'simple is better than complex'.capitalize()
# print(s)           # Simple is better than complex

# s = 'Simple IS beTTer ThAN cOmPLE'
# print(s.capitalize())         # Simple is better than comple



# 14.title()    将每个单词的首字母大写。


# s = "Welcome to mY 2nd World"
# print(s.title())        # Welcome To My 2Nd World


# 15.islower()     判断字符串中的所有字母是否都为小写，是则返回True，否则返回False。


# print('SIMPLE IS BETTER THAN COMPLEX'.islower())    # False
# print('simple is better than complex'.islower())    # True


# 16.isupper()    # 判断字符串中的所有字母是否都为大写，是则返回True，否则返回False。


# print('SIMPLE IS BETTER THAN COMPLEX'.isupper()) # True
# print('SIMPLE IS BETTER THAN complex'.isupper()) # False


# 17.isalpha()    如果字符串至少有一个字符并且所有字符都是字母，则返回 True，否则返回 False。


# s = 'python'
# print(s.isalpha())      # true

# s = '123'
# print(s.isalpha())      # false

# s = 'python123'
# print(s.isalpha())      # false

# s = 'python-123'
# print(s.isalpha())      # false


# 18.isnumeric()    如果字符串中只包含数字字符，则返回 True，否则返回 False。


# s = 'python'  
# print(s.isnumeric())       # False

# s = '123'
# print(s.isnumeric())       # True

# s = 'python123'
# print(s.isnumeric())       # False

# s = 'python-123'  
# print(s.isnumeric())       # False


# 19.isalnum()    如果字符串中至少有一个字符并且所有字符都是字母或数字，则返回True，否则返回 False。


# s = 'python123'
# print(s.isalnum())      # True

# s = 'phthon-123'
# print(s.isalnum())      # False


# 20.count()  返回指定内容在字符串中出现的次数


# n = 'hello world'.count('o')
# print(n)       # 2

# n = 'hell world'.count('he')
# print(n)       # 1


# 21.find() 检测指定内容是否包含在字符串中，如果是返回开始的索引值，否则返回-1。


# s = 'Machine Learning'
# idx = s.find('a')
# print(idx)       # 1
# print(s[idx:])      # achine Learning

# s = 'Machine Learing'
# idx = s.find('ach')
# print(idx)      # 1
# print(s[idx:])      # achine Learing

# s = 'Machine Learing'
# idx = s.find('a', 2)
# print(idx)      # 10
# print(s[idx:])      # aring


# 22.rfind()   类似于find()函数，返回字符串最后一次出现的位置，如果没有匹配项则返回 -1。


# s = 'Machine Learning'
# idx = s.rfind('a')
# print(idx)      # 10
# print(s[idx:])      # arning


# 23.startswith()   检查字符串是否是以指定内容开头，是则返回 True，否则返回 False。


# print('Patrick'.startswith('P'))    # True


# 24.endswith()   检查字符串是否是以指定内容结束，是则返回 True，否则返回 False。


# print('Patrick'.endswith('ck'))     # True


# 25.center()     返回一个原字符串居中，并使用空格填充至长度width的新字符串。


# s = 'Python is awesome!'
# s1 = s.center(31, '_')
# print(len(s))     # 18
# print(s1)     # _______Python is awesome!______


# 26.ljust()      返回一个原字符串左对齐，并使用空格填充至长度width的新字符串。



# s = 'Python is awesome!'
# s1 = s.ljust(30, '_')
# print(s1)       # Python is awesome!____________


# 27.rjust()  返回一个原字符串右对齐，并使用空格填充至长度width的新字符串。


# s = 'Python is awesome!'
# s1 = s.rjust(30, '_')
# print(s1)       # ____________Python is awesome!


# 28.partition()    从str出现的第一个位置起,把字符串string分成一个3 元素的元组(string_pre_str,str,string_post_str)，如果string中不包含str则 string_pre_str==string。


# s = 'Python is awesome!'
# parts = s.partition('is')
# print(parts)        # ('Python ', 'is', ' awesome!')

# s = 'Python is awesome!'
# parts = s.partition('was')
# print(parts)        # ('Python is awesome!', '', '')


# 29.f-strings  f-string是格式化字符串的新语法。


# num = 1
# language = 'Python'
# s = f'{language} is the number {num} in programming!'
# print(s)        # Python is the number 1 in programming!


# 30.swapcase()     翻转字符串中的字母大小写。


# s = 'HellO wORld'
# print(s.swapcase())     # hELLo WorLD


# 31.zfill()    string.zfill(width), 返回长度为width的字符串，原字符串string右对齐，前面填充0。


# s = '42'.zfill(5)
# print(s)        # 00042

# s = '-42'.zfill(5)
# print(s)        # -0042

# s = '+42'.zfill(5)
# print(s)        # +0042
# 02-Python的核心数据类型

------

## 内置对象

| 对象类型     | 例子                         |
| -------- | -------------------------- |
| 数字       | 1234                       |
| 字符串      | 'spam'，"guido's"           |
| 列表       | [1, [2, 'three'], 4]       |
| 字典       | {1, ‘s’, 4, 'U'}           |
| 元组       | (1, 'spam', 4,'U')         |
| 文件       | myfile = open('eggs', 'r') |
| 集合       | set('abc'),{'a', 'b', 'c'} |
| 其他类型     | 类型、None、布尔型                |
| 编程单元类型   | 函数、模块、类                    |
| 与实现相关的类型 | 编译的代码堆栈跟踪                  |

表格并不完整，因为在Python程序中处理的每样同喜都是一种对象。例如，在Python中进行文本模式匹配时，创建了模式对象，在进行网络脚本编程时，使用了套接字对象。其他类型的对象往往是通过导入或者使用模块来简历的，而且它们各自有各自的行为。

在核心类型中，数字，字符串和元组是不可变的，列表和字典是可变的。

------

## 数字

Python的核心对象集合包括常规的类型：

1. 整数
2. 浮点数
3. 有虚部的复数
4. 固定精度的十进制数
5. 带分子和分母的有理分数
6. 集合等

Python中的数字支持一般的数学运算：

1. 加法（+）
2. 乘法（*）
3. 乘方（**）

```python
>>> 123 + 222  #整数相加
345
>>> 1.5 * 4    #浮点数相乘
6.0
>>> 2 ** 100   #2的100次方
1267650600228229401496703205376
```

注意第三个结果:Python 3.0的整数类型会在需要的时候自动提供额外的精度

```python
>>> len(str(2 ** 1000000))  #计算位数
301030
```

Python常用的数学模块，模块只不过是我们导入以供使用的一些额外工具包。

```python
>>> import math
>>> math.pi
3.141592653589793
>>> math.sqrt(85)
9.219544457292887
>>>
```

Math模块包含更高级的数学工具，如函数，random模块可以作为随机数字的生成器和随机选择器：

```python
>>> import random
>>> random.random()
0.026534982723416367
>>> random.choice([1, 2, 3, 4])
1
```

------

## 字符串

字符串是Python中序列的一个**序列**，序列中的元素包含了一个从左到右顺序——序列中的元素根据他们的相对位置进行存储和读取。吃饱饭严格意义上来说，字符串是单个字符的字符串序列，其他类型的序列还包括：**元组**和**列表**。

### 字符串索引

作为序列：字符串支持假设其中各个元素包含位置顺序的操作，索引是按照从最前面的偏移量进行编码，从0开始。

```python
>>> S = 'EricChen'
>>> len(S)
8
>>> S[0]
'E'
>>> S[1]
'r'
```

在Python中，我们能够反向索引，从最后一个开始（正向索引时从左边开始计算，反向索引时从右面开始计算。

```python
>>> S[-1] # S中最后一个字符
'n'
>>> S[len(S)-1] #同样结果，但更麻烦且容易出错
'n'
```

### 分片

分片操作就是一种一步就能够提取整个分片（slice）的方法，左边界默认为0，而且右边界默认为分片序列的长度。

```python
>>> S
'EricChen'
>>> S[1:3]  #取第1-3位的字符
'ri'
>>> S[1:]  #取第1开始到结尾的字符
'ricChen'
>>> S[0:3] #取第0-3位的字符
'Eri'
>>> S[:3]  #取第0-3位的字符
'Eri'
>>> S[:-1] #取第0-结尾前一位的字符
'EricChe'  
>>> S[:]  #获取整个字符串
'EricChen'
```

作为序列，字符串也支持加号合并操作，或者重复操作（通过再重复一次创建一个新的字符串）：

```python
>>> S
'EricChen'
>>> S + 'XYZ'
'EricChenXYZ'
>>> S
'EricChen'
>>> S*5
'EricChenEricChenEricChenEricChenEricChen'
```

### 不可变性

Python字符串具有不可变性-即创建后就不能够改变。

### 类型特定的方法

字符串独有一些操作作为方法存在（对象的函数，将会通过一个调用表达式触发）。

以下是一些例子：

1. find()方法：一个基本的子字符串朝赵的操作，它将返回一个传入子字符串的偏移量，或者没有找到的情况下返回-1.

2. replace()：字符串的replace方法将会对全局进行搜索和替换。

3. split()：通过指定分隔符将字符串拆分为子字符串

4. upper()：转化为大写

5. isalpha()：是否是字母

6. rstrip()：从右方删除空格

   ​

```python
>>> line = 'aaa,bbb,cccc,dd'
>>> line.split(',')
['aaa', 'bbb', 'cccc', 'dd']
>>> S.upper()
'ERICCHEN'
>>> S.isalpha()
True
>>> line = 'aaa,bbb,cccc,dd\n'
>>> line
'aaa,bbb,cccc,dd\n'
>>> line = line.rstrip()
>>> line
'aaa,bbb,cccc,dd'
```

字符串还支持一个叫做格式化的高级替代操作：

```python
>>> '%s,egs,and %s' % ('spam','SPAM!')
'spam,egs,and SPAM!'
>>> '{0},egg,and {1}'.format('spam','SPAM!')
'spam,egg,and SPAM!'
```

### 寻求帮助

更多方法可以使用以下方法寻求帮助：

```python
>>> dir(S)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '_
_eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs
__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__'
, '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__'
, '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'e
ncode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isal
num', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstr
ip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartitio
n', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase'
, 'title', 'translate', 'upper', 'zfill']
```

要查询某个方法是做什么的

```python
>>> help(S.replace)
Help on built-in function replace:

replace(...) method of builtins.str instance
    S.replace(old, new[, count]) -> str

    Return a copy of S with all occurrences of substring
    old replaced by new.  If the optional argument count is
    given, only the first count occurrences are replaced.
```

### 模式匹配

文本的匹配模式相对高级的工具，我们可以导入一个名为re的模块，这个模块包含了类似搜索，分隔，替换等调用，这个模块包含了类似搜索，分隔和替换等调用，但是因为使用模式去定义子字符串，可以更通用些：

```
>>> import re
>>> match = re.match('Hello[ \t]*(.*)world','Hello   Python world')
>>> match.group(1)
'Python '
```

这个例子目的是搜索子字符串，这个子字符串一'Hello'开始，后面跟着另个或者几个制表符或者宫格，接招有任意字符并将其保存至匹配的gourp中，最后以‘world.’结尾。如果找到这样的子字符串，与模式中括号包含的部分匹配的子字符串的对应部分为组。

一面的模式去除了三个被斜线所分割的组

```
>>> match = re.match('/(.*)/(.*)/<.*>', '/usr/home/lumberjack')
>>> match.groups()
('usr','home','lumberjack')
```

匹配模式本身是一个相当高级的文本处理工具，但是Python中还支持更高级的语言处理工具，包括自然语言处理等。
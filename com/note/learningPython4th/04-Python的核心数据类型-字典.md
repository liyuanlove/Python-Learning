# 04-Python的核心数据类型-字典

------

## 字典

Python中的字典不是序列，而是一种**映射**。映射是一个其他对象的集合，但是他们是通过键而不是相对位置来存储的。映射并没有任何可靠的从左到右的顺序，也就是说，它并不是有序的。操作

定义一个字典：

```python
>>> D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'} #定义一个字典，key:value
>>> D['food'] 			  # 根据key获取vlaue
'Spam'
>>> D['quantity'] += 1    #根据key操作vlaue
>>> D
{'food': 'Spam', 'quantity': 5, 'color': 'pink'}
```

与列表中净值边界外赋值不同，对一个新的字典的键赋值会创建该键：

```python
>>> D = {}
>>> D['name'] = 'Bob'
>>> D['job'] = 'dev'
>>> D['age'] = 40
>>> D
{'name': 'Bob', 'job': 'dev', 'age': 40}
>>> D['name']
'Bob'
```

通过键索引一个字典往往是Python中编写搜索的最快方法。

------



## 嵌套

字典中可以嵌套字典，也可以嵌套列表：



```python
>>> rec = {'name': {'first': 'Eric', 'last': 'Chen'}, #嵌套字典
           'job': ['dev', 'mgr'],   #嵌套列表
           'age' : 20}
>>> rec
{'name': {'first': 'Eric', 'last': 'Chen'}, 'job': ['dev', 'mgr'], 'age': 20}

>>> rec['name']
{'first': 'Eric', 'last': 'Chen'}  #取出字典name

>>> rec['name']['last']      #取出字典name中的last
'Chen'

>>> rec['job']     #取出列表job
['dev', 'mgr']

>>> rec['job'][0]   #可以随意操作列表job
'dev'

>>> rec['job'][-1]
'mgr'

>>> rec['job'].append('CTO')

>>> rec['job']
['dev', 'mgr', 'CTO']
```

注意：最后一个操作：因为job列表是字典所包含的一部分独立的内存，所以它**可以自由地增加或者减少**。

Python核心数据类型非常灵活，嵌套允许直接轻松地简历复杂的信息结构。运行表达式创建了整个嵌套对象结构，不用实现安排并且声明结构和数组，这是Python脚本语言的主要优点之一。

------

## 垃圾收集

在底层语言中，当我们不再需要该对象时，必须小心地去释放掉所有对象空间。在Python中，当最后一次引用对象后（例如，将这个变量用其他值进行赋值），这个对象所占用的内存空间将会被自动清理掉：

从技术上来说，Python具有一种垃圾收集的特性，在程序运行时，可以清理不再使用的内存，一旦一个对象最后一次引用被移除，空间将会立刻回收，详细细节后面会介绍。

------

## 键的排序：for循环

作为映射，字典仅仅支持通过键获取元素，当我们打印一个字典的时候，它是乱序的：

```python
>>> D = {'a': 1, 'b': 2, 'c': 3}
>>> D
{'a': 1, 'c': 3, 'b': 2}
```

当我们强调字典的顺序时：

```python
>>> Ks = list(D.keys())
>>> Ks
['a', 'b', 'c']
>>> for key in Ks:
...     print(key, '->', D[key])
a -> 1
b -> 2
c -> 3
```

我们可以使用if语句对字典中的值进行判断是否存在：

```python
{'a': 1, 'b': 2, 'c': 3}
>>> 'f' in D
False
>>> if not 'f' in D:
...     print('missing')
missing
```

我们可以使用get方法（带有一个默认值的条件索引）来获取值：

```python
>>> vlaue = D.get('x', 0)  #如果没有获取到，默认返回0
>>> vlaue
0
>>> value = D['x'] if 'x' in D else 0    
>>> value
0
```


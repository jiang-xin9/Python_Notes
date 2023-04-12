# 前言
有问题可以加V：qing_an_an，本章无习题，只有例题操作！
如果看不懂如下例子，那么请移步到：
![1657106540296.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/25452484/1657106560610-b661c077-57c2-4333-a04b-be57b5a51b06.jpeg#clientId=u4d0176ef-f829-4&from=paste&height=152&id=dUjOd&name=1657106540296.jpg&originHeight=152&originWidth=151&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20432&status=done&style=none&taskId=u42fce756-3cdf-4ee3-b17d-8df6e784146&title=&width=151)
# 官网地址
[JSONPath - XPath for JSON](https://goessner.net/articles/JsonPath/)
# Jsonpath
对于jsonpath的定义：JSONPath 表达式始终引用 JSON 结构，就像 XPath 表达式与 XML 文档结合使用一样。由于 JSON 结构通常是匿名的，并且不一定具有“根成员对象”，因此 JSONPath 假定$分配给外层对象的抽象名称。
JSONPath表达式可以使用点- 表示法 $.store.book[0].title 或括号- 表示法 $['store']['book'][0]['title']
# 实例
```python
# -->>>清安<<<---
import jsonpath

a = {"home": {
    "information": [
        {"name": "清安",
         "sex": "男",
         "age": 18,
         "Telephone": 12345678900
         },
        {"name": "QA",
         "sex": "男",
         "age": 19,
         "Telephone": 98765432100
         },
        {"name": "AQA",
         "sex": "女",
         "age": 20,
         "Telephone": 1597532486200
         },
        {"name": "QAQ",
         "sex": "女",
         "age": 19,
         "Telephone": 96385274100
         }
    ],
    "hobby": {
        "Bicycle": "red",
        "car": "yellow"
    }
}
}
```
## 获取所有name键对应的值
```python
# -->>>清安<<<---
import jsonpath

i = jsonpath.jsonpath(a,"$..name")
print(i)

# ['清安', 'QA', 'AQA', 'QAQ']
```
## 获取所有Telephone对应的值
```python
# -->>>清安<<<---
import jsonpath


o = jsonpath.jsonpath(a,'$.home..Telephone')

print(o)

```
这里运用第一种写法也是可以的。直接$..Telephone。
## 获取home下的information下的全部性别
```python
# -->>>清安<<<---
import jsonpath

p = jsonpath.jsonpath(a,'$.home.information[*].sex')
print(p)

```
其实方法都是类似的，以上三种例子大可以用同一种方式来写，灵活多变，看你自己所取得数据的结构是怎么样的了。
# 官网实例
```python
{ "store": {
    "book": [ 
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}
```
| **XPath** | **JSON路径** | **结果** |
| --- | --- | --- |
| /home/book/author | $.store.book[*].author |  店内所有书籍的作者   |
| //author | $..author |  所有作者   |
| /store/* | $.store.* |  所有东西都在商店里，包括一些书和一辆红色自行车。   |
| /store//price | $.store..price |  商店里所有东西的价格。   |
| //information[3] | $..information[2] |  第三个人信息   |
| //information[last()] | $..information[(@.length-1)]
$..information[-1:] |  按顺序排列的最后一个人信息。   |
| //information[position()<3] | $..information[0,1]
$..information[:2] |  前两个人信息   |
| //information[sex] | $..information[?(@.sex)] |  过滤所有带有 sex的信息   |
| //information[age<19] | $..information[?(@.age<19)] |  过滤并所有年龄低于 19岁人的信息   |
| //* | $..* |  XML 文档中的所有元素。JSON结构的所有成员。   |


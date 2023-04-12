import random
import re


class Match:
    def match(self):
        content='ewq3sfdad234ddaf'
        result1=re.match('(ewq)',content)
        result2=re.search('\d',content)
        result3=re.findall('[0-9]',content)
        result4=re.finditer('[0-9]',content)
        result5=re.split('[0-9]',content)
        result6=re.sub('(.+?1e)','ewq',content)
        print(result1)#使用带有可选标记的正则表达式的模式来匹配字符串，匹配成功返回匹配对象，否则返回None
        print(result1.group())#返回整个匹配对象
        print(result1.group(1))#查看正则式中第一个括号里面的内容
        print(result1.groups)#将正则式中所有括号里面的内容组成一个tuple，提取字符串要用切片的方法result.groups()[0]
        #group里面的参数是从1开始的，不是从0开始的
        print(result2)  # 使用可选标记搜索字符串中第一次出现的正则表达式模式，如果匹配成功，则返回匹配对象，否则返回None
        print(result3) #查找字符串中所有（非重复）出现的正则表达式模式，并返回一个匹配列表
        print(result4) #返回一个迭代器，对于每一次匹配，迭代器都能返回一个匹配对象
        print(next(result4))
        print(next(result4).group())
        print(result5)#根据正则表达式的模式分隔符，split函数将字符串分割为列表，返回匹配列表，分割最多操作max次
        print(result6)#替换匹配的子字符串，返回替换之后的字符串

    def random(self):
        print(random.random())#生成随机浮点数（0-1）
        print(round(random.random(),6))#四舍五入
        print(random.uniform(0,4)) #生成指定范围的随机浮点数
        print(random.randint(1,8))#生成指定范围随机整数
        print(random.randrange(1,10,2)) #从1-10中步长为2中生成随机数，即奇数
        result=[i for i in range(1,9) if i%2==1]
        print(result)
        print(random.choice("match.py"))
        print(random.choice([1,4,6,8,[1,2,4]]))
        print(random.choice((1,2,3,4)))
        print(random.choice([1,2,4,(3,4,5)]))
        #random.choice(sequence),sequence表示有序类型，可为列表，元组，字符串
        result1=[1,2,4,5,67,5]
        random.shuffle(result1)#将一个列表中的数据打乱重新组合
        print(result1)
        result2=(1,34,45,5,3,5,3,[3,5,6],'dd',[4,6,7],[7,8,65])
        result3=random.sample(result2,4)#从列表中随机取k个数，源列表不变
        print(result2)
        print(result3)


if __name__ == '__main__':
    Match().match()
    Match().random()
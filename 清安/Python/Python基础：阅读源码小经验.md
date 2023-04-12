# 经验一，返回值问题
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25452484/1658375416985-dd3d741f-89f1-42f1-91a9-3413c75f3c66.png#clientId=u33afda7d-9fe2-4&from=paste&height=511&id=u17273efa&name=image.png&originHeight=511&originWidth=562&originalType=binary&ratio=1&rotation=0&showTitle=false&size=58399&status=done&style=none&taskId=u7425be76-93ed-438d-b7e4-51b22634b79&title=&width=562)
上述中注释中都有返回值，有返回值意味着什么？看例子，以列表为例！
```python
list_ = ['我','是','清','安']
print(list_.index('安'))
"""
有返回值的可以直接print使用。结果为：
3
"""
```
那么无返回值的呢？
```python
list_ = ['我','是','清','安']
print(list_.insert(1,'安'))

"""
无返回值不能够直接print。print的结果是：
None
"""
```
那么最直接的问题看法：
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25452484/1658375728113-555eb887-27f4-471d-a980-29f222ed4083.png#clientId=u33afda7d-9fe2-4&from=paste&height=197&id=ueef04bdb&name=image.png&originHeight=197&originWidth=447&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24265&status=done&style=none&taskId=u35c812dc-ee24-466a-9268-bd145be3364&title=&width=447)
鼠标放在inset函数上，就能看到，函数指向返回值是None，那么就知道了，这个函数返回值是None，不建议直接print。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25452484/1658375794177-d89aaa5a-7121-4b81-8965-126cac3aff60.png#clientId=u33afda7d-9fe2-4&from=paste&height=229&id=ubba7e0e5&name=image.png&originHeight=229&originWidth=443&originalType=binary&ratio=1&rotation=0&showTitle=false&size=25960&status=done&style=none&taskId=u7c137aec-7e4d-4a55-a568-8ea89ad205d&title=&width=443)
这个就不一样了，是int型的，那么返回的就是一个整型，例如1，2，3。

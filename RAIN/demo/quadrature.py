import pytest
from allpairspy import AllPairs


def is_valid_combination(row):
    n = len(row)
    # 设置过滤条件
    if n > 2:
        # 一年级 不能匹配 10-13岁
        if "一年级" == row[1] and "10-13岁" == row[2]:
            return False
    return True


parameters = [
    ["男", "女"],
    ["一年级", "二年级", "三年级", "四年级", "五年级"],
    ["8岁以下", "8-10岁", "10-13岁"]
]

print("PAIRWISE:")
for i, pairs in enumerate(AllPairs(parameters, filter_func=is_valid_combination)):
    print("用例编号{}: {}".format(i, pairs))

@pytest.mark.parametrize(["sex", "grade", "age"], [
        value_list for value_list in AllPairs([
            [u"男", u"女"],
            ["一年级", "二年级", "三年级", "四年级", "五年级"],
            ["8岁以下", "8-10岁", "10-13岁"]
        ])
    ])
def test(self, sex, grade, age):
    assert print(sex, grade, age)

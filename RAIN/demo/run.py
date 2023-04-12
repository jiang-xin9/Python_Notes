from selenium import webdriver
from demo.keywords import Keywords
from demo.util import Util


def run_case_from_txt(driver):
    test_data=Util.get_test_data_from_txt("data")
    for line in test_data:
        print("当前执行：{}".format(line))
        key_words=line.split(',')
        if hasattr(Keywords,key_words[0]):
            action=getattr(Keywords,key_words[0]) #调用关键字对应的方法
            result=action(driver,*key_words)
            if not result:
                print('命令执行错误，测试中止。。。。')
                break
            else:
                print('命令执行成功')
if __name__ == '__main__':
    driver=webdriver.Chrome()
    run_case_from_txt(driver)
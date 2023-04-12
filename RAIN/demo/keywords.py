from selenium import webdriver
from selenium.webdriver.common.by import By


class Keywords:
    @classmethod
    def goto(cls,driver,*args):
        if args and len(args)>=2:
            driver.get(args[1])
            return True
        else:
            print("goto命令参数不正确，请检查")
            return False

    @classmethod
    def input(cls,driver,*args):
        if args and len(args)>=3:
            if 'xpath' in args[1]:
                locate_way=By.XPATH
                locator=args[1][6:]
                value=args[2].strip()
            else:
                locate_way = By.ID
                locator = args[1][3:]
                value = args[2].strip()
            driver.find_element(locate_way,locator).send_keys(value)
            return True
        else:
            print('input命令参数不正确，请检查')
            return False

    @classmethod
    def singleclick(cls, driver, *args):
        if args and len(args) >= 2:
            if 'xpath' in args[1]:
                locate_way = By.XPATH
                locator = args[1][6:]
            else:
                locate_way = By.ID
                locator = args[1][3:]
            driver.find_element(locate_way, locator).click()
            return True
        else:
            print('input命令参数不正确，请检查')
            return False

import os
import yaml


class YamlUtil:
    #读取yaml文件
    def read_extract_yaml(self,path):
        root_path2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        DESIRED_CAPS_YAML_PATH = root_path2 + path
        with open(DESIRED_CAPS_YAML_PATH, mode='r',encoding='utf-8') as f:
            value=yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

    #写入yaml文件
    def write_extract_yaml(self,path,data):
        root_path2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        DESIRED_CAPS_YAML_PATH = root_path2 + path
        with open(DESIRED_CAPS_YAML_PATH, mode='a',encoding='utf-8') as f:
            yaml.dump(data=data,stream=f,allow_unicode=True)

    #清除yaml文件
    def clear_extract_yaml(self,path):
        root_path2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        DESIRED_CAPS_YAML_PATH = root_path2 + path
        with open(DESIRED_CAPS_YAML_PATH, mode='w',encoding='utf-8') as f:
            f.truncate()


#没啥好东西



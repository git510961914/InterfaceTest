#!user/bin/python3
#coding=utf-8
from setting import ENVIRONMENT_CONFIG

class EnvironmentModule:
    def __init__(self):
        pass

    def get_env_url(self,env):
        # env_url = ENVIRONMENT_CONFIG[sys.argv[1]]
        # 注意，下面里面的interfaceUrl就是我们setting文件里的名字
        env_url = ENVIRONMENT_CONFIG["interfaceUrl"]
        return env_url[env]
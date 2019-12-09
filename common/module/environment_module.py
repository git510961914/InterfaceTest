#!user/bin/python3
#coding=utf-8
import setting

class EnvironmentModule:
    def __init__(self):
        pass

    def get_env_url(self,env):
        env_url = setting.ENVIRONMENT_CONFIG["interfaceUrl"]
        return env_url[env]

    def set_token(self,token):
        setting.TOKEN['token'] = token
        return True

    def get_token(self):
        token = setting.TOKEN['token']
        return token

    def get_database(self,env):
        database = setting.database[env]
        return database

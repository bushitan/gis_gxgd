#coding:utf-8

from .action_episode import *
from .action_login import *

class actionUtils ():
    def __init__(self):
        self.episode = ActionEpisode()
        self.login = ActionLogin()
        pass

action = actionUtils()
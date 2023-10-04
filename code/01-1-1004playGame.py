# -*- coding: utf-8 -*-
# @Author  : Lulu Lyu
# @Time    : 2023/10/4 20:16
# @E-mail  :lllyuwork@163.com 

import pandas as pd
import numpy as np

if __name__ == "__main__":

    def CCC(repu_self, repu_oppo):
        action = (1, 0)
        return action


    def CCD(repu_self, repu_oppo):
        if repu_self > repu_oppo:
            action = (1, 0)
        elif repu_self == repu_oppo:
            action = (1, 0)
        elif repu_self < repu_oppo:
            action = (0, 1)
        return action


    def CDC(repu_self, repu_oppo):
        if repu_self > repu_oppo:
            action = (1, 0)
        elif repu_self == repu_oppo:
            action = (0, 1)
        elif repu_self < repu_oppo:
            action = (1, 0)
        return action


    def CDD(repu_self, repu_oppo):
        if repu_self > repu_oppo:
            action = (1, 0)
        elif repu_self == repu_oppo:
            action = (0, 1)
        elif repu_self < repu_oppo:
            action = (0, 1)
        return action


    def DCC(repu_self, repu_oppo):
        if repu_self > repu_oppo:
            action = (0, 1)
        elif repu_self == repu_oppo:
            action = (1, 0)
        elif repu_self < repu_oppo:
            action = (1, 0)
        return action


    def DCD(repu_self, repu_oppo):
        if repu_self > repu_oppo:
            action = (0, 1)
        elif repu_self == repu_oppo:
            action = (1, 0)
        elif repu_self < repu_oppo:
            action = (0, 1)
        return action


    def DDC(repu_self, repu_oppo):
        if repu_self > repu_oppo:
            action = (0, 1)
        elif repu_self == repu_oppo:
            action = (0, 1)
        elif repu_self < repu_oppo:
            action = (1, 0)
        return action


    def DDD(repu_self, repu_oppo):
        action = (0, 1)
        return action


    def payoffRepuScore(action_self, action_oppo):
        if action_self == action_oppo and action_self[0] == 1:
            payoff = 3
            repu_change = 0
        elif action_self == action_oppo and action_self[0] == 0:
            payoff = 1
            repu_change = 0
        elif action_self != action_oppo and action_self[0] == 1:
            payoff = 0
            repu_change = 1
        elif action_self != action_oppo and action_self[0] == 0:
            payoff = 5
            repu_change = -1
        return payoff, repu_change


    # 策略的准备工作
    strategy_list = ['CCC', 'CCD', 'CDC', 'CDD', 'DCC', 'DCD', 'DDC', 'DDD']
    repu_list = [0, 0, 0, 0, 0, 0, 0, 0]
    propotion_list = [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]
    strategy_len = len(strategy_list)
# -*- coding: utf-8 -*-
# @Author  : Lulu Lyu
# @Time    : 2023/10/4 15:15
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


    tmax = 100

    # 策略的准备工作
    strategy_list = [CCC, CCD, CDC, CDD, DCC, DCD, DDC, DDD]
    repu_list = [0, 0, 0, 0, 0, 0, 0, 0]
    propotion_list = [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]
    strategy_len = len(strategy_list)

    # 正式博弈——演化
    for t in range(tmax):
        action_total = []
        payoff_total = []
        repu_change_total = []
        for index in range(strategy_len):
            action_list = []
            payoff_list = []
            repu_change_list = []

            repu_temp = repu_list[index]
            strategy_temp = strategy_list[index]

            for index_oppo in range(strategy_len):
                repu_oppo = repu_oppo[index_oppo]
                strategy_oppo = strategy_list[index_oppo]

                # 当前的action
                action_self = globals()[strategy_temp](repu_temp, repu_oppo)
                action_oppo = globals()[strategy_oppo](repu_oppo, repu_temp)
                action_list.append(action_self)

                # 当前得分及声誉变化
                payoff_self, repu_change = payoffRepuScore(action_self, action_oppo)
                payoff_list.append(payoff_self)
                repu_change_list.append(repu_change)

            action_total.append(action_list)
            payoff_total.append(payoff_list)
            repu_change_total.append(repu_change_list)

        # 各种清算
        # 1、repu清算

        # 2、收益清算、群体适应度清算

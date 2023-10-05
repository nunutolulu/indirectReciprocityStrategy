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


    # 计算声誉和收益
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


    # 初始配置，根据人数
    def initialCons(populations, strategy_list):
        # 根据人数，随机选一个策略，保存在列表里
        individual_strategy = []
        repu_total = []
        payoff_total = []
        for i in range(populations):
            strategy_stra = np.random.choice(strategy_list)
            individual_strategy.append(strategy_stra)
            repu.append(0)
            payoff_total.append(0)

        return individual_strategy, repu_total, payoff_total


    # 每次随机选两个，得到行动
    def chooseTwoIndex(populations):
        chosenTwoIndex = np.random.choice(populations, size=2, replace=False)
        one_index = chosenTwoIndex[0]
        another_index = chosenTwoIndex[1]

        return one_index, another_index


    # 根据 index选择行动
    def chooseTwoAction(index_list, individual_strategy, repu):
        one_index = index_list[0]
        another_index = index_list[1]
        one_strategy = individual_strategy[one_index]
        one_repu = repu[one_index]

        another_strategy = individual_strategy[another_index]
        another_repu = repu[another_index]

        action_one = globals()[one_strategy](one_repu, another_repu)
        action_another = globals()[another_strategy](another_repu, one_repu)

        return action_one, action_another


    # 得分
    def score(action_one, action_another):
        if action_one == action_another and action_one[0] == 1:
            payoff = [3, 3]
            repu_change = [0, 0]
        elif action_one == action_another and action_one[0] == 0:
            payoff = [1, 1]
            repu_change = [0, 0]
        elif action_one != action_another and action_one[0] == 1:
            payoff = [0, 5]
            repu_change = [1, -1]
        elif action_one != action_another and action_one[0] == 0:
            payoff = [5, 0]
            repu_change = [-1, 1]
        return payoff, repu_change


    # 策略的准备工作
    strategy_list = ['CCC', 'CCD', 'CDC', 'CDD', 'DCC', 'DCD', 'DDC', 'DDD']
    populations = 100
    individual_strategy, repu_total, payoff_total = initialCons(populations, strategy_list)

    tmax = 500
    couple = 5
    for t in range(tmax):
        index_round = []
        payoff_round = []
        repu_change_round = []
        for c in range(couple):
            # 选择两个index
            index_list = chooseTwoIndex(populations)
            # 选择index对应的action
            action_list = chooseTwoAction(index_list, individual_strategy, repu_total)
            # 根据action计算收益、声誉变化
            payoff_temp, repu_change = score(action_list[0], action_list[1])

            # 暂时存储
            index_round.append(index_list)
            payoff_round.append.append(payoff_temp)
            repu_change_round.append(repu_change)

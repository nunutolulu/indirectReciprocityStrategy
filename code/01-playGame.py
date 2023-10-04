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


    # 策略的准备工作
    strategy_list = ['CCC', 'CCD', 'CDC', 'CDD', 'DCC', 'DCD', 'DDC', 'DDD']
    repu_list = [0, 0, 0, 0, 0, 0, 0, 0]
    propotion_list = [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]
    strategy_len = len(strategy_list)

    # 输出的几个表
    payoff_mean_time = pd.DataFrame(columns=strategy_list)
    repu_time = pd.DataFrame(columns=strategy_list)
    propotion_time = pd.DataFrame(columns=strategy_list)

    tmax = 500

    # 正式博弈——演化
    for t in range(tmax):
        print(t)
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
                repu_oppo = repu_list[index_oppo]
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
        # 1、repu更新-按行计算-遍历计算更新
        repu_change_sum = np.sum(repu_change_total, axis=1)
        for index in range(strategy_len):
            repu_change_temp = repu_change_sum[index]
            repu_list[index] = repu_list[index] + repu_change_temp
        repu_time.loc[len(repu_time)] = repu_list

        # 2、收益更新-按行平均值
        payoff_mean = np.mean(payoff_total, axis=1)
        payoff_mean_time.loc[len(payoff_mean_time)] = payoff_mean

        # 3、群体适应度更新
        # 系统平均适应度
        avg_fitness = np.dot(propotion_list, payoff_mean)
        # 个体适应度更新
        for index in range(strategy_len):
            individual_fitness = payoff_mean[index] * propotion_list[index]
            propotion_list[index] = individual_fitness / avg_fitness
        propotion_time.loc[len(propotion_time)] = propotion_list

    # 输出到csv文件
    propotion_time.to_csv('output/propotion_time.csv', index=True, encoding='utf-8')
    payoff_mean_time.to_csv('output/payoff_mean_time.csv', index=True, encoding='utf-8')
    repu_time.to_csv('output/repu_time.csv', index=True, encoding='utf-8')

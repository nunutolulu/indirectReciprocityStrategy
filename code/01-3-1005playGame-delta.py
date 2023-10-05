# -*- coding: utf-8 -*-
# @Author  : Lulu Lyu
# @Time    : 2023/10/4 20:16
# @E-mail  :lllyuwork@163.com 

import pandas as pd
import numpy as np

if __name__ == "__main__":

    def CCC(repu_self, repu_oppo, delta):
        action = (1, 0)
        return action


    def CCD(repu_self, repu_oppo, delta):
        if repu_self - repu_oppo > delta:
            action = (1, 0)
        elif repu_self - repu_oppo >= 0 and repu_self - repu_oppo <= delta:
            action = (1, 0)
        elif repu_self - repu_oppo < 0:
            action = (0, 1)
        return action


    def CDC(repu_self, repu_oppo, delta):
        if repu_self - repu_oppo > delta:
            action = (1, 0)
        elif repu_self - repu_oppo >= 0 and repu_self - repu_oppo <= delta:
            action = (0, 1)
        elif repu_self - repu_oppo < 0:
            action = (1, 0)
        return action


    def CDD(repu_self, repu_oppo, delta):
        if repu_self - repu_oppo > delta:
            action = (1, 0)
        elif repu_self - repu_oppo >= 0 and repu_self - repu_oppo <= delta:
            action = (0, 1)
        elif repu_self - repu_oppo < 0:
            action = (0, 1)
        return action


    def DCC(repu_self, repu_oppo, delta):
        if repu_self - repu_oppo > delta:
            action = (0, 1)
        elif repu_self - repu_oppo >= 0 and repu_self - repu_oppo <= delta:
            action = (1, 0)
        elif repu_self - repu_oppo < 0:
            action = (1, 0)
        return action


    def DCD(repu_self, repu_oppo, delta):
        if repu_self - repu_oppo > delta:
            action = (0, 1)
        elif repu_self - repu_oppo >= 0 and repu_self - repu_oppo <= delta:
            action = (1, 0)
        elif repu_self - repu_oppo < 0:
            action = (0, 1)
        return action


    def DDC(repu_self, repu_oppo, delta):
        if repu_self - repu_oppo > delta:
            action = (0, 1)
        elif repu_self - repu_oppo >= 0 and repu_self - repu_oppo <= delta:
            action = (0, 1)
        elif repu_self - repu_oppo < 0:
            action = (1, 0)
        return action


    def DDD(repu_self, repu_oppo, delta):
        action = (0, 1)
        return action


    # 初始配置，根据人数
    def initialCons(populations, strategy_list):
        # 根据人数，随机选一个策略，保存在列表里
        individual_strategy = []
        repu_total = []
        payoff_total = []
        for i in range(populations):
            strategy_stra = np.random.choice(strategy_list)
            individual_strategy.append(strategy_stra)
            repu_total.append(0)
            payoff_total.append(0)

        return individual_strategy, repu_total, payoff_total


    # 每次随机选两个，得到行动
    def chooseTwoIndex(populations):
        chosenTwoIndex = np.random.choice(populations, size=2, replace=False)
        one_index = chosenTwoIndex[0]
        another_index = chosenTwoIndex[1]

        return one_index, another_index


    # 根据 index选择行动
    def chooseTwoAction(index_list, individual_strategy, repu, delta):
        one_index = index_list[0]
        another_index = index_list[1]
        one_strategy = individual_strategy[one_index]
        one_repu = repu[one_index]

        another_strategy = individual_strategy[another_index]
        another_repu = repu[another_index]

        action_one = globals()[one_strategy](one_repu, another_repu, delta)
        action_another = globals()[another_strategy](another_repu, one_repu, delta)

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


    # 索引统计
    def countIndex(ten_index_list):
        indices = {}
        for index, item in enumerate(ten_index_list):
            if item in indices:
                indices[item].append(index)
            else:
                indices[item] = [index]
        # print(indices)
        return indices


    # 策略占比统计
    def propotion_strategy_count(individual_strategy, strategy_list):
        # se = pd.Series(individual_strategy)
        # propotionDict = dict(se.value_counts(normalize=True))
        propotionDict = dict()
        for i in strategy_list:
            propotionDict[i] = individual_strategy.count(i) / len(individual_strategy)

        propotion_df = pd.DataFrame([propotionDict])
        return propotion_df


    # 策略的准备工作
    strategy_list = ['CCC', 'CCD', 'CDC', 'CDD', 'DCC', 'DCD', 'DDC', 'DDD']
    populations = 100
    individual_strategy, repu_total, payoff_total = initialCons(populations, strategy_list)

    payoff_mean_time = pd.DataFrame(columns=np.arange(populations))
    repu_time = pd.DataFrame(columns=np.arange(populations))
    propotion_time = propotion_strategy_count(individual_strategy, strategy_list)
    payoff_mean_time.loc[len(payoff_mean_time)] = payoff_total
    repu_time.loc[len(repu_time)] = repu_total

    tmax = 5000
    couple = 5
    delta = 1
    for t in range(tmax):
        print(t)
        index_round = []
        payoff_round = []
        repu_change_round = []
        for c in range(couple):
            # 选择两个index
            index_list = chooseTwoIndex(populations)
            # 选择index对应的action
            action_list = chooseTwoAction(index_list, individual_strategy, repu_total, delta)
            # 根据action计算收益、声誉变化
            payoff_temp, repu_change = score(action_list[0], action_list[1])

            # 暂时存储
            index_round.append(index_list)
            payoff_round.append(payoff_temp)
            repu_change_round.append(repu_change)

        # 之前存储的内容，在整个群体统一更新(声誉和收益）——声誉是累积的，但是收益每一代平均一下
        ten_index_list = [element for subindex in index_round for element in subindex]
        ten_payoof_list = [element for subpayoff in payoff_round for element in subpayoff]
        ten_repu_change_list = [element for subrepuchange in repu_change_round for element in subrepuchange]
        # 选择相同元素索引值——产生的indices为字典类型，key为list的数值，values为key的索引
        indices = countIndex(ten_index_list)
        for individual_index, list_index in indices.items():
            payoff_collect = []
            repu_change_collect = []
            for index in list_index:
                payoff_collect.append(ten_payoof_list[index])
                repu_change_collect.append(ten_repu_change_list[index])
            individual_mean_payoff = np.mean(payoff_collect)
            individual_sum_repu_change = np.sum(repu_change_collect)

            payoff_total[individual_index] = individual_mean_payoff
            repu_total[individual_index] = repu_total[individual_index] + individual_sum_repu_change

        # 费米更新规则——更新策略
        update_index = chooseTwoIndex(populations)
        payoff_one = payoff_total[update_index[0]]
        payoff_another = payoff_total[update_index[1]]
        # epsilon = 1.0 / (1 + np.exp(np.sum(payoff_me) - np.sum(payoff_opponent)) / 1)
        epsilon = 1.0 / (1 + np.exp((payoff_one - payoff_another) / 0.1))
        if np.random.random(1) < epsilon:
            individual_strategy[update_index[0]] = individual_strategy[update_index[1]]

        payoff_mean_time.loc[len(payoff_mean_time)] = payoff_total
        repu_time.loc[len(repu_time)] = repu_total
        propotion_now = propotion_strategy_count(individual_strategy, strategy_list)
        propotion_time = pd.concat([propotion_time, propotion_now])
    # 输出
    payoff_mean_time.to_csv('output/payoff_mean_time_delta.csv', index=True, encoding='utf-8')
    repu_time.to_csv('output/repu_time_delta.csv', index=True, encoding='utf-8')
    propotion_time.to_csv('output/propotion_time_delta.csv', index=True, encoding='utf-8')

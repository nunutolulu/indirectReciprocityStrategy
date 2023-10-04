# -*- coding: utf-8 -*-
# @Author  : Lulu Lyu
# @Time    : 2023/10/4 15:15
# @E-mail  :lllyuwork@163.com 


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


    def payoffScore(action_self, action_oppo):
        if action_self == action_oppo and action_self[0] == 1:
            payoff = 3
        elif action_self == action_oppo and action_self[0] == 0:
            payoff = 1
        elif action_self != action_oppo and action_self[0] == 1:
            payoff = 0
        elif action_self != action_oppo and action_self[0] == 0:
            payoff = 5
        return payoff


    tmax = 100
    strategy_list = [CCC, CCD, CDC, CDD, DCC, DCD, DDC, DDD]
    repu_list = [0, 0, 0, 0, 0, 0, 0, 0]
    propotion_list = [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]

    strategy_len = len(strategy_list)
    for t in range(tmax):
        action_total = []
        payoff_total = []
        for index in range(strategy_len):
            action_list = []
            payoff_list = []

            repu_temp = repu_list[index]
            strategy_temp = strategy_list[index]

            for index_oppo in range(strategy_len):
                repu_oppo = repu_oppo[index_oppo]
                strategy_oppo = strategy_list[index_oppo]

                # 当前的action
                action_self = globals()[strategy_temp](repu_temp, repu_oppo)
                action_oppo = globals()[strategy_oppo](repu_oppo, repu_temp)
                action_list.append(action_self)

                # 当前得分
                payoff_self = payoffScore(action_self, action_oppo)
                payoff_list.append(payoff_self)

                # 声誉的变化

                
            action_total.append(action_list)
            payoff_total.append(payoff_list)


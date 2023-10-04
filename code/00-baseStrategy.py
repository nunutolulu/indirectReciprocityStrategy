# -*- coding: utf-8 -*-
# @Author  : Lulu Lyu
# @Time    : 2023/9/28 18:25
# @E-mail  :lllyuwork@163.com 


# (1,0)代表合作，(0,1)代表背叛

# CCC
class strategyCCC():
    name = "CCC"

    def __init__(self, repu_self, repu_oppo):
        self.repu_self = repu_self
        self.repu_oppo = repu_oppo
        self.action(self.repu_self, self.repu_oppo)

    def action(self, repu_self, repu_oppo):
        action = (1, 0)
        return action

# CCD
class strategyCCD():
    name = "CCD"

    def __init__(self, repu_self, repu_oppo):
        self.repu_self = repu_self
        self.repu_oppo = repu_oppo
        self.action(self.repu_self, self.repu_oppo)

    def action(self, repu_self, repu_oppo):
        if repu_self > repu_oppo:
            action = (1, 0)
        elif repu_self == repu_oppo:
            action = (1, 0)
        elif repu_self < repu_oppo:
            action = (0, 1)
        return action


# CDC
class strategyCDC():
    name = "CDC"

    def __init__(self, repu_self, repu_oppo):
        self.repu_self = repu_self
        self.repu_oppo = repu_oppo
        self.action(self.repu_self, self.repu_oppo)

    def action(self, repu_self, repu_oppo):
        if repu_self > repu_oppo:
            action = (1, 0)
        elif repu_self == repu_oppo:
            action = (0, 1)
        elif repu_self < repu_oppo:
            action = (1, 0)
        return action


# CDD
class strategyCDD():
    name = "CDD"

    def __init__(self, repu_self, repu_oppo):
        self.repu_self = repu_self
        self.repu_oppo = repu_oppo
        self.action(self.repu_self, self.repu_oppo)

    def action(self, repu_self, repu_oppo):
        if repu_self > repu_oppo:
            action = (1, 0)
        elif repu_self == repu_oppo:
            action = (0, 1)
        elif repu_self < repu_oppo:
            action = (0, 1)
        return action


# DCC
class strategyDCC():
    name = "DCC"

    def __init__(self, repu_self, repu_oppo):
        self.repu_self = repu_self
        self.repu_oppo = repu_oppo
        self.action(self.repu_self, self.repu_oppo)

    def action(self, repu_self, repu_oppo):
        if repu_self > repu_oppo:
            action = (0, 1)
        elif repu_self == repu_oppo:
            action = (1, 0)
        elif repu_self < repu_oppo:
            action = (1, 0)
        return action


# DCD
class strategyDCD():
    name = "DCD"

    def __init__(self, repu_self, repu_oppo):
        self.repu_self = repu_self
        self.repu_oppo = repu_oppo
        self.action(self.repu_self, self.repu_oppo)

    def action(self, repu_self, repu_oppo):
        if repu_self > repu_oppo:
            action = (0, 1)
        elif repu_self == repu_oppo:
            action = (1, 0)
        elif repu_self < repu_oppo:
            action = (0, 1)
        return action


# DDC
class strategyDDC():
    name = "DDC"

    def __init__(self, repu_self, repu_oppo):
        self.repu_self = repu_self
        self.repu_oppo = repu_oppo
        self.action(self.repu_self, self.repu_oppo)

    def action(self, repu_self, repu_oppo):
        if repu_self > repu_oppo:
            action = (0, 1)
        elif repu_self == repu_oppo:
            action = (0, 1)
        elif repu_self < repu_oppo:
            action = (1, 0)
        return action


# DDD
class strategyDDD():
    name = "DDD"

    def __init__(self, repu_self, repu_oppo):
        self.repu_self = repu_self
        self.repu_oppo = repu_oppo
        self.action(self.repu_self, self.repu_oppo)

    def action(self, repu_self, repu_oppo):
        action = (0, 1)
        return action


# 得分
class score():
    def __init__(self, action_one, action_other):
        self.R = 3
        self.S = 0
        self.T = 5
        self.P = 1
        self.action_one = action_one
        self.action_other = action_other

    def play(self, action_one, action_other):
        if action_one == action_other and action_one[0] == 1:
            payoff = [3, 3]
            # repu = [1, 1]
        elif action_one == action_other and action_one[0] == 0:
            payoff = [1, 1]
        elif action_one != action_other and action_one[0] == 1:
            payoff = [0, 5]
        elif action_one != action_other and action_one[0] == 0:
            payoff = [5, 0]
        return payoff


if __name__ == "__main__":

    # def CCC():

    tmax = 100
    strategy_list = [strategyCCC(), strategyCCD(), strategyCDC(), strategyCDD(), strategyDCC(), strategyDCD(),
                     strategyDDC(), strategyDDD()]
    repu_list = [0, 0, 0, 0, 0, 0, 0, 0]
    propotion_list = [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]
    for t in range(tmax):
        # 两两博弈确定行动
        for index in range(len(strategy_list)):
            action_list=[]
            repu_temp = repu_list[index]
            for index_oppo in range(len(strategy_list)):
                repu_oppo = repu_list[index_oppo]
                # action=

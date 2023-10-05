# -*- coding: utf-8 -*-
# @Author  : Lulu Lyu
# @Time    : 2023/10/4 16:35
# @E-mail  :lllyuwork@163.com 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['font.sans-serif'] = ['SimHei']


    def propotion():
        propotion_time = pd.read_csv('output/propotion_time_delta.csv', index_col=0,
                                     encoding='utf-8')
        times = len(propotion_time)
        x = np.arange(times)
        y_ccc = propotion_time['CCC'].tolist()
        y_ccd = propotion_time['CCD'].tolist()
        y_cdc = propotion_time['CDC'].tolist()
        y_cdd = propotion_time['CDD'].tolist()
        y_dcc = propotion_time['DCC'].tolist()
        y_dcd = propotion_time['DCD'].tolist()
        y_ddc = propotion_time['DDC'].tolist()
        y_ddd = propotion_time['DDD'].tolist()

        fig = plt.figure(figsize=(16, 8))
        plt.title('各策略占比情况', fontsize=26, loc='center', color='k')
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.xlabel('Generation')
        plt.ylabel('Propotion')

        plt.plot(x, y_ccc, label='CCC', color='red')
        plt.plot(x, y_ccd, label='CCD', color='green')
        plt.plot(x, y_cdc, label='CDC', color='blue')
        plt.plot(x, y_cdd, label='CDD', color='black')
        plt.plot(x, y_dcc, label='DCC', color='pink')
        plt.plot(x, y_dcd, label='DCD', color='orange')
        plt.plot(x, y_ddc, label='DDC', color='purple')
        plt.plot(x, y_ddd, label='DDD', color='aqua')

        plt.legend()
        plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
        plt.savefig('output/propotion_delta.png', bbox_inches='tight')
        plt.show()


    def propotion_mutation():
        propotion_time = pd.read_csv('output/propotion_time_delta_mutation.csv', index_col=0,
                                     encoding='utf-8')
        times = len(propotion_time)
        x = np.arange(times)
        y_ccc = propotion_time['CCC'].tolist()
        y_ccd = propotion_time['CCD'].tolist()
        y_cdc = propotion_time['CDC'].tolist()
        y_cdd = propotion_time['CDD'].tolist()
        y_dcc = propotion_time['DCC'].tolist()
        y_dcd = propotion_time['DCD'].tolist()
        y_ddc = propotion_time['DDC'].tolist()
        y_ddd = propotion_time['DDD'].tolist()

        fig = plt.figure(figsize=(16, 8))
        plt.title('各策略占比情况-突变', fontsize=26, loc='center', color='k')
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.xlabel('Generation')
        plt.ylabel('Propotion')

        plt.plot(x, y_ccc, label='CCC', color='red')
        plt.plot(x, y_ccd, label='CCD', color='green')
        plt.plot(x, y_cdc, label='CDC', color='blue')
        plt.plot(x, y_cdd, label='CDD', color='black')
        plt.plot(x, y_dcc, label='DCC', color='pink')
        plt.plot(x, y_dcd, label='DCD', color='orange')
        plt.plot(x, y_ddc, label='DDC', color='purple')
        plt.plot(x, y_ddd, label='DDD', color='aqua')

        plt.legend()
        plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
        plt.savefig('output/propotion_delta_mutation.png', bbox_inches='tight')
        plt.show()


    def payoff_mean():
        payoff_mean_time = pd.read_csv('output/payoff_mean_time.csv', index_col=0, encoding='utf-8')
        x = np.arange(0, 10001)
        y_ccc = payoff_mean_time['CCC'].tolist()
        y_ccd = payoff_mean_time['CCD'].tolist()
        y_cdc = payoff_mean_time['CDC'].tolist()
        y_cdd = payoff_mean_time['CDD'].tolist()
        y_dcc = payoff_mean_time['DCC'].tolist()
        y_dcd = payoff_mean_time['DCD'].tolist()
        y_ddc = payoff_mean_time['DDC'].tolist()
        y_ddd = payoff_mean_time['DDD'].tolist()

        fig = plt.figure(figsize=(16, 8))
        plt.title('各策略每轮平均收益', fontsize=26, loc='center', color='k')
        plt.xlabel('Generation')
        plt.ylabel('Payoff_mean')

        plt.plot(x, y_ccc, label='CCC', color='red')
        plt.plot(x, y_ccd, label='CCD', color='green')
        plt.plot(x, y_cdc, label='CDC', color='blue')
        plt.plot(x, y_cdd, label='CDD', color='black')
        plt.plot(x, y_dcc, label='DCC', color='pink')
        plt.plot(x, y_dcd, label='DCD', color='orange')
        plt.plot(x, y_ddc, label='DDC', color='purple')
        plt.plot(x, y_ddd, label='DDD', color='aqua')

        plt.legend()
        plt.yticks([0, 0.5, 1, 1.5, 2, 2.5, 3])
        plt.savefig('output/payoff.png', bbox_inches='tight')
        plt.show()


    def repu():
        repu_time = pd.read_csv('output/repu_time.csv', index_col=0, encoding='utf-8')
        x = np.arange(0, 500)
        y_ccc = repu_time['CCC'].tolist()
        y_ccd = repu_time['CCD'].tolist()
        y_cdc = repu_time['CDC'].tolist()
        y_cdd = repu_time['CDD'].tolist()
        y_dcc = repu_time['DCC'].tolist()
        y_dcd = repu_time['DCD'].tolist()
        y_ddc = repu_time['DDC'].tolist()
        y_ddd = repu_time['DDD'].tolist()

        fig = plt.figure(figsize=(16, 8))
        plt.title('各策略累积声誉', fontsize=26, loc='center', color='k')
        plt.xlabel('Generation')
        plt.ylabel('Reputation')

        plt.plot(x, y_ccc, label='CCC', color='red')
        plt.plot(x, y_ccd, label='CCD', color='green')
        plt.plot(x, y_cdc, label='CDC', color='blue')
        plt.plot(x, y_cdd, label='CDD', color='black')
        plt.plot(x, y_dcc, label='DCC', color='pink')
        plt.plot(x, y_dcd, label='DCD', color='orange')
        plt.plot(x, y_ddc, label='DDC', color='purple')
        plt.plot(x, y_ddd, label='DDD', color='aqua')

        plt.legend()
        plt.savefig('output/reputation.png', bbox_inches='tight')
        plt.show()


    propotion()
    propotion_mutation()
    # payoff_mean()
    # repu()

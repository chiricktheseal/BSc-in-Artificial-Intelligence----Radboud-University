#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:32:29 2024

@author: Angelina and Maria (group 53)
"""

import matplotlib.pyplot as plt

# depth 2
# minmax data
d2_w_mm = [482, 688, 1261, 8969]
d2_h_mm = [482, 526, 762, 1462]
d2_n_mm = [482, 482, 514]
d2_mm = d2_w_mm + d2_h_mm + d2_n_mm

# alpha beta data
d2_w_ab = [171, 218, 331, 1330]
d2_h_ab = [171, 189, 269, 514]
d2_n_ab = [171, 169, 186]
d2_ab = d2_w_ab + d2_h_ab + d2_n_ab

# depth 3
# minmax data
d3_w_mm = [2401, 3972, 9268, 135042]
d3_h_mm = [2401, 2747, 3965, 7875]
d3_n_mm = [2401, 2374, 2359]
d3_mm = d3_w_mm + d3_h_mm + d3_n_mm

# alpha beta data
d3_w_ab = [617, 876, 1568, 10287]
d3_h_ab = [617, 695, 1033, 2073]
d3_n_ab = [617, 613, 613]
d3_ab = d3_w_ab + d3_h_ab + d3_n_ab

# depth 4
# minmax data
d4_w_mm = [16150, 30176, 86044, 2323304]
d4_h_mm = [16150, 17950, 25085, 47320]
d4_n_mm = [16150, 16207, 16239]
d4_mm = d4_w_mm + d4_h_mm + d4_n_mm

# alpha beta data
d4_w_ab = [1030, 1459, 2612, 17955]
d4_h_ab = [1030, 1187, 1742, 3482]
d4_n_ab = [1030, 934, 936]
d4_ab = d4_w_ab + d4_h_ab + d4_n_ab

# depth 5
# minmax data
d5_w_mm = [86164, 184768, 665631, 37542386]
d5_h_mm = [86164, 101624, 143240, 285935]
d5_n_mm = [86164, 85969, 85898]
d5_mm = d5_w_mm + d5_h_mm + d5_n_mm

# alpha beta data
d5_w_ab = [5046, 7951, 17013, 190319]
d5_h_ab = [5046, 6012, 8830, 18290]
d5_n_ab = [5046, 5122, 5133]
d5_ab = d5_w_ab + d5_h_ab + d5_n_ab


plt.figure()
plt.scatter(d2_ab, d2_mm, color = 'blue', label = 'Depth 2')
plt.scatter(d3_ab, d3_mm, color = 'red', label = 'Depth 3')
plt.scatter(d4_ab, d4_mm, color = 'green', label = 'Depth 4')
plt.scatter(d5_ab, d5_mm, color = 'purple', label = 'Depth 5')
plt.xlabel('Alpha-beta Pruning')
plt.ylabel('MiniMax')
plt.title('Number of evaluations')
plt.xlim(0, 10000)
plt.ylim(0, 200000)
plt.legend()
plt.show()


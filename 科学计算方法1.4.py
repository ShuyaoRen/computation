# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:30:14 2024

@author: Tu_Ruby
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
from scipy.interpolate import interp1d, lagrange, CubicSpline

# 模拟温度数据
days = np.array([1, 2, 3, 4, 5, 6, 7])
temperature = np.array([22.1, 21.9, 23.4, 24.5, 25.0, 24.8, 22.7])

# 三次样条插值
cs = CubicSpline(days, temperature)

# 生成细致的天数数据
days_fine = np.linspace(1, 7, 100)
temperature_interp = cs(days_fine)

# 绘制结果
plt.plot(days, temperature, 'o', label='原始数据')
plt.plot(days_fine, temperature_interp, label='三次样条插值')
plt.title('温度数据的三次样条插值')
plt.xlabel('天数')
plt.ylabel('温度 (°C)')
plt.legend()
plt.grid(True)
plt.show()


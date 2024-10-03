# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:01:36 2024

@author: Tu_Ruby
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
from scipy.interpolate import interp1d, lagrange, CubicSpline

# 定义目标函数
def f(x):
    return np.sin(3 * np.pi * x) * np.exp(-x)

# 生成插值点
x = np.linspace(0, 1, 10)
y = f(x)

# 生成更细的点用于误差计算
x_fine = np.linspace(0, 1, 100)
y_true = f(x_fine)

# 线性插值
linear_interp = interp1d(x, y, kind='linear')
y_linear = linear_interp(x_fine)

# 三次样条插值
cubic_spline = CubicSpline(x, y)
y_cubic = cubic_spline(x_fine)

# 拉格朗日插值
lagrange_interp = lagrange(x, y)
y_lagrange = lagrange_interp(x_fine)

# 计算误差
error_linear = np.abs(y_true - y_linear)
error_cubic = np.abs(y_true - y_cubic)
error_lagrange = np.abs(y_true - y_lagrange)

# 绘制误差图
plt.figure(figsize=(10, 6))
plt.plot(x_fine, error_linear, label="线性插值误差", color='blue')
plt.plot(x_fine, error_cubic, label="三次样条插值误差", color='green')
plt.plot(x_fine, error_lagrange, label="拉格朗日插值误差", color='red')
plt.title('三种插值方法的误差对比')
plt.xlabel('x')
plt.ylabel('误差')
plt.legend()
plt.grid(True)
plt.show()




import numpy as np
import matplotlib.pyplot as plt

# 元の関数を定義
def func(x):
    return np.exp(x)

# グラフを描画するためのx軸の値を定義
x = np.linspace(0, 4, 50)

# 元の関数をプロット
plt.plot(x, func(x), 'o', label='Original Function')

# polyfitを使用して近似関数を求める
coefficients = np.polyfit(x, np.log(func(x)), 1)
a = np.exp(coefficients[1])
b = coefficients[0]

# 近似関数を定義
approx_func = lambda x: a * np.exp(b*x)

# 近似関数をプロット
plt.plot(x, approx_func(x), label='Approximation')

plt.legend()
plt.show()
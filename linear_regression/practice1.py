import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 读取去除0后的数据
data = pd.read_csv('sale_land_1000_nozero.csv')

# 去除包含 NaN 的行
data = data.dropna()

# 降低多项式阶数为2
m = 6


coef = np.polyfit(data['LAND SQUARE FEET'], data['SALE PRICE'], deg=m)
f = np.poly1d(coef)

x_line = np.linspace(data['LAND SQUARE FEET'].min(), data['LAND SQUARE FEET'].max(), 400)
y_line = f(x_line)

plt.figure(figsize=(10,6.18))
plt.scatter(data['LAND SQUARE FEET'], data['SALE PRICE'], s=30, label='Noisy data')
plt.plot(x_line, y_line, linewidth=2, label=f'Polyfit (degree={m})')
plt.xlabel('LAND SQUARE FEET')
plt.ylabel('SALE PRICE')
plt.title('SALE PRICE vs LAND SQUARE FEET')
plt.legend()
plt.show()

print(f(1000))



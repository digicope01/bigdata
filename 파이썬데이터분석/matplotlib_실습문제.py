# matplotlib_실습문제.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('boston_train.csv')

# 1.1번 로그플롯
crim = df['CRIM'].values
medv = df['MEDV'].values

poly = np.polyfit(crim,np.log(medv),deg=1) # 학습
print(type(poly))
print('Poly',poly[0]) # W, 기울기
print('Poly',poly[1]) # b, y절편
# plt.plot(crim,np.log(medv),'o')
# plt.show()
plt.semilogy(crim,medv,'o')
plt.semilogy(crim,np.exp(np.polyval(poly,crim)))
plt.title('1.1 Boston crim/zn medv scatter plot')

plt.show()
print(df.corr())


# 1.2번 분산 플롯
crim = df['CRIM'].values
medv = df['MEDV'].values
zn = df['ZN'].values

# c: color, s:size, apha:투명도
plt.scatter(crim,medv,c = 200*crim,
            s =20 + 200*zn/zn.max(),
            alpha = 0.5)  # 버블차트

plt.grid(True)
plt.xlabel('crim')
plt.ylabel('medv')
plt.title('1.2 Boston crim/zn medv scatter plot')
plt.show()

# 1.3 번
crim = df['CRIM'].values
medv = df['MEDV'].values

poly = np.polyfit(crim,np.log(medv),deg=1) # 학습
plt.plot(crim, np.polyval(poly, crim), label='Fit')

medv_start = int(medv.mean())
print(medv_start )
y_ann = np.log(df.at[medv_start, 'MEDV']) - 0.1
print(y_ann)
ann_str = "Medv Crime\n %d" % medv_start
plt.annotate(ann_str, xy=(medv_start, y_ann),
             arrowprops=dict(arrowstyle="->"),
             xytext=(-30, +70), textcoords='offset points')

cnt_log = np.log(medv)
plt.scatter(crim, cnt_log, c= 200 * crim,
            s=20 + 200 * zn/zn.max(),
            alpha=0.5, label="Scatter Plot")
plt.legend(loc='upper right')
plt.grid()
plt.xlabel("Crime")
plt.ylabel("Medv", fontsize=16)
plt.title("1.3 Boston Housing : Crime Medv")
plt.show()

# 1.4번
from mpl_toolkits.mplot3d.axes3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = df['CRIM'].values

Y = np.where(df['MEDV'].values>0, np.log(df['MEDV'].values), 0)
X, Y = np.meshgrid(X, Y)

Z = np.where(df['ZN'].values>0, np.log(df['ZN'].values), 0)
# Z =Z.reshape(1,Z.shape[0])
Z,_ =np.meshgrid(Z,0)

ax.plot_surface(X, Y, Z)
ax.set_xlabel('CRIME')
ax.set_ylabel('MEDV')
ax.set_zlabel('ZN')
ax.set_title("1.4 Boston Housing : Crime/ZN  Medv")
plt.show()

#  1.5번
from pandas.plotting import lag_plot

lag_plot(np.log(df['MEDV']))
plt.title('1.5 Boston lag_plot')
plt.show()

#  1.6번
from pandas.plotting import autocorrelation_plot
autocorrelation_plot(np.log(df['MEDV']))

plt.title('1.6 Boston autocorrelation_plot')
plt.show()

# 1.7번

df.plot.box()
plt.title('1.7.1 Boston Box plot')
plt.show()

df['TAX'].plot.box()
plt.boxplot(df['TAX'],labels=['TAX'])
plt.text(1, df['TAX'].median(), df['TAX'].median())

plt.title('1.7.2 Boston TAX Box plot')
plt.show()

plt.boxplot(df['TAX'],labels=['TAX'])
plt.text(1, df['TAX'].median(), df['TAX'].median())
plt.title('1.7.3 Boston TAX Box plot')
plt.show()

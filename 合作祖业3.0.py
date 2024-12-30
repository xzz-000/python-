import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib. pyplot as plt

# 为可视化设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题


#读取数据
df = pd.read_excel("data.xlsx", "Sheet1",
 index_col="序号")
  # 去除空白数据
df = df.dropna().drop(columns="姓名")
  # 去除非法数据
df = df[(df["年龄"] <= 100) & (df["BMI"] <= 60)]

# 绘制性别比例# 统计性别分布
gender_counts = df['性别'].value_counts()

# #绘制饼状图
plt.figure(figsize=(6, 6))
plt.pie(gender_counts,
        autopct='%1.1f%%',
        colors=['skyblue', 'lightpink'],
        startangle=90,
        wedgeprops={'edgecolor': 'black'},
        labeldistance=1.1,  # 调整标签位置，默认为1.1
        textprops={'fontsize': 14, 'color': 'black', 'fontweight': 'bold'})  # 修改字体样式

plt.title('患者性别比例'
          '  男  女   ')



# 将年龄数据分成若干段
bins = [20, 30, 40, 50, 60, 70, 80]
labels = ['20-30', '30-40', '40-50', '50-60', '60-70', '70+']
df['年龄段'] = pd.cut(df['年龄'], bins=bins, labels=labels, right=False)

# 绘制年龄段分布的频率直方图
plt.figure(figsize=(8, 6))
df['年龄段'].value_counts().sort_index().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('年龄段分布')
plt.xlabel('年龄段')
plt.ylabel('人数')
plt.xticks(rotation=45)




# 绘制肿瘤分期分布的频率直方图
plt.figure(figsize=(8, 6))
df['肿瘤分期'].value_counts().sort_index().plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('肿瘤分期分布')
plt.xlabel('肿瘤分期')
plt.ylabel('人数')
plt.xticks(rotation=0)  # 保持分期标签水平显示
plt.show()




# 假设真实值和预测值
y_true = np.array([2.5, 3.5, 4.0, 5.1, 6.3, 7.8, 8.0])
y_pred = np.array([2.4, 3.6, 3.9, 5.0, 6.5, 7.5, 8.1])

# 绘制散点图
plt.scatter(y_true, y_pred, color='blue')
plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], color='red', linestyle='--')  # 预测值 = 真实值的线
plt.title('真实值与预测值对比')
plt.xlabel('真实值')
plt.ylabel('预测值')


# 假设真实值与预测值按顺序排列
x = np.arange(len(y_true))

plt.plot(x, y_true, label='真实值', color='blue', marker='o')
plt.plot(x, y_pred, label='预测值', color='green', marker='x')
plt.title('预测值与真实值的时间序列对比')
plt.xlabel('样本索引')
plt.ylabel('值')
plt.legend()
plt.show()


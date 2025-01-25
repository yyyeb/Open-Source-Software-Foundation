import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
df = pd.read_csv('Commits over time.csv')

total_commits = df['Commits'].sum()
print(f"总提交次数为: {total_commits}")

df['年份'] = pd.to_datetime(df['Week of']).dt.year
yearly_commits = df.groupby('年份')['Commits'].sum().reset_index()
print(yearly_commits)

# 获取系统中已安装的字体文件路径
font_list = matplotlib.font_manager.fontManager.ttflist

# 遍历字体文件列表,找到包含"SimHei"的字体文件路径
for font in font_list:
    if "SimHei" in font.name:
        font_path = font.fname
        break
font = FontProperties(fname=font_path)

plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['text.color'] = '#333333'
plt.rcParams['axes.labelcolor'] = '#555555'

plt.figure(figsize=(10, 6))
plt.plot(yearly_commits['年份'], yearly_commits['Commits'], color='#1f77b4', linewidth=2)
plt.grid(color='#f0f0f0', linestyle='--', linewidth=1)
plt.tick_params(axis='both', which='major', length=6, width=1, color='#777777')

plt.title('每年总提交次数', fontsize=16, fontweight='bold', fontproperties=font)
plt.xlabel('年份', fontsize=14, fontproperties=font)
plt.ylabel('提交次数', fontsize=14, fontproperties=font)
plt.xticks(yearly_commits['年份'][::2], rotation=45, ha='right', fontproperties=font)

plt.annotate(f"总提交次数: {total_commits}", xy=(0.05, 0.95), xycoords='axes fraction',
              fontsize=12, va='top', fontproperties=font)

plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)

plt.show()
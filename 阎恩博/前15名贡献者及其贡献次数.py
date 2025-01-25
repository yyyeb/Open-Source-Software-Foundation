import matplotlib
import requests
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置GitHub API的访问地址
repo_owner = 'prestosql'
repo_name = 'presto'
api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contributors'

# 发送GET请求,获取贡献者信息
response = requests.get(api_url)
contributors = response.json()

# 提取前15名贡献者的用户名和提交次数
top_contributors = sorted(contributors, key=lambda x: x['contributions'], reverse=True)[:15]
names = [contributor['login'] for contributor in top_contributors]
commits = [contributor['contributions'] for contributor in top_contributors]

# 输出贡献次数最多的15人及其贡献次数
print("Presto项目贡献次数最多的15人及其贡献次数:")
for i in range(len(names)):
    print(f"{names[i]}: {commits[i]}")

# 获取系统中已安装的字体文件路径
font_list = matplotlib.font_manager.fontManager.ttflist

# 遍历字体文件列表,找到包含"SimHei"的字体文件路径
for font in font_list:
    if "SimHei" in font.name:
        font_path = font.fname
        break
font = FontProperties(fname=font_path)

# 绘制柱状图
plt.figure(figsize=(12, 6))
plt.bar(names, commits)

# 在每个柱顶部标注具体的贡献次数
for i, v in enumerate(commits):
    plt.text(i, v, str(v), ha='center', va='bottom', fontsize=8)

plt.xticks(rotation=90)
plt.xlabel('贡献者',fontproperties=font)
plt.ylabel('提交次数',fontproperties=font)
plt.title('Presto项目前15名贡献者',fontproperties=font)
plt.tight_layout()
plt.show()
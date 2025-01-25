import json
from collections import defaultdict
import matplotlib.pyplot as plt

# 1. 定义文件路径
file_path = r'C:\Users\scmb\Desktop\presto_prs.json'  # 使用原始字符串（raw string）避免转义问题

# 2. 读取 JSON 数据
with open(file_path, 'r', encoding='utf-8') as f:  # 确保使用 UTF-8 编码读取文件
    data = json.load(f)

# 3. 统计 PR 的标签分布（贡献来源）
label_stats = defaultdict(int)

for pr in data:
    for label in pr['labels']:
        label_name = label['name']
        label_stats[label_name] += 1

# 4. 合并低于 4% 的标签为 "Other"
total_labels = sum(label_stats.values())
filtered_labels = {}
other_count = 0

for label, count in label_stats.items():
    percentage = (count / total_labels) * 100
    if percentage >= 4:  # 保留占比 >= 4% 的标签
        filtered_labels[label] = count
    else:  # 合并占比 < 4% 的标签
        other_count += count

if other_count > 0:  # 如果有低于 4% 的标签，添加 "Other"
    filtered_labels['Other'] = other_count

# 5. 绘制标签分布的饼状图
labels = list(filtered_labels.keys())
label_counts = list(filtered_labels.values())

plt.figure(figsize=(8, 8))
plt.pie(label_counts, labels=labels, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen', 'lightcoral', 'gold', 'orange', 'pink'])
plt.title('PR Label Distribution (Contribution Source)')
plt.show()

# 6. 统计 PR 的状态分布
state_stats = defaultdict(int)

for pr in data:
    state = pr['state']
    if pr['merged_at']:  # 如果 merged_at 不为空，说明 PR 已合并
        state = 'merged'
    state_stats[state] += 1

# 7. 绘制 PR 状态分布的饼状图
states = list(state_stats.keys())
state_counts = list(state_stats.values())

plt.figure(figsize=(8, 8))
plt.pie(state_counts, labels=states, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen', 'lightcoral'])
plt.title('PR State Distribution')
plt.show()
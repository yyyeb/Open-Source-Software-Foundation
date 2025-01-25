import pandas as pd

# 定义文件路径
json_file_path = r'C:\Users\scmb\Desktop\presto_prs.json'  # JSON文件路径
csv_file_path = r'C:\Users\scmb\Desktop\output.csv'  # CSV文件保存路径

# 读取JSON文件
df = pd.read_json(json_file_path)

# 将数据保存为CSV文件
df.to_csv(csv_file_path, index=False)

print(f"CSV文件已保存到: {csv_file_path}")
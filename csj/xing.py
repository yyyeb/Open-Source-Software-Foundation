import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 请求GitHub API获取特定owner和repo的信息
owner = 'prestodb'
repo = 'presto'
URL = f'https://api.github.com/repos/{owner}/{repo}'

r = requests.get(URL, verify=False)

# 打印状态码
print("Status code:", r.status_code)

# 解析返回的JSON数据
response_dict = r.json()

# 打印repo的基本信息
print("Repository name:", response_dict['name'])
print("Repository description:", response_dict['description'])
print("Stars:", response_dict['stargazers_count'])
print("Forks:", response_dict['forks_count'])

# 使用Pygal创建一个简单的图表，显示星标数和Fork数
names = ['Stars', 'Forks']
values = [response_dict['stargazers_count'], response_dict['forks_count']]

# 设置图表样式
my_style = LS('#333366', base_style=LCS)

# 创建条形图
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

# 设置图表标题
chart.title = f'{owner}/{repo} Repository Statistics'

# 设置X轴标签
chart.x_labels = names

# 添加数据
chart.add('Count', values)

# 渲染图表并保存为SVG文件
chart.render_to_file('presto_repo_statistics.svg')

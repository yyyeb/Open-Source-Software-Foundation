import requests
import time
import pandas as pd
from datetime import datetime
from lxml import etree

token = ''

# 定义repo_owner和repo_name
repo_owner = 'prestodb'  # GitHub用户名
repo_name = 'presto'     # GitHub仓库名

# 修改后的url，包含正确的repo_owner和repo_name
url = f'https://api.kkgithub.com/repos/{repo_owner}/{repo_name}/discussions?stage=all'
headers = {
    'Authorization': f'token {token}'  # 使用token进行身份验证
}

with open('response_data2.txt', 'a', encoding='utf-8') as f:
    for i in range(1, 50):
        while True:
            try:
                # 修改请求 URL 为 discussions
                response = requests.get(
                    f"https://api.kkgithub.com/repos/{repo_owner}/{repo_name}/discussions?q=is%3Adiscussion+is%3Aopen&page={i}", 
                    headers=headers
                )
                
                # 确保response对象包含内容
                if response.status_code == 200:
                    f.write(f"第{i}页爬取的内容:\n")
                    f.write(response.text + "\n")  # 将response.text写入文件
                    f.write("\n" + "=" * 50 + "\n")  # 每次请求后添加分隔符
                    print(f"第{i}页爬取完毕")
                else:
                    print(f"第{i}页请求失败，状态码：{response.status_code}")
                
                time.sleep(2)
                break
            except requests.exceptions.RequestException as e:
                print(f"请求异常：{e}")
                print("Connection was refused by the server...")
                time.sleep(2)
                print("ReConnecting...")
                continue

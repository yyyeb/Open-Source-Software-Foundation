import requests
import time
import pandas as pd
from datetime import datetime
from lxml import etree
#token =   # GitHub个人Token（替换为你自己的token）
#url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues?stage=all'
headers = {
    'Authorization': f'token {token}'  # 使用token进行身份验证
}
with open('response_data2.txt', 'a', encoding='utf-8') as f:
    for i in range(1, 50):
        while True:
            try:
                response = requests.get(
                    #f"https://github.com/prestodb/presto/issues?q=is%3Aissue%20state%3Aopen&page={i}",timeout=(30,50),verify=False,headers=headers)

                f"https://api.github.com/repos/prestodb/presto/issues?q=is%3Aissue+is%3Aopen&page={i}",headers=headers)
                #print(response.text)
                f.write(f"第{i}页爬取的内容:\n")
                f.write(response2.text + "\n")  # 将response.text写入文件
                f.write("\n" + "=" * 50 + "\n")  # 每次请求后添加分隔符
                print("第" + str(i) + "页爬取完毕")
                time.sleep(2)
                break
            except:
                print("Connection was refused by the server...")
                time.sleep(2)
                print("ReConnecting...")
                continue

#print(issues)
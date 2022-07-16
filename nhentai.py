from pathlib import Path
import os
import requests
from bs4 import BeautifulSoup
import random
import time

# 指定要查詢的路徑
books = 'C:/Users/88697/Desktop/nhenail/Books'
myPath = books
delay_choises = [8, 5, 10, 6, 20, 11]                       # 可選的延遲秒數
delay = random.choice(delay_choises)                        # 隨機選擇秒數 因為怕被認為是爬蟲被擋
# 列出指定路徑底下所有檔案(包含資料夾)
allFileList = os.listdir(myPath)
# 逐一查詢檔案清單
n = 0                                                       # 第幾本
for file in allFileList:
    resp = requests.get('https://nhentai.to/g/'+file)       # 查看網頁請求
    soup = BeautifulSoup(resp.text, 'html.parser')          # 開始爬蟲
    if str(resp) == '<Response [404]>':                     # 如果找不到網頁 code:404
        pass
    elif str(resp) == '<Response [200]>':                   # 找到網頁  code:202
        file_oldname = os.path.join(myPath, file)
        s = soup.h2.text.replace('\\', ' ').replace('/', ' ').replace('*', ' ').replace('?', ' ').replace('"', ' ') \
        .replace('<', ' ').replace('>', ' ').replace('|', ' ').replace(':', ' ')
        file_newname_newfile = os.path.join(myPath, file + s)  # code:202 修改檔名
        os.rename(file_oldname, file_newname_newfile)       # 實際修改檔名
    else:                                                   # 其他錯誤
        pass
    print("第 {} 本，ID : {}".format(n, file))
    n = n + 1
    time.sleep(delay)                                       # 爬蟲延遲

